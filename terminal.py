import time
# Loops the program until the user quits
while True:
    # Asks the user which operation they want
    operation_type = input("Please enter your operation type:\n*add\n*subtract\n*multiply\n*divide\n: ")
    if operation_type not in ["add", "subtract", "multiply", "divide"]:
        print("invalid operation type")
        # Delays loop for readablity
        time.sleep(2)
        # Returns to start of the program
        continue
    # Asks the user for numbers to calculate
    number1 = float(input("number 1: "))
    number2 = float(input("number 2: "))
    if operation_type == "add":
        print(f"The result is {number1 + number2}")
    elif operation_type == "subtract":
        print(f"The result is {number1 - number2}")
    elif operation_type == "multiply":
        print(f"The result is {number1 * number2}")
    elif operation_type == "divide":
        if number2 == 0:
            print("Cannot divide by zero!")
        else:
            print(f"The result is {number1 / number2}")
    # Delays output for readablity
    time.sleep(2)
