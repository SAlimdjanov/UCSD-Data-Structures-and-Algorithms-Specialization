""" 
max_ad_revenue.py

"""


def max_ad_revenue(num_n, price_list, clicks_list):
    """
    Computes the maximum possible ad revenue through maximizing the dot product of the two lists

    Args:
        num_n (int): Number of elements in both lists
        price_list (list, int): List of prices
        clicks_list (list, int): List of clicks

    Returns:
        int: The maximized dot product between the two lists

    """
    price_list.sort(reverse=True)
    clicks_list.sort(reverse=True)
    dot_product = 0
    for i in range(num_n):
        dot_product += price_list[i] * clicks_list[i]
    return dot_product


if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(max_ad_revenue(n, p, c))
