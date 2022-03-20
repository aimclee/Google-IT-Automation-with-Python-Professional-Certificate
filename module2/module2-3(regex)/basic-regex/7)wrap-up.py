import re

# $ sign을 추가함으로써 A로 시작해서 a로 끝나는 문자열만을 매칭시킬 수 있다.
# *는 바로 앞의 문자를 여러번 반복할 때 사용할 수 있다.

# If a caret (^) is at the beginning of the entire regular expression, it matches the beginning of a line.
# If a dollar sign ($) is at the end of the entire regular expression, it matches the end of a line.
# If an entire regular expression is enclosed by a caret and dollar sign (^like this$), it matches an entire line.

print(re.search(r'A.*a', "Argentina")) # <re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r'A.*a', "Azerbaijan")) # <re.Match object; span=(0, 9), match='Azerbaija'>
print(re.search(r'^A.*a$', "Azerbaijan")) # None
print(re.search(r'^A.*a$', "Australia")) # <re.Match object; span=(0, 9), match='Australia'>

pattern_for_checking_variable = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern_for_checking_variable, "_this_is_valid_var_name")) # <re.Match object; span=(0, 23), match='_this_is_valid_var_name'>
print(re.search(pattern_for_checking_variable, "this isn't valid var name")) # None
print(re.search(pattern_for_checking_variable, "2variable")) # None

# Fill in the code to check if the text passed looks like a standard sentence, 
# meaning that it starts with an uppercase letter, 
# followed by at least some lowercase letters or a space, and ends with a period, 
# question mark, or exclamation point.
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[\.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
