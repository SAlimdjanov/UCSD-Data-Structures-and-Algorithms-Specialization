# python3

""" 
phi_x_174_error_free_overlap.py

Given a list of error-free reads, Genome Assembly is performed and the circular genome from which 
they came is returned.

"""

import sys


class SuffixArray:
    """
    Build a suffix array. Refer to "Algorithms on Strings" for explanation of functions in this
    class that are not documented.

    """

    def _sort_characters(self, _text):
        """Sort the characters of an input text"""
        _len_text, _count = len(_text), {}
        _order = [0] * _len_text
        for i in range(_len_text):
            _count[_text[i]] = _count.get(_text[i], 0) + 1
        _chars = sorted(_count.keys())
        _prev_char = _chars[0]
        for char in _chars[1:]:
            _count[char] += _count[_prev_char]
            _prev_char = char
        for i in range(_len_text - 1, -1, -1):
            _char = _text[i]
            _count[_char] = _count[_char] - 1
            _order[_count[_char]] = i
        return _order

    def _compute_char_classes(self, _text, _order):
        """Compute classes of characters"""
        _len_text = len(_text)
        _char_class = [0] * _len_text
        _char_class[_order[0]] = 0
        for i in range(1, _len_text):
            if _text[_order[i]] != _text[_order[i - 1]]:
                _char_class[_order[i]] = _char_class[_order[i - 1]] + 1
            else:
                _char_class[_order[i]] = _char_class[_order[i - 1]]
        return _char_class

    def _sort_doubled(self, _text, _l, _prev_order, _prev_class):
        """Sort doubled cyclic shifts"""
        _len_text = len(_text)
        _count = [0] * _len_text
        _new_order = [0] * _len_text
        for i in range(_len_text):
            _count[_prev_class[i]] += 1
        for j in range(1, _len_text):
            _count[j] += _count[j - 1]
        for i in range(_len_text - 1, -1, -1):
            start = (_prev_order[i] - _l + _len_text) % _len_text
            _class = _prev_class[start]
            _count[_class] -= 1
            _new_order[_count[_class]] = start
        return _new_order

    def _update_classes(self, _new_order, _prev_class, _l):
        """Update character classes"""
        _len_new_order = len(_new_order)
        _new_classes = [0] * _len_new_order
        _new_classes[_new_order[0]] = 0
        for i in range(1, _len_new_order):
            _current_class = _new_order[i]
            _prev = _new_order[i - 1]
            _mid_prev = _current_class + _l
            _mid_prev = (_prev + _l) % _len_new_order
            if (
                _prev_class[_current_class] != _prev_class[_prev]
                or _prev_class[_mid_prev] != _prev_class[_mid_prev]
            ):
                _new_classes[_current_class] = _new_classes[_prev] + 1
            else:
                _new_classes[_current_class] = _new_classes[_prev]
        return _new_classes

    def build_suffix_array(self, _text):
        """Builds a suffix array with string text"""
        _len_text = len(_text)
        _order = self._sort_characters(_text)
        _class = self._compute_char_classes(_text, _order)
        _l = 1
        while _l < _len_text:
            _order = self._sort_doubled(_text, _l, _order, _class)
            _class = self._update_classes(_order, _class, _l)
            _l = 2 * _l
        return _order

    def __init__(self, _text):
        self.order = self.build_suffix_array(_text)


class AssembleErrorFree:
    """Genome assembly with error-free data reads"""

    def __init__(self):
        data = self._read_data()
        genome = self.genome_assembly(data)
        print(genome)

    def _read_data(self):
        """Read input data, terminated by EOF keyboard interrupt (ctrl+Z on Windows)"""
        return list(set(sys.stdin.read().strip().split()))

    def bwt_suffix_array(self, _text, _order):
        """
        Constructs the Burrows-Wheeler Transform (BWT) of the input text based on the specified
        order from the suffix array.

        Args:
            _text (str): Input text
            _order (list): Suffix array

        Returns:
            tuple: The BWT of _text, dictionary with starting positions of each character in BWT,
                   dictionary with counts of each character occurrence in the BWT at different
                   indices.

        """
        _l = len(_text)
        _counts, _starts = {}, {}
        _chars = ["$", "A", "C", "G", "T"]
        _bwt = [""] * _l
        for i in range(_l):
            _bwt[i] = _text[(_order[i] + _l - 1) % _l]
        for char in _chars:
            _counts[char] = [0] * (_l + 1)
        for i in range(_l):
            _current_char = _bwt[i]
            for char, _ in _counts.items():
                _counts[char][i + 1] = _counts[char][i]
            _counts[_current_char][i + 1] += 1
        _current_index = 0
        for char in sorted(_chars):
            _starts[char] = _current_index
            _current_index += _counts[char][_l]
        return _bwt, _starts, _counts

    def longest_overlap(self, _text, _patterns):
        """
        Finds the longest overlapping suffix between the input text and a list of patterns. Had to
        set k = 1 instead of k = 12 (recommended in the assignment sheet) for this to actually
        work.

        Args:
            _text (str): Input text
            _patterns (list): List of pattern strings

        Returns:
            tuple: The index of the pattern with the longest overlapping suffix, length of the
                   longest overlapping suffix between the pattern and the input text.

        """
        _order, _k = SuffixArray(_text).order, 1
        bwt, starts, counts = self.bwt_suffix_array(_text, _order)
        _l, _occurences = len(_text) - 1, {}
        for i, _p in enumerate(_patterns):
            _pattern = _p[:_k]
            _top, _bottom = 0, len(bwt) - 1
            _current_index = len(_pattern) - 1
            while _top <= _bottom:
                if _current_index >= 0:
                    _symbol = _pattern[_current_index]
                    _current_index -= 1
                    if counts[_symbol][_bottom + 1] - counts[_symbol][_top] > 0:
                        _top = starts[_symbol] + counts[_symbol][_top]
                        _bottom = starts[_symbol] + counts[_symbol][_bottom + 1] - 1
                    else:
                        break
                else:
                    for j in range(_top, _bottom + 1):
                        if not _order[j] in _occurences:
                            _occurences[_order[j]] = []
                        _occurences[_order[j]].append(i)
                    break
        _overlap, i = 0, 0
        for _index, _list in sorted(_occurences.items()):
            for i in _list:
                if _text[_index:-1] == _patterns[i][: _l - _index]:
                    return i, _l - _index
        return i, _overlap

    def genome_assembly(self, _data):
        """
        Assembles the genome given the input data.

        Args:
            _data (list): Input data (reads)

        Returns:
            str: Assembled genome from reads

        """
        _genome = _data[0]
        _current_index = 0
        _first_data_read = _data[_current_index]
        while True:
            _current_data_read = _data[_current_index]
            if len(_data) == 1:
                break
            del _data[_current_index]
            _current_index, _overlap = self.longest_overlap(
                _current_data_read + "$", _data
            )
            _genome += _data[_current_index][_overlap:]
        _current_index, _overlap = self.longest_overlap(
            _data[0] + "$", [_first_data_read]
        )
        if _overlap > 0:
            return _genome[:-_overlap]
        return _genome


if __name__ == "__main__":
    AssembleErrorFree()
