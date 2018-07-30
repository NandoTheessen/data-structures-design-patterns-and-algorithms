def make_change(amount, denominations):
    ways = [1] + [0] * amount
    for element in denominations:
        for i in range(element, amount + 1):
            ways[i] += ways[i-element]

    return ways[amount]

print(make_change(100, [1, 2]))
