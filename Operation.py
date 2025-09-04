from . import Database
from . import util
import os

def Update(no_tugas,pk, tugas, Jam, status):
  data = Database.Template.copy()
  data["pk"] = pk
  data["tugas"] = tugas + Database.Template["tugas"][len(tugas):]
  data["Jam"] = Jam + Database.Template["Jam"][len(Jam):]
  data["status"] = status + Database.Template["status"][len(status):]
  data_str = f'{data["pk"]}, {data["tugas"]}, {data["Jam"]}, {data["status"]}'
  data_length = len(data_str)
  try:
    with open(Database.DB_name, "r") as file:
      r_data = file.readlines()
      r_data[no_tugas-1] = data_str
    with open(Database.DB_name, "w", encoding="utf-8") as file:
      file.writelines(r_data)
  except:
    print("error...")

def create_new_task():
  tugas = input("Tugas : ")
  jam = input("jam : ")
  menit = input("menit : ")
  
  Jam = f"{jam}:{menit}"
  status = "belum"
  data = Database.Template.copy()
  data["pk"] = util.string_random(6)
  data["tugas"] = tugas + Database.Template["tugas"][len(tugas):]
  data["Jam"] = Jam + Database.Template["Jam"][len(Jam):]
  data["status"] = status + Database.Template["status"][len(status):]
  data_str = f'{data["pk"]}, {data["tugas"]}, {data["Jam"]}, {data["status"]}'
  try:
    with open(Database.DB_name, "w", encoding="utf-8") as file:
      file.write(data_str+"\n")
  except:
    print("Failed...")
def reading(**kywarg):
  try:
    with open(Database.DB_name, "r") as file:
      content = file.readlines()
      
      jumlah_tugas = len(content)
      if "index" in kywarg:
        index_tugas = kywarg["index"]-1
        if index_tugas < 0 or index_tugas > jumlah_tugas:
          return False
        else:
          return content[index_tugas]
      else:
        return content
  except:
    return False
def delete(no_tugas):
  try:
    with open(Database.DB_name, "r") as file:
      counter = 0
      while True:
        content = file.readline()
        if len(content) == 0:
          break
        elif counter == no_tugas-1:
          pass
        else:
          with open("data_tempt.txt", 'a', encoding="utf-8") as tempt_file:
            tempt_file.write(content)
        counter += 1
  except:
    print("database gagal!")
  os.rename("data_tempt.txt", Database.DB_name)
 