# 从列表中移除多个元素
# 其实就是求差集


def remove_list(listA, listB):
    for item in listB:
        listA.remove(item)
    return listA


listA = [3, 5, 7, 9, 11, 13]
listB = [11, 7]

print(f"from {listA} rmove {listB} result: ", remove_list(listA, listB))

listA = [3, 5, 7, 9, 11, 11, 13]
listB = [11, 7]

# 列表推导式的方式
new_listA = [item for item in listA if item not in listB]
print(f"from {listA} rmove {listB} result: ", new_listA)
