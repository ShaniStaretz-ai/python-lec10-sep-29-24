# python-lec10-sep-29-24

## Subjects learnt today:

1) List Comprehension: only in for loop:
   simple example:put each i in range 0-11 in list l1
   ```
   l1=[i for i in range(11)]
   ```
    * the first i is the value to append in the list
    * The return value is a new list, leaving the old list unchanged.
      another with if: if 'a' in x append in newList
   ```
   fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
   newlist = [x for x in fruits if "a" in x]
   print(newlist)
   ```
    * another example:
   ```
   newlist = [x if x != "banana" else "orange" for x in fruits]
   ```
   meaning append x if x!="banana", else (if x="banana") append "orange" instead of the "banana"
    * general: newL=[item for iterator in list if condition==True]
    *
2) Error handling:

## Extra:

1) to init list of 10 with zeros:

 ```
count_numbers:list=[0]*10
 ```
