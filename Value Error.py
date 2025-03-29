try:
    age=int(input("Enter age: "))
    if age<18:
        raise ValueError("Age should be greater than 18")
    else:
        print("Age is valid")
except ValueError as e:
    print(e)