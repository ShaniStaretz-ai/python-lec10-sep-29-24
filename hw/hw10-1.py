from random import randint, choice

l1: list[int] = [i for i in range(95, 106)];
print("95-105:", l1);
l2: list[int] = [i for i in range(10, 22, 2)];
print("10-20 evens:", l2);
l3: list[int] = [choice([True, False]) for _ in range(5)];
print("random booleans:", l3);
l4: list[int] = [randint(1, 100) for _ in range(10)];
print("random 1-100:", l4);
l5: list[int] = [x for x in l4 if x > 50];
print("bigger than 50:", l5);
l6: list[int] = [x for x in [randint(1, 100) for _ in range(10)] if x > 50]
print("random bigger than 50:", l6);

str_l7: str = input("enter sentence:");
l7: list[str] = [letter for letter in str_l7 if letter not in [' ', 't']];
print("sentence without 't' or space:", l7);
l8: list[int] = [randint(10, 99) for _ in range(10)];
print("random 1-100:", l8);
l9: list[int] = [x % 10 for x in l8];
print("last digits:", l9);


l9=[]
for i in range(l8):
    l9.append(l8[i]%10)
print(l9)