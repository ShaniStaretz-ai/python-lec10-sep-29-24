# ex1:
while True:
    try:
        height = float(input("enter height:"))
        if not 1.4 <= height <= 3.0:
            raise ValueError("must be within range (1.4,3.0)", height)# or continue
        break
    except ValueError as e:
        print("invalid height:", e)
print("the right height is:", height)
