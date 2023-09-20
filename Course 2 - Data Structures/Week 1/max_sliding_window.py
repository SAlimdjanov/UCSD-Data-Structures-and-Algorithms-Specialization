"""
max_sliding_window.py

"""

from collections import deque


def max_sliding_window(sequence, num_n):
    """
    Maximum value in sliding window

    Args:
        sequence (int list): Input sequence
        num_n (int): length of input sequence

    Returns:
        int list: list of maximums

    """
    _deque, maximums, sequence_len = deque(), [], len(sequence)
    for i in range(sequence_len):
        while _deque and sequence[i] >= sequence[_deque[-1]]:
            _deque.pop()
        _deque.append(i)
        if i >= num_n and _deque and _deque[0] == i - num_n:
            _deque.popleft()
        if i >= num_n - 1:
            maximums.append(sequence[_deque[0]])
    return maximums


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window(input_sequence, window_size))
