# python3

""" 
suffix_array_long.py

Constructs the suffix array of a string.

"""


def sort_characters(_text):
    """
    Sort the characters of an input text

    Args:
        _text (str): Text string

    Returns:
        list: Characters of _text in order

    """
    _len_text = len(_text)
    _char_order = [0] * _len_text
    _char_count = {"$": 0, "A": 0, "C": 0, "G": 0, "T": 0}
    for char in _text:
        _char_count[char] += 1
    _chars = ["$", "A", "C", "G", "T"]
    for i in range(1, 5):
        _char_count[_chars[i]] += _char_count[_chars[i - 1]]
    for j in range(_len_text - 1, -1, -1):
        _char = _text[j]
        _char_count[_char] -= 1
        _char_order[_char_count[_char]] = j
    return _char_order


def compute_char_classes(_text, _order):
    """
    Compute classes of characters

    Args:
        _text (str): Text string
        _order (list): Character order

    Returns:
        list: Character classes

    """
    _len_text = len(_text)
    _char_class = [0] * _len_text
    for i in range(1, _len_text):
        if _text[_order[i]] == _text[_order[i - 1]]:
            _char_class[_order[i]] = _char_class[_order[i - 1]]
        else:
            _char_class[_order[i]] = _char_class[_order[i - 1]] + 1
    return _char_class


def sort_doubled(_text, _l, _prev_order, _prev_class):
    """
    Sorts doubled cyclic shifts

    Args:
        _text (str): Text string
        _l (int): Length of sort string
        _prev_order (list): Previously obtained character orders
        _prev_class (list): Previously obtained character classes

    Returns:
        list: New order of characters after sorting

    """
    _len_text = len(_text)
    _count = [0] * _len_text
    _new_order = [0] * _len_text
    for i in range(_len_text):
        _count[_prev_class[i]] += 1
    for i in range(1, _len_text):
        _count[i] += _count[i - 1]
    for j in range(_len_text - 1, -1, -1):
        start = (_prev_order[j] - _l + _len_text) % _len_text
        _class = _prev_class[start]
        _count[_class] -= 1
        _new_order[_count[_class]] = start
    return _new_order


def update_classes(_new_order, _prev_class, _l):
    """
    Updates character classes

    Args:
        _new_order (list): New order of characters
        _prev_class (list): Previously obtained character classes
        _l (int): Length of sort string

    Returns:
        list: New character classes

    """
    _len_new_order = len(_new_order)
    _new_classes = [0] * _len_new_order
    for i in range(1, _len_new_order):
        _current = _new_order[i]
        _midpoint = (_current + _l) % _len_new_order
        _previous = _new_order[i - 1]
        _mid_prev = (_previous + _l) % _len_new_order
        if (
            _prev_class[_current] == _prev_class[_previous]
            and _prev_class[_midpoint] == _prev_class[_mid_prev]
        ):
            _new_classes[_current] = _new_classes[_previous]
        else:
            _new_classes[_current] = _new_classes[_previous] + 1
    return _new_classes


def build_suffix_array(_text):
    """
    Builds a suffix array

    Args:
        _text (str): Text string

    Returns:
        list: Suffix array

    """
    _order = sort_characters(_text)
    _class = compute_char_classes(_text, _order)
    _l = 1
    while _l < len(_text):
        _order = sort_doubled(_text, _l, _order, _class)
        _class = update_classes(_order, _class, _l)
        _l = 2 * _l
    return _order


if __name__ == "__main__":
    text = input()
    suffix_array = build_suffix_array(text)
    for index in suffix_array:
        print(index, end=" ")
