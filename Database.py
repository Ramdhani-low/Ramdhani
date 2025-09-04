from . import Operation
import os
path = "/Project/mylib"

DB_name = "data_list.txt"
Template = {
  "pk" : "xxxxxx",
  "tugas" : 25*"",
  "Jam" : 5*"",
  "status" : 25*"",
}
def init_console():
  try:
    with open(DB_name, "r") as file:
      print("database tersedia")
  except:
    print("database belum tersedia, buat yg baru")
    Operation.create_new_task()
      