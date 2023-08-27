"""
money_change.py

"""


def money_change(money):
    """Returns minumum number of coins with denominations 1, 5, and 10"""
    if 1 <= money <= 10**3:
        coins = 0
        while money > 0:
            if money >= 10:
                money -= 10
            elif money >= 5:
                money -= 5
            else:
                money -= 1
            coins += 1
        return coins
    return None


if __name__ == "__main__":
    amount = int(input())
    print(money_change(amount))
