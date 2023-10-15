def sweap_max(items: list) -> list:
    max_item = items[0]
    item_zero = items[0]
    for i in range(1, len(items)):
        if items[i] > max_item:
            max_item = items[i]
            items[0] = items[i]
            max_pos = i
    items[max_pos] = item_zero
    return items

print(sweap_max([2,8,10,0,5,7]))

