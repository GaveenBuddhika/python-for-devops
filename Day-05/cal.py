
import sys


def sum(num1,num2):
    add = num2 + num1
    return add


num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])


if operation == "sum":
   output = sum(num1,num2)
   print(output)