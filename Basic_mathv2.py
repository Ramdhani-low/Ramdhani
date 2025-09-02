import os,sys,time
def ketik(text, delay=0.1):
  for huruf in text:
    print(huruf, end='', flush=True)
    time.sleep(delay)
  print()
def NumberChecking(a):
  try:
    float(a)
    return True
  except ValueError:
    ketik("sorry, the number not a valid", 0.1)
    return False
def Returned(Text6):
  ketik(Text6, 0.1)
  c = input().lower()
  if c == "y":
    return True
  else:
    return False
if __name__ == "__main__":
  while True:
    print("THE BASIC CALCULATOR")
    print("====================")
    print("OPERATION: +")
    print("OPERATION: -")
    print("OPERATION: /")
    print("OPERATION: x")
    print("====================")
    ketik("please, enter +,-,/ or x", 0.1)
    choice_o = input()
    ketik("enter a first number", 0.1)
    number_1 = input()
    number_1 = int(number_1)
    ketik("enter a second number", 0.1)
    number_2 = input()
    number_2 = int(number_2)
    if NumberChecking(number_1) and NumberChecking(2) != True:
      break
    match choice_o:
      case "+":
        results = number_1 + number_2
        ketik(f"{number_1} + {number_2} = {results}", 0.1)
        time.sleep(3)
        
      case "-":
        results = number_1 - number_2
        ketik(f"{number_1} - {number_2} = {results}", 0.1)
        time.sleep(3)
        
      case "/":
        results = number_1 / number_2
        results = float(results)
        results = round(results)
        ketik(f"{number_1} / {number_2} = {results}", 0.1)
        time.sleep(3)
        
      case "x":
        results = number_1 * number_2
        ketik(f"{number_1} x {number_2} = {results}", 0.1)
        time.sleep(3)
        
      case _:
        ketik("the Operation not a valid", 0.1)
        time.sleep(3)
    ketik("clear chat?(y/n)", 0.1)
    j = input().lower()
    match j:
      case "y":
        ketik("the chat getting clear.....", 0.1)
        time.sleep(3)
        operation = os.name
        match operation:
          case "posix": os.system("clear")
          case "nt": os.system("cls")
      case "n" : ketik("Ok", 0.1)
      case _ : ketik("ok", 0.1)
    Agains = Returned("Do you want continue? (y/n)")
    match Agains:
      case True: continue
      case False: break
      case _: break