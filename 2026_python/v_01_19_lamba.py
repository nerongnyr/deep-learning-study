# 람다함수 양식(일회용 함수)
# 함수명 = lambda 매개변수: 반환값

# 기본 함수
# def add(a, b):
#     return a + b
# print(add(7, 10))

# 람다 함수
# add = lambda a, b: a + b
# print(add(10, 10))

import pyfiglet

# pyfiglet 기본 함수
def decoraate_text(text):
    return pyfiglet.figlet_format(text, font="slant")

# pyfiglet 람다 함수
decoraate_text = lambda text: pyfiglet.figlet_format(text)
print(decoraate_text("Hello"))

