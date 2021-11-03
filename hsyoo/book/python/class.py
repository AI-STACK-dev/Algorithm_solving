class SoccerPlayer(object):
    def __init__(self, name : str, position : str, back_number : int):
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self):
        return "Hello My name is %s. My back number is %d" % \
            (self.name, self.back_number)
    
    def __add__(self, other):
        return self.name + other.name
    def change_back_number(self, new_number):
        print(f"change from {self.back_number} to {new_number}")
        self.back_number = new_number
a = SoccerPlayer("son", "FW", 7) # a는 객체, SoccerPlayer는 clas
park = SoccerPlayer("park", "WF", 13)
## 틀만 같고 서로 다른 객체이다!!!!


a.change_back_number(99)
print(a)
