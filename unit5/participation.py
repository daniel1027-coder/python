age = int(input("enter the age: "))


if age < 2 :
    print(f"That the person is a baby")
elif age < 4 :
    print(f"That the person is a toddler")
elif age < 13 :
    print(f"That the person is a kid")
elif age < 20 : 
    print(f"That the person is a teenager")
elif age < 65 :
    print(f"That the person is a adult")
else: 
    print(f"That the person is an elder")