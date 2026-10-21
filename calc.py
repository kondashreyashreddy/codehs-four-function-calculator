# Default Variable Settings
save1 = "No Number Present"
save2 = "No Number Present"
save3 = "No Number Present"
save4 = "No Number Present"
save5 = "No Number Present"
ole = 0
ore = 0
olge = 0
num1 = 0
num2 = 0
value = 0

"""
Precondition: Have all of the saves listed and printed out
Postcondition: Update once run again if there is an update in the variables
"""
def saves():
    global save1, save2, save3, save4, save5
    print(f'\nSave 1: {str(save1)}')
    print(f'Save 2: {str(save2)}')
    print(f'Save 3: {str(save3)}')
    print(f'Save 4: {str(save4)}')
    print(f'Save 5: {str(save5)}')

"""
Precondition: User choses "2. No" when being asked if they want to continue using the program
Postcondition: Prints the PROGRAM END text and ends the program.
"""
def end_program():
    print("-------------------------------------------------------")
    print("                    PROGRAM END
    print("-------------------------------------------------------")
    quit()

"""
Precondition: Program redirects for the user to chose which save file they would want to use.
Postcondition: The user choses a save file or manually enters a new number for either their first or second number.
"""
def complex_operations():
    global save1, save2, save3, save4, save5, num1, num2, ore, olge
    if ole == 1:
        saves()
        ui_1 = int(input("\nWhich Save Would You Like To Use?\n1. Save 1\n2. Save 2\n3. Save 3\n4. Save 4\n5. Save 5\n6. Return\nUser Input: "))
        if ui_1 == 1:
            if save1 ==  "No Number Present":
                save1 = 0
            num1 = save1
        elif ui_1 == 2:
            if save2 ==  "No Number Present":
                save2 = 0
            num1 = save2
        elif ui_1 == 3:
            if save3 ==  "No Number Present":
                save3 = 0
            num1 = save3
        elif ui_1 == 4:
            if save4 ==  "No Number Present":
                save4 = 0
            num1 = save4
        elif ui_1 == 5:
            if save5 ==  "No Number Present":
                save5 = 0
            num1 = save5
        else:
            num1 = int(input("\nEnter The First Number: "))
        ore = 1
    elif ole ==  2:
        saves()
        ui_2 = int(input("\nWhich Save Would You Like To Use?\n1. Save 1\n2. Save 2\n3. Save 3\n4. Save 4\n5. Save 5\n6. Return\nUser Input: "))
        if ui_2 == 1:
            if save1 ==  "No Number Present":
                save1 = 0
            num2 = save1
        elif ui_2 == 2:
            if save2 ==  "No Number Present":
                save2 = 0
            num2 = save2
        elif ui_2 == 3:
            if save3 ==  "No Number Present":
                save3 = 0
            num2 = save3
        elif ui_2 == 4:
            if save4 ==  "No Number Present":
                save4 = 0
            num2 = save4
        elif ui_2 == 5:
            if save5 ==  "No Number Present":
                save5 = 0
            num2 = save5
        else:
            num2 = int(input("\nEnter The Second Number: "))
        olge = 2

"""
Precondition: After finishing a calculation, the user choses to save the number
Postcondition: User choses which save file to keep their number in and the program saves it as a variable
"""
def save_num():
    global save1, save2, save3, save4, save5, value
    saves()
    edit = int(input("\nWhich Save Would You Like To Edit: "))
    if edit == 1:
        save1 = value
        print(f'\nThe Number {value} Saved In Save 1')
    elif edit == 2:
        save2 = value
        print(f'\nThe Number {value} Saved In Save 2')
    elif edit == 3:
        save3 = value
        print(f'\nThe Number {value} Saved In Save 3')
    elif edit == 4:
        save4 = value
        print(f'\nThe Number {value} Saved In Save 4')
    elif edit == 5:
        save5 = value
        print(f'\nThe Number {value} Saved In Save 5')
    else:
        print("\nInvalid Save. Number Has Not Been Saved.")

"""
Precondition: The user enters the values and operation of choice for their calculation
Postcondition: The code checks whether the values meet the restrictions for the program
"""
def operations():
    global value, num1, num2, operation
    if operation == 1:
        if num1 == "No Number Present" or num2 == "No Number Present":
            value = "No Number Present"
        else:
            value = num1 + num2
    elif operation == 2:
        if num1 == "No Number Present" or num2 == "No Number Present":
            value = "No Number Present"
        else:
            value = num1 - num2
    elif operation == 3:
        if num1 == "No Number Present" or num2 == "No Number Present":
            value = "No Number Present"
        else:
            value = num1 * num2
    elif operation == 4:
        if num2 == 0:
            value = "No Number Present"
        else:
            value = num1 / num2
    else:
        value = "No Number Present"
    print(f'\nResult Of Operation: {value}')
    save = int(input("\nWould You Like To Save This Number?\n1. Yes\n2. No\nUser Input: "))
    if save == 1:
        save_num()
    else:
        pass
    print("-------------------------------------------------------")

"""
Precondition: User starts the program
Postcondition: User has inputted the 2 numbers and operation form and have recieved their input
"""
def calculator_module():
    global num1, operation, num2, ole, ore, olge
    if ore == 1:
        ore = 0
    check_1 = int(input("\nWould You Like To Use A Saved Number For First Number?\n1. Yes\n2. No\nUser Input: "))
    if check_1 == 1:
        ole = 1
        complex_operations()
    else:
        num1 = int(input("\nEnter The First Number: "))
    operation = int(input("\nEnter The Operation Of Choice\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nUser Input: "))
    if olge == 2:
        olge = 0
    check2 = int(input("\nWould You Like To Use A Saved Number For Second Number?\n1. Yes\n2. No\nUser Input: "))
    if check2 == 1:
        ole = 2
        complex_operations()
    else:
        num2 = int(input("\nEnter The Second Number: "))
    operations()
    confirm = int(input("Would You Like To Continue?\n1. Yes\n2. No\nUser Input: "))
    if confirm == 1:
        calculator_module()
    else:
        end_program()
    
print("-------------------------------------------------------")
print("              Basic 4 Function Calulator")
start = int(input("Type Which Number You Chose\n1. Open Calculator\n2. Quit\nUser Input: "))

if start == 1:
    print("-------------------------------------------------------")
    calculator_module()
else:
    end_program()
