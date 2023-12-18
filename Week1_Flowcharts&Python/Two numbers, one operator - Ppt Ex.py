number1=float(input('Input first operand: '))
number2=float(input('Input second operand: '))
operator=input('Input operator(+,-,*,/): ')

if operator == "+":
    result = number1 + number2
if operator == "-":
    result = number1 - number2
if operator == "*":
    result = number1 * number2
if operator == "/":
    if number2 == 0:
        result = "Invalid operation"
    else:
        result = number1 / number2

print(result)