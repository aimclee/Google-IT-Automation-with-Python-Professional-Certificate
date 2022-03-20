import re

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))

# search는 조건에 맞는 값 중 첫번째의 값을 반환한다.
# findall을 활용하면 raw string의 조건의 모든 값을 반환한다.
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

'''
# 실행결과
<re.Match object; span=(7, 10), match='cat'>
<re.Match object; span=(7, 10), match='dog'>
<re.Match object; span=(12, 15), match='dog'>
['dog', 'cat']
'''