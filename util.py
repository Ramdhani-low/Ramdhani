import string
import random

def string_random(panjang:int) -> str:
  string_r = "".join(random.choice(string.ascii_letters) for i in range(panjang))
  return string_r