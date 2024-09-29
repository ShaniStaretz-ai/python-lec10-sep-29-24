# ex1:
from random import randint
#
# l1 = [i * 2 for i in range(1, 11)]
# l2 = [i for i in range(99, 60 - 3, -3)]
# l3 = [randint(1, 100) for _ in range(10)]
# print("l1:", l1)
# print("l2:", l2)
# print("l3:", l3)
#
# l4 = [int(input("Enter number:")) for _ in range(10)]
# print("l4:", l4)
# # ex3
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = [x for x in fruits if "a" in x]#only with if
# newList = [x if x != "banana" else "orange" for x in fruits]  # with if,else
# # if x!="banana", append x, else append "orange"
# print(newList)

# ex4:
l4 = [randint(-50, 50) for _ in range(10)]
l5 = [x for x in l4 if x % 2 == 0]
l6 = [x for x in l4 if x > 0]

print("l4:", l4)
print("l5:", l5)
print("l6:", l6)
