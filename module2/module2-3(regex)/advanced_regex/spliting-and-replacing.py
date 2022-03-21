import re

print(re.split(r"the|a", "One sentence. Another one? And the last one!")) # ['One sentence. Ano', 'r one? And ', ' l', 'st one!']
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!")) # ['One sentence', ' Another one', ' And the last one', '']
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!")) # ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

# It's used for creating new strings by substituting all or part of them for a different string, 
# similar to the replace string method 
# but using regular expressions for both the matching and the replacing.
print(re.sub(
    r"[\w.%+-]+@[\w.-]+", 
    "[REDACTED]", "Received an email for go_nuts95@my.example.com") # Received an email for [REDACTED]
)

# 첫번째 인자값을 찾고 두번째 인자값에서  [\w .-]*가 \2, [\w .-]*가 \1에 매칭된다.
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")) # Ada Lovelace

