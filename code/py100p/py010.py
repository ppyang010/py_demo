# 对简单列表排序  列表元素不是复合对象

listA = [3, 5, 7, 9, 11, 11, 7, 3, 13]
# 在原数组中排序
# 默认升序  设置reverse=True 改为倒序
listA.sort(reverse=True)
print(f"listA={listA}")

listB = [3, 5, 7, 9, 11, 11, 7, 3, 13]
# 使用函数排序
# 默认升序  设置reverse=True 改为倒序
newListB = sorted(listB, reverse=True)
print(f"newListB={newListB}")
