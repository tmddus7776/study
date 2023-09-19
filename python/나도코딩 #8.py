#_8) 클래스
name = "마린" #마린
hp = 40
damage = 5
print("{}유닛이 생성되었습니다.".format(name))
print("체력 {}, 공격력 {}\n".format(hp, damage))

tank_name = "탱크" #탱크
tank_hp = 150
tank_damage = 35

tank2_name = "탱크" #탱크2
tank2_hp = 150
tank2_damage = 35

print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력:{2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)


class Unit:
    def __init__(self, name, hp, damage):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력: {}, 공격력: {}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #class 외부에 변수 추가 할당 -> 변수 확장 : 확장한 변수에 대해서만 실행 가능

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#_8) 메소드
class AttackUnit:
    def __init__(self, name, hp, damage):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        self.name = name #self.name:생성한 인자, name:전달받은 인자
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{} : {}방향으로 적군을 공격합니다. [공격력{}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

#_8) 상속
class Unit:
    def __init__(self, name, hp):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} : {}방향으로 적군을 공격합니다. [공격력{}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

#_8) 다중 상속
class Unit:
    def __init__(self, name, hp):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} : {}방향으로 적군을 공격합니다. [공격력{}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


#_8)메소드 오버라이딩
class Unit:
    def __init__(self, name, hp, speed):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 : {}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {}방향으로 적군을 공격합니다. [공격력{}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)
vulture.move("11시")

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.move("9시")

#_8)pass
class Unit:
    def __init__(self, name, hp, speed):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 : {}]"\
            .format(self.name, location, self.speed))


class BuildingUnit(Unit):
    def __init__(Self, name, hp, location):
        pass  #아무것도 하지 않고 일단 넘어간다. pass를 쓰면 아무것도 안적어도 오류가 안남

supply_depot = BuildingUnit("서플라잇 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over() #아무것도 실행하지 않음


#_8) Super
class Unit:
    def __init__(self, name, hp, speed):  #init는 파이썬 생성자임. 객체가 만들어질때 자동으로 호출됨
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 : {}]"\
            .format(self.name, location, self.speed))


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) #super는 self가 필요 없음
        self.location = location

'''
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

#class FlyableUnit(Unit, Flyable): #다중상속에서 super는 앞에온 인산자만 계산해서 산출함
 #   def __init__(self):
  #      super().__init__()

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()
'''

#_8) 스타크레프트 전반전
#일반유닛
class Unit:
    def __init__(self, name, hp, damage):  
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력: {}, 공격력: {}\n".format(self.hp, self.damage))

    def move(self, location):
        print("{} : {} 방향으로 이동합니다."\
            .format(self.name, location))  
    def damaged(self, damage):
        print("{} : {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))
#공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, damage)
        self.speed = speed

    def move(self, location):
        print("{} : {} 방향으로 이동합니다. [속도 {}]"\
            .format(self.name, location, self.speed))  

    def attack(self, location):
        print("{} : {}방향으로 적군을 공격합니다. [공격력{}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

#마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
#스팀팩: 일정시간동안 이동 및 공격 속도가 증가. 체력10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

#탱크 클래스
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜 더 높은 파워로 공격 가능, 이동불가
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False


    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        #시즈모드가 아닐 때 -> 시즈모드로 전환
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #시즈모드가 일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#공중유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format(name, location, self.flying_speed))
#공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

#레이스 클래스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드(해제상태)

    def clocking(self):
        if self.clocking == True: #클로킹 모드 -> 모드 해제
            print("{} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocking == False
        else: #클로킹 모드 해제 -> 모드 설정
            print("{} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocking == True

def game_start():
    print("\n---------[알림] 새로운 게임을 시작합니다.----------")

def game_over():
    print("player : gg")
    print("[player] 님이 게임에서 퇴장하였습니다.\n")


#실제게임 시작
game_start()
#마린생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
#탱크생성
t1 = Tank()
t2 = Tank()
t3 = Tank()
#레이스 생성
w1 = Wraith()
#유닛 일괄 관리 (생성된 모든 유닛 append)->리스트에 저장
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(t3)
attack_units.append(w1)

#전군이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈보드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격모드 준비 (마린: 스팀팩, 탱크 : 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): #유닛이 마린인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank): #유닛이 탱크인지 확인
        unit.set_seize_mode()
    elif isinstance(unit, Wraith): #유닛이 레이스인지 확인
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
from random import *
for unit in attack_units:
    unit.damaged(randint(5, 21)) #공격은 랜덤으로 5-20까지 받음

#게임종료
game_over()














