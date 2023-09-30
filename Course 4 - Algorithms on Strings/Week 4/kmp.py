# python3

""" 
kmp.py

Finds all occurrences of a pattern (Pattern) in a string (Genome).

"""


def precompute_prefix(_pattern):
    """
    Precompute prefixes (KMP Failure function)

    Args:
        _pattern (str): Pattern string

    Returns:
        _type_: Failure values for each index in _pattern

    """
    _len_pattern, _fail = len(_pattern), 0
    _prefixes = [0] * _len_pattern
    for i in range(1, _len_pattern):
        while _fail > 0 and _pattern[i] != _pattern[_fail]:
            _fail = _prefixes[_fail - 1]
        if _pattern[i] == _pattern[_fail]:
            _fail += 1
        else:
            _fail = 0
        _prefixes[i] = _fail
    return _prefixes


def find_kmp(_pattern, _text):
    """
     Knuth-Morris-Pratt (KMP) string matching algorithm

    Args:
        _pattern (str): Pattern string
        _text (str): Text string

    Returns:
        list: Starting indices of all occurrences _pattern in _text

    """
    _len_pattern, _result = len(_pattern), []
    _str = _pattern + "$" + _text
    _len_str = len(_str)
    _precompute = precompute_prefix(_str)
    for i in range(_len_pattern + 1, _len_str):
        if _precompute[i] == _len_pattern:
            _result.append(i - 2 * _len_pattern)
    return _result


if __name__ == "__main__":
    pattern = input()
    text = input()
    positions = find_kmp(pattern, text)
    for pos in positions:
        print(pos, end=" ")
