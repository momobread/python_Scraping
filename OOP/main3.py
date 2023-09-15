from typing import Any


class Dog:
    def __init__(self,name):
        self.name = name
        print(self.name)
        
    def __str__(self):
        print(super().__str__())
        return f"name : {self.name}"
    def __getattribute__(self,name):
        print(f"they want to get {name}")
        #이렇게 쓰면 {name}에 momo가 나와야 하는게 아닌가 싶지만
        # attribute 속성때문에 그대로 나온다
        #name이 속성 이름이 아니라 __init__메서드에서 self.name으로 설정한 인스턴트 변수의 이름이다. 
        #즉 self.name에 접근한것과 동일한 결과가 나온다
        return "😍"
        
        
        
sieun = Dog("sieun")
print(sieun)
momo = Dog("sieun")
print(momo)
print(momo.name)
