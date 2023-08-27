""" 
max_ad_revenue.py

"""


def max_ad_revenue(num_n, price_list, clicks_list):
    """Computes the max dot product of the two lists"""
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
