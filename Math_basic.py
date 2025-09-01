import time,sys
print("\n=============")
print("    Calculator")
print("   (+) (-) (:) (×)")
print("=============")

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
    return False
def Returned(Text6):
  ketik(Text6, 0.1)
  c = input().lower()
  if c == "y":
    return True
  else:
    return False
Text = "Hello, Do you want to count? "
for huruf in Text:
  print(huruf, end="", flush=True)
  time.sleep(0.1)
choice1 = input("Y/n: ").lower()
if choice1 == "y":
  while True:
    ketik("Select the first number.", 0.1)
    number1 = input()
    NumberChecking(number1)
    ketik("Select the second number.", 0.1)
    number2 = input()
    NumberChecking(number2)
    ketik("choose between +,-,/,x")
    choice = input()
    
    if NumberChecking(number1) and NumberChecking(number2):
        number1 = int(number1)
        number2 = int(number2)
        if choice == "+":
          results = number1 + number2
          ketik(f"{number1} + {number2} = {results}", 0.1)
          time.sleep(2)
          cek = Returned("Do you want restart? (y/n) ")
          if cek == True:
            ketik("The program......restart!", 0.1)
            time.sleep(1)
            continue
          else:
            ketik("running...stop", 0.1)
            time.sleep(1)
            break
        elif choice == "-":
          results = number1 - number2
          ketik(f"{number1} - {number2} = {results}", 0.1)
          time.sleep(2)
          cek = Returned("Do you want restart? (y/n) ")
          if cek == True:
            ketik("The program......restart!", 0.1)
            time.sleep(1)
            continue
          else:
            ketik("running....stop", 0.1)
            time.sleep(1)
            break
        elif choice == "/":
          results = number1 / number2
          results = round(results)
          ketik(f"{number1} / {number2} = {results}", 0.1)
          time.sleep(2)
          cek = Returned("Do you want restart? (y/n) ")
          if cek == True:
            ketik("The program......restart!", 0.1)
            time.sleep(1)
            continue
          else:
            ketik("running...stop", 0.1)
            time.sleep(1)
            break
        elif choice == "x":
          results = number1 * number2
          results = float(results)
          ketik(f"{number1} x {number2} = {results}", 0.1)
          time.sleep(2)
          cek = Returned("Do you want restart? (y/n) ")
          if cek == True:
            ketik("The program......restart!", 0.1)
            time.sleep(1)
            continue
          else:
            ketik("running....stop", 0.1)
            time.sleep(1)
            break
        else:
          ketik("please, enter a valid \n operation", 0.1)
          time.sleep(2)
          cek = Returned("Do you want restart? (y/n) ")
          if Returned == True:
            ketik("The program......restart!", 0.1)
            time.sleep(1)
            continue
          else:
            ketik("running...stop", 0.1)
            time.sleep(1)
            break
          
    else:
      ketik("sorry, this is not number", 0.1)
      time.sleep(2)
      Returned("Do you want restart? (y/n) ")
      if Returned == True:
        ketik("The program......restart!", 0.1)
        time.sleep(1)
        continue
      else:
        ketik("Running...stop", 0.1)
        time.sleep(1)
        break
else:
  T = "Okay, by-by"
  for i in T:
    print(i, end="", flush=True)
    time.sleep(0.1)
    break
  

