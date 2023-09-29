# python3

"""
bwt.py

"""


def bwt(_text):
    """
    Computes the Burrows-Wheeler transform of a string

    Args:
        _text (str): An input string with end delimiter '$'. E.g., AA$

    Returns:
        str: Burrows-Wheeler Transformed string

    """
    _m, _len_text = [_text], len(_text)
    for _ in range(1, _len_text):
        _text = _text[-1] + _text[:-1]
        _m.append(_text)
    _m.sort()
    _bwt_text = ""
    for i in _m:
        _bwt_text += i[-1]
    return _bwt_text


if __name__ == "__main__":
    text = input()
    print(bwt(text))
