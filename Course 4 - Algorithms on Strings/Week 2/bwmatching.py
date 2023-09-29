# python3

""" 
bwtmatching.py

"""


def preprocess_bwt(_bwt_text):
    """
    Preprocesses the bwt string to be examined by count_occurences()

    Args:
        _bwt_text (str): Text after BWT is applied

    Returns:
        dict, dict: first occurence, count

    """
    _len_bwt_text = len(_bwt_text)
    _char_counts = {"$": 0, "A": 0, "C": 0, "G": 0, "T": 0}
    for _char in _bwt_text:
        _char_counts[_char] += 1
    _chars = ["$", "A", "C", "G", "T"]
    _first_occurence = {"$": 0}
    for i in range(1, 5):
        _first_occurence[_chars[i]] = (
            _first_occurence[_chars[i - 1]] + _char_counts[_chars[i - 1]]
        )
    _count = {}
    for _char in _chars:
        _count[_char] = [0] * (_len_bwt_text + 1)
    for i in range(_len_bwt_text):
        temp = {_bwt_text[i]: 1}
        for _char in _chars:
            _count[_char][i + 1] = _count[_char][i] + temp.get(_char, 0)
    return _first_occurence, _count


def count_occurences(_bwt_text, _pattern, _first_occurence, _count):
    """
    Implementation of the better version of the BWMatching algorithm

    Args:
        _bwt_text (str): BWT string
        _pattern (str): Pattern string
        _first_occurence (dict): First occurence
        _count (dict): character count

    Returns:
        int: Number of occurences of the pattern string in the text, 0 if the pattern is not in
             the string.

    """
    _top = 0
    _bottom = len(_bwt_text) - 1
    while _top <= _bottom:
        if _pattern:
            _char = _pattern[-1]
            _pattern = _pattern[:-1]
            _top = _first_occurence[_char] + _count[_char][_top]
            _bottom = _first_occurence[_char] + _count[_char][_bottom + 1] - 1
        else:
            return _bottom - _top + 1
    return 0


if __name__ == "__main__":
    bwt_text = input()
    num_p = int(input())
    patterns = list(input().split())
    first_occurence, count = preprocess_bwt(bwt_text)
    for pattern in patterns:
        occurences = count_occurences(bwt_text, pattern, first_occurence, count)
        print(occurences, end=" ")
