"""
작성자:나현호
작성일:19.12.03
설명
계좌 정보를 저장하는 Account클래스를 정의한다.
1)계좌번호, 계좌주이름, 잔액을 저장하는 __init__함수
2)input은 입금액을 잔액에 추가
3)withdrow는 출금액을 잔액에서 차감
4)print 는 현재 계좌정보 출력

installAcoount 클래스에서는
적금계좌정보를 저장한다. Account클래스를 계승한다
1)account class + 적금일을 저장하는 init함수
2)적금을 해약하는 close함수가 있다. 현재 잔액에 2%이율을 계산하여 반환한다

accountMain프로그램
계좌를 하나 만들어 100원을 입금한후 10원을 출금, 출력
적금계좌를 하나 만들어 10000원을 입금한 후 적금해약금을 출력
"""
class Account: #계좌를 개설, 시작금은 항상 0으로, 계좌주이름과 계좌번호를 받아서 생성한다.
    def __init__(self, num, name):
        self.num = num
        self.name = name
        self.charge = 0
    def input(self, income): #입금 시 charge에 추가
        self.charge += income
    def withdrow(self,outgoings):#출금 시 charge에서 차감
        self.charge -= outgoings
    def print(self):#print()메쏘드 시 계좌번호, 이름, 잔액을 반환
        print("계좌번호:" + str(self.num) + "\n이름:" + self.name + "\n잔액:" + str(self.charge))