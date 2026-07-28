try:
    a = int(input("Enter the first Number: "))

    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform. \nPress + for additon\npress - for subtraction\npress * for multiplication\npress / for division")

    o = input("Enter Operation: ")
    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The value is {a - b}")
        case "*":
            print(f"The result is {a * b}")
        case "/":
            print(f"The result is {a / b}")
        case default:
            print("There was an error")
    
except Exception as e:
    print("Enter a valid value") 