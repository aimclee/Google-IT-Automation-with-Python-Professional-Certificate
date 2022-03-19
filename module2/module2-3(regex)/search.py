# r은 raw string을 의미, .은 각 알파벳 사이에 올 수 있는 하나의 무작위의 string이다.
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True