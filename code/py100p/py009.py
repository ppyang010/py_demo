# 实现对列表的去重


def get_unique_list(listA):
    result = []
    for item in listA:
        if item not in result:
            result.append(item)
    return result


listA = [3, 5, 7, 9, 11, 11, 7, 3, 13]

print(f"source list {listA}, unique list: ", get_unique_list(listA))

# 利用set去重集合的特性实现
print(f"source list {listA}, unique list: ", list(set(listA)))
