class DeliveryFood:
    def __init__(self, menu, price, delivery_time):
        self.menu = menu
        self.price = price
        self.delivery_time = delivery_time

    def confirm_order(self):
        print(f"{self.menu} 주문이 접수되었습니다! ({self.price}원 / 약 {self.delivery_time}분 소요)")

    def complete_delivery(self):
        print(f"{self.menu} 배달이 완료되었습니다. 맛있게 드세요!😊💕🤞")

food1 = DeliveryFood("마라탕", 18000, 36)
food2 = DeliveryFood("파스타", 13000, 28)

food1.confirm_order()
food1.complete_delivery()
print("-" * 57)
food2.confirm_order()
food2.complete_delivery()