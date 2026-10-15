# 붕어빵 비유
#     클래스 : 붕어빵 틀(설계도)
#     생성자 : 붕어빵을 처음 만들 때 자동 실행되는 준비 단게(재료 넣기, 반죽 만들기 등)
#     속성 : 붕어빵의 맛, 크기, 색상(정보를 담는 변수)
#     메서드 : 붕어빵이 할 수 있는 일(먹기, 데우기 - 클래스 안의 함수)
#     객체 : 붕어빵 틀로 만든 진짜 붕어빵
    
# 클래스 정의
class BungEoBbang:
    # 생성자
    def __init__(self, name, color):
        # 속성 정의
        self.name = name
        self.color = color

    # 메서드 정의
    def info(self):
        print(f"안녕하세요. 저는{self.name}붕어빵이고, {self.color}색입니다.")

    # 객체 생성
first_bbang = BungEoBbang("달콤이", "푸른")

    # 객체 메서드 호출
first_bbang.info()