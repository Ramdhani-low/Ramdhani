from . import Operation
from . import Database
from . import util
def add_console():
  print("\n\n"+"="*25)
  print("silahkan tambahkan tugas")
  tugas = input("Tugas\t: ")
  jam = int(input("jam\t : "))
  menit = int(input("menit\t: "))
  Jam = f"{jam}:{menit}"
  status = "belum"
  data = Database.Template.copy()
  data["pk"] = util.string_random(6)
  data["tugas"] = tugas + Database.Template["tugas"][len(tugas):]
  data["Jam"] = Jam + Database.Template["Jam"][len(Jam):]
  data["status"] = status + Database.Template["status"][len(status):]
  data_str = f'{data["pk"]}, {data["tugas"]}, {data["Jam"]}, {data["status"]}'
  try:
    with open(Database.DB_name, "a", encoding="utf-8") as file:
      file.write(data_str+"\n")
  except:
    print("Failed...")
  print("ini hasil penambahan")
  read_console()
  
def read_console():
  data_file = Operation.reading()
  index = "no"
  tugas = "Tugas"
  Jam = "Jam"
  status = "Status"
  print("\n"+"="*50)
  print(f"{index:4} | {tugas:25} | {Jam:5} | {status:8}")
  print("\n"+"="*50)
  for index, data in enumerate(data_file):
    data_break = data.split(",")
    pk = data_break[0]
    tugas = data_break[1]
    Jam = data_break[2]
    status = data_break[3]
    print(f"{index+1:4} | {tugas:25} | {Jam:5} | {status:8}")
def update_console():
  read_console()
  while True:
    print("Silahkan Pilih apa yang mau di update")
    no_tugas = int(input("Nomor Tugas \t: "))
    data_tugas = Operation.reading(index=no_tugas)
    if data_tugas:
      break
    else:
      print("gagal!?")
  
  data_break = data_tugas.split(",")
  pk = data_break[0]
  tugas = data_break[1]
  Jam = data_break[2]
  status = data_break[3][:-1]
  while True:
    print("\n"+"="*25)
    print("silahkan, apa yang ingin kau ubah? Tugas? Waktu? atau menyelesaikan Tugas?")
    print(f"tugas \t: {tugas:25}")
    print(f"jam \t: {Jam:5}")
    print(f"status \t: {status:8}")
    user_option = input("pilih opsi [1,2,3] : ")
    match user_option:
      case "1": tugas = input("Tugas \t:")
      case "2":
        jam = int(input("jam \t: "))
        menit = int(input("menit \t : "))
        Jam = f"{jam}:{menit}"
      case "3":
        will = input(f" Yakin anda mau menyelesaikan {tugas:.25}? (y/n): ")
        if will == "y" or will == "Y":
          status = "Selesai"
          print(f"anda telah menyelesaikan tugas {tugas:.25}")
        else:
          pass
    print(f"tugas \t: {tugas:25}")
    print(f"jam \t: {Jam:5}")
    print(f"status \t: {status:8}")
    is_done = input("apakah update sesuai dengan yang anda inginkan? (y/n) ")
    if is_done == "y" or is_done == "Y":
      break
    else:
      continue
  Operation.Update(no_tugas, pk, tugas, Jam, status)

def delete_console():
  read_console()
  while True:
    print("Silahkan Pilih apa yang mau di hapus!")
    no_tugas = int(input("Nomor Tugas \t: "))
    data_tugas = Operation.reading(index=no_tugas)
    if data_tugas:
      data_break = data_tugas.split(",")
      pk = data_break[0]
      tugas = data_break[1]
      Jam = data_break[2]
      status = data_break[3][:-1]
      print("apakah anda yakin mau menghapus ini? \n")
      print("\n"+"="*25)
      print(f"tugas \t: {tugas:25}")
      print(f"jam \t: {Jam:5}")
      print(f"status \t: {status:8}")
      is_done = input("apakah update sesuai dengan yang anda inginkan? (y/n) ")
      if is_done == "y" or is_done == "Y":
        Operation.delete(no_tugas)
        break
      else:
        continue
    else:
      print("gagal!?")
  print("tugas berhasil dihapus")