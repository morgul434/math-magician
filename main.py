  # Math Magician Main File
  # usage: math operator operand1 operand2
from unittest import result


def sub(a, b): 
	return a - b


def main():
      print("Welcome to Math Magician!")


def main():
      import sys

      op = sys.argv[1]
      a = float(sys.argv[2])
      b = float(sys.argv[3])

      if op == "sub" or op == "-":
            result = sub(a, b)

      
      print(f"Result: {result}")

if __name__ == "__main__":
      main()
