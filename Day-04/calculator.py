

num1 = 10
num2 = 2

addition = num1 + num2
print(addition)


def sum(num1,num2):
    add = num2 + num1
    return add

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
    # Handle division by zero
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

print("Sum:", sum(2, 4))
print("Multiplication:", multiply(3, 5))
print("Division:", divide(10, 2))
print("Division by zero test:", divide(10, 0))
