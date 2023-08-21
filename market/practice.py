# import random
#
# nums = [1, 4, 3, 2, 0, 8, 12]
# target = random.randint(1, 10)
# print(target)
# first_index = 0
# for i in nums:
#     second_index = 0
#     for n in nums:
#         if i != n and i + n == target:
#             print(i, n)
#             print(first_index, second_index)
#         second_index += 1
#     first_index += 1

# nums = [1, 2, 3, 4, 5]
# res = []
# for i in range(len(nums)):
#     res.append(nums[i])
#
# res2 = res+res
# print(res2)

# a = 5
# b = a
# a = 20
# print(b)
#
# my_s = {1, 2, 3, 1, 1, 4}
# print(my_s)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Приклад використання:
# Створюємо бінарне дерево:
#      1
#     / \
#    2   3
#   /
#  4
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(4)
root.left.left = Node(4)
root.left.left.left = Node(4)


print(count_nodes(root))  # Виводить: 4