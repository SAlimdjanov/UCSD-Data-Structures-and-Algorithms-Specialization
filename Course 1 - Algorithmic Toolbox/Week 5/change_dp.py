"""
change_dp.py

"""


def change(money):
    """
    Solves the money change problem with dynamic programming

    Args:
        money (int): Amount of money

    Returns:
        int: minimum number of coins required to have the amount 'money'

    """
    min_num_coins = [0] + [float("inf")] * money
    coins = [1, 3, 4]
    len_coins = len(coins)

    for i in range(1, money + 1):
        for j in range(len_coins):
            if i >= coins[j]:
                num_coins = min_num_coins[i - coins[j]] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins

    return min_num_coins[money]


if __name__ == "__main__":
    money_val = int(input())
    print(change(money_val))
