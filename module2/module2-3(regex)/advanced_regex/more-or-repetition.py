# The long_words function returns all words that are at least 7 characters.
import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# \b matches word limits at the beginning and end of the pattern (정확히 5글자만)
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) # ['scary', 'ghost']

print(re.findall(r"\w{5,10}", "I really like strawberries")) # ['really', 'strawberri']
print(re.findall(r"\w{5,}", "I really like strawberries")) # ['really', 'strawberries']
print(re.search(r"s\w{,20}", "I really like starawberries")) # <re.Match object; span=(14, 27), match='starawberries'>

