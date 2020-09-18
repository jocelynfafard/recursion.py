# Author: Jocelyn Fafard jqf5530@psu.edu
# Collaborator: Stephanie Jen tzj5235@psu.edu
# Collaborator: Corey Freas cxf5302@psu.edu
# Collaborator: Christian Dell'Edera cmd6705@psu.edu
# Section: 011R
# Breakout: 4 

def sum_n(n): 
  if n <= 0:
    return 0
  else:
    return n + sum_n(n-1)

def print_n(s, n):
  if n <= 0:
    return 
  else:
    print(s)
    print_n(s, n-1)
  
def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  phrase = input("Enter a string: ")
  print_n(phrase,num)

if __name__ == "__main__":
  run()