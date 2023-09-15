class Human:
    def __init__(self,name):
        print("human 생성자 OK")
        self.name =name    
    def say_hello(self):
        print(f"hello{self.name}")
    
class Player(Human):
    def __init__(self,name,xp):
        # self를 this라고 생각하면 되겠다
        # class 안에 있는 모든 메서드는 self를 
        # 가장 첫 번째 parameter로 한다
        super().__init__(name)
        self.xp = xp

class Fan(Human):
    def __init__(self,name,fav_team):
        #상속하려면 상속하는 클래스의 생성자를 써줘야 함
        #super를 쓰면 human에 접속할 수 있다
        #그렇게 해서 human의 __INITt__에 접근한다
        super().__init__(name)
        self.fav_team = fav_team        
    
    



sieun_player = Player("sieun",16);
sieun_player.say_hello
sieun_fan = Fan("sieun","ddd")
sieun_fan.say_hello



