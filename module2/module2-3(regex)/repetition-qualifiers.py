import re

# *는 가능한한 많은 문자를 취한다.
print(re.search(r"Py.*n", "Pygmalion")) # <re.Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r"Py.*n", "Python Programming")) # <re.Match object; span=(0, 17), match='Python Programmin'>

# raw string에 정의된 값이 문자열에 부합하는지 확인하려면 아래와 같이 쓴다.
print(re.search(r"Py[a-z]*n", "Python Programming")) # <re.Match object; span=(0, 6), match='Python'>
print(re.search(r"Py[a-z]*n", "Pyn")) # <re.Match object; span=(0, 3), match='Pyn'>

# The plus character matches one or more occurrences of the character that comes before it.
print(re.search(r"o+l+", 'goldfish')) # <re.Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", 'woolly')) # <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+", 'boil')) # None


# The question mark means either zero or one occurrence of the character before it.
# 물음표 앞의 글자는 optional하다.
print(re.search(r"p?each", "To each their own")) # <re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "I like peaches")) # <re.Match object; span=(7, 12), match='peach'>

# Question
# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. 
# For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False.
import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
