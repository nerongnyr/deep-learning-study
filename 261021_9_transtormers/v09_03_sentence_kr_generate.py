from transformers import pipeline

# 1 텍스트 생성 파이프라인 생성
generator = pipeline("text-generation", model="yanolja/YanoljaNEXT-EEVE-2.8B") 

# 2 시드 문장 입력 (이어 쓸 첫 부분)
q = input("이어서 쓸 첫 문장을 입력해주세요 : ")

# 3 텍스트 생성 실행
results = generator(
    q,
    max_new_tokens=130,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.7,         # 숫자가 낮을수록 무난하고 정돈된 문장이 나옴
    repetition_penalty=2.0
)

# 4 결과 출력
print(results[0]["generated_text"])

# 이어서 쓸 첫 문장을 입력해주세요 : 파이썬에서 가상환경을 구축하고 라이브러리를 관리하는 방법은
# 파이썬에서 가상환경을 구축하고 라이브러리를 관리하는 방법은 두 가지인데 하나는 pyenv를 사용해 쉽게 구현할 수 있지만, 
# 다른 한 가지는 virtualenvs라고 불리는 python-venv와 같은 프로그램을 사용해야 한다.
# pyvirtualize는 venvis로써 여러 번 설치해서 사용할 필요 없이 사용 방법을 간단하게 설명하고 있다(이것이 매우 효과적임을 증명하는 것이 아닐까). 
# 다만 그 이유는 이쪽의 github에 들어가보면 알겠지만 오픈소스이기 때문이다!
