# python3

"""
bwtinverse.py

"""


def bwt_inverse(_bwt_text):
    """
    Computes the Inverse Burrows-Wheeler transform of a string

    Args:
        _bwt_text (str): A BWT string containing '$'

    Returns:
        str: The original string before BWT

    """
    _char_counts = {"$": 0, "A": 0, "C": 0, "G": 0, "T": 0}
    for _char in _bwt_text:
        _char_counts[_char] += 1
    _tmp_var = -1
    _positions = {}
    for _char in ["$", "A", "C", "G", "T"]:
        _tmp_var += _char_counts[_char]
        _positions[_char] = _tmp_var
    _array = [0] * len(_bwt_text)
    for i in range(len(_bwt_text) - 1, -1, -1):
        _array[i] = _positions[_bwt_text[i]]
        _positions[_bwt_text[i]] -= 1
    _initial_text = "$"
    _index = 0
    for i in range(len(_bwt_text) - 1):
        _initial_text += _bwt_text[_index]
        _index = _array[_index]
    _initial_text = _initial_text[::-1]
    return _initial_text


if __name__ == "__main__":
    bwt_text = input()
    print(bwt_inverse(bwt_text))
