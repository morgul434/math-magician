
# Math Magician Main File
  # usage: math operator operand1 operand2
import sys
import os
  
def main():
    print("Welcome to Math Magician!")

def add(a, b):
    return a + b   

def sub(a, b): 
    return a - b

def multi(a, b):
    return a * b


def main():
    import sys

    print("Welcome to Math Magician!")

    op = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if op == "mul" or op == "*":
        result = multi(a, b)

    if op == "add" or op == "+":
        result = add(a, b); 

    if op == "sub" or op == "-":
        result = sub(a, b)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
