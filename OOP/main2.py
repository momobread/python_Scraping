class Dog:
    def woof(self):
        print("woofwof")
        
class Beagle(Dog):
    # def jump(self):
    #     print("jump")
    def woof(self):
        super().woof()
        # super은 init이 없어도 사용할 수 있다
        print("super woof")
    
    
        
#main.py와 비교하다 싶이, 항상 클래스 안에 __init__을 할 필요는 없다
#위의 경우는 메서드만 정의하고 있다

beagle = Beagle()
beagle.woof()