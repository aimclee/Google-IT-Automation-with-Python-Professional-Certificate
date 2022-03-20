import re
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-z|A-Z|0-9]", "cloudy"))
print(re.search(r"cloud[a-z|A-Z|0-9]", "cloud9"))

# search는 조건에 맞는 값 중 첫번째의 값을 반환한다.
# 띄어쓰기가 space를 의미하므로 아래 두개의 값은 다르게 나온다.
print(re.search(r"[^a-z|A-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-z|A-Z ]", "This is a sentence with spaces."))

'''
# 실행결과
<re.Match object; span=(18, 22), match='hway'>
None
<re.Match object; span=(0, 6), match='cloudy'>
<re.Match object; span=(0, 6), match='cloud9'>
<re.Match object; span=(4, 5), match=' '>
<re.Match object; span=(30, 31), match='.'>
'''
