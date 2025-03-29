try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is : ",result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("please enter numerical value")
except NameError as ex:
    print("The exception is ",ex)
except:
    print("Some error occurred")
finally:
     print("I will execute no matter what happens")