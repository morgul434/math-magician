# Math Magician Main File
  # usage: math operator operand1 operand2
def main():
      print("Welcome to Math Magician!")

def add(a, b):
     return a +b    


def main():
      import sys

      op = sys.argv[1]
      a = float(sys.argv[2])
      b = float(sys.argv[3]) 

      if op == "add":
        result = add(a, b);  

      print(f"Result: {result}")

if __name__ == "__main__":
      main()
