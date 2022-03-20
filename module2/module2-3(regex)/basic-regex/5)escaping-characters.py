import re

# When we see a pattern that includes a backslash, 
# it could be escaping a special regex character or a special string character.

# escape character(\)는 문자 그 자체를 찾고자 할 때 활용된다.
print(re.search(r".com", "welcome")) # <re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com", "welcome")) # None
print(re.search(r"\.com", "mydomain.com")) # <re.Match object; span=(8, 12), match='.com'>

# \w matches letters, numbers, and underscores.
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))