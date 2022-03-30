
#!/usr/bin/env python3

import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)

  # number가 str(number)로 수정되어야 한다.
  # 수정하지 않으면 TypeError 발생. 아래는 에러 내용
  # print("hello " + name + ", your random number is " +number)
  # TypeError: can only concatenate str (not "int") to str)
  print("hello " + name + ", your random number is " + str(number))

greeting()
