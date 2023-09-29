# python3

""" 
suffix_array.py

"""


def build_suffix_array(_text):
    """
    Builds a suffix array with an input string

    Args:
        _text (str): Input text ending with '$'

    Returns:
        list: Suffix array

    """
    _suffixes, _len_text = [], len(_text)
    for i in range(_len_text):
        _suffixes.append((_text[i:], i))
    _suffixes.sort()
    _suffix_array = []
    for _elem in _suffixes:
        _suffix_array.append(_elem[1])
    return _suffix_array


if __name__ == "__main__":
    text = input()
    suffix_array = build_suffix_array(text)
    for index in suffix_array:
        print(index, end=" ")
