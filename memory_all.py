a=10
b=20
print("Id of a:", id(a))
print("Id of b:", id(b))
if a is b:
    print("a and b refers to the same object")
else:
    print("a and b do not refer to the same obj")