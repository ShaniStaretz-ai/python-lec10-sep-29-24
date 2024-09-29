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
   newlist = [x if x != "banana" else "orange" for x in fruits]# like ternary-operator, see extra section
   ```
   meaning append x if x!="banana", else (if x="banana") append "orange" instead of the "banana"
    * general: newL=[item for iterator in list if condition==True]
    *
2) Error handling:
    * "ValueError" -an example for an error type,when expected int got string
    * "IndexError"- count=None error type, try to reach list out of range
    * "TypeError" - when type count+=1, when count=None
    * "Exception" - the prototype origin, will catch all exceptions.
    1. To create error: with the keyword: *raise*. this will load/ raise the error to the air .
       need to catch it, to prevent stopping.
       ```
       raise ValueError("must be within the range of the list")
       ```
    2. we want to catch this error, in order to prevent the program from stopping:

    * we use TryExcept:
       ```
      try:
      . . . . 
      except:
         print("cought error") 
       ```
   * after specifying all exceptions types, better to catch all others that weren't specified above it
   * to print the given error: 
     ```
     except ValueError as e:
        print("invalid height:", e)
     ```
## Extra:

1) to init list of 10 with zeros:

 ```
count_numbers:list=[0]*10
 ```
2) ternary-operator: (self learning)
* a shortcut to assign a value to a parameter, by result of condition:
 ```
 print(f"{'+' if temperature > 0 else '-'}{temperature}C", end=' '); 
 min = "a is minimum" if a < b else "b is minimum"
 ```
