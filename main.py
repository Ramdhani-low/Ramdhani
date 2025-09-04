import os
import Crud as Crud

if __name__ == "__main__":
  while True:
    operation = os.name
    match operation:
      case "posix": os.system("clear")
      case "nt": os.system("cls")
    Crud.init_console()
    print("=========================")
    print("      TO DO LIST         ")
    print("1. Read Task")
    print("2. Add Task")
    print("3. Completed Task")
    print("4. Remove Task")
    print("5. Close")
    choce = input("Opsi: ")
    match choce:
      case "1": Crud.read_console()
      case "2": Crud.add_console()
      case "3": Crud.update_console()
      case "4": Crud.delete_console()
      case "4": break
    lanjut = input(" Selesai atau belum?(Y/n) ")
    if lanjut == "y" or lanjut == "Y":
      break
   
 
   
  
   