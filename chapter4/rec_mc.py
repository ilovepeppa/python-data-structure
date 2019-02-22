def rec_mc(coins, change, known_results):
    min_coins = change
    if change in coins:
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coins if c < change]:
            nums = 1 + rec_mc(coins, change - i, known_results)
            if nums < min_coins:
                min_coins = nums
                known_results[change] = min_coins

    return min_coins


def dp_make_change(coin_value_list, change, min_coins, used_coins):
    for cents in range(change + 1):
        coin_count = cents
        used_coin = 0
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                used_coin = j
        min_coins[cents] = coin_count
        used_coins[cents] = used_coin

    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        c_coin = coins_used[change]
        coin -= c_coin
        print(c_coin)


if __name__ == '__main__':
    amount = 63
    clist = [1, 5, 10, 21, 25]
    coin_used = [0] * (amount + 1)
    coin_count = [0] * (amount + 1)

    dp_make_change(clist, amount, coin_count, coin_used)
    print_coins(coin_used, amount)
