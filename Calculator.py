#python calculator
while True:
    operator=input("Enter an operator ofyour choice(+ - * /): ")
    if operator not in ["+","-","*","/"]:
        print("The operator you've entered is invalid ,please a valid operator")
    try:
        num_1=float(input("Enter the first number:"))
        num_2=float(input("Enter the second digit: "))
        break
    except ValueError:
        print("Invalid input,pleae enter the correct input:")
    

def addition(num_1,num_2):
    return num_1+num_2
def sub(num_1,num_2):
    return num_1+num_2
def mult(num_1,num_2):
    return num_1*num_2
def div(num_1,num_2):
    return num_1/num_2

if operator=="+":
    print(addition(num_1,num_2))
elif operator=="-":
    print(sub(num_1,num_2))
elif operator=="*":
    print(mult(num_1,num_2))
elif operator=="/":
    print(div(num_1,num_2))
else:
    print("ERROR")