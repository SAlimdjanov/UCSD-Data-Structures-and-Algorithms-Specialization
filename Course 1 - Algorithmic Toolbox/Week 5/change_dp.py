"""
change_dp.py

"""


def change(money):
    """Money change with dynamic programming"""
    min_num_coins = [0] + [float("inf")] * money
    coins = [1, 3, 4]
    for i in range(1, money + 1):
        for j in range(len(coins)):
            if i >= coins[j]:
                num_coins = min_num_coins[i - coins[j]] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins
    return min_num_coins[money]


if __name__ == "__main__":
    money_val = int(input())
    print(change(money_val))
