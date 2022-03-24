class Dog:
  years = 0
  def dog_years(self):
    # 아래와 같이 docstring을 쓰면 help(Dog)를 인터프리터에 입력했을 때
    # help에 해당 내용이 나온다.
    '''returns age of dog compared to human being'''
    return self.years*7
    
fido=Dog()
fido.years=3
print(fido.dog_years())