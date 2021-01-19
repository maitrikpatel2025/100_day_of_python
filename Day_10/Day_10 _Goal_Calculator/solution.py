from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

End_calcutor = False

def calcution(num1, num2, ope):
    if ope == "+":
        return add(num1, num2)
    elif ope == "-":
        return sub(num1, num2)
    elif ope == "*":
        return multiply(num1, num2)
    elif ope == "/":
        return divide(num1, num2)
    else:
        return f"invaild input try again"

f_number = float(input("Enter First Number : "))
End_calcutor = False
while not End_calcutor:
    print("""+ : 'add'
    - : 'subtraction'
    * : 'multiply'
    / : 'divide """)
    choice = input("Pick a Operater : ")
    s_number = float(input("Enter second Number : "))
    calc_number = calcution(f_number, s_number, choice)
    should_continue = str(input(f"would you like to continue : {calc_number} 'y' and 'n' "))
    if should_continue == 'y':
        f_number = calc_number
    else:
        print(f"{f_number} {choice} {s_number} = {calc_number}")
        End_calcutor = True

print(logo)
