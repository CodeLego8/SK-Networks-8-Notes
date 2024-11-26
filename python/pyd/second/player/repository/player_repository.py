from abc import ABC, abstractmethod

#ABC는 ABstract Class 라는 뜻을 가지고 있음
#즉 DiceRepository(ABC)는 '추상화 클래스'라는 뜻을 가짐
#인터페이스란 용어가 와닿지 않을테니
#lol의 r(궁극기)라고 생각하면 됨
#<<<<<<<<<<여기서부터>>>>>>>>>>>>>
#R키는 상징적으로 궁극기라고 생각하게 됨
#그러나 실제 캐릭터들은 제각각 다른 궁극기들을 펼치게 됩니다.
#<<<<<<<<<<<<<<<<여기까지 인터페이스라 생각하면 됨>>>>>>>>>>>>>>>>>>
class playerRepository(ABC):
    @abstractmethod
    def rollplayer(self):
        pass