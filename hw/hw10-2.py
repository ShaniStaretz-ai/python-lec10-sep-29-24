# a. try-except let the program the option to run without crushing by a failed action.
# b. it's better to catch the exceptions, because if one of the actions in the program failed,
# the program will crush

from random import randint

# c.
try:
    88 / 0;
except ZeroDivisionError:
    print("can't dived a number by zero");

# d.
try:
    height = float(input("enter height:"));
    if not 1.4 <= height <= 3.0:
        raise ValueError("must be within range (1.4,3.0)");
# e.
except ValueError as error:
    print("error in height programs:", error);

# e.
SENTINEL: int = -999;
l1 = [randint(1, 10) for i in range(4)];
print("l1:", l1);
try:
    while True:
        num = int(input("enter number of index, between 0-9:"))
        if num == SENTINEL:
            print("goodbye!")
            break;
        if not 0 <= num <= 9:
            raise IndexError(f"The value '{num}' is not in the range of the list, must be between 0-9 including");
        print(f"In index {num} you have the value:'{l1[num]}'");
except IndexError as e:
    print(f"\033[1;31mError in input:{e}\033[0m");
except ValueError:
    print(f"\033[1;31mError in Input:must be a number\033[0m");
