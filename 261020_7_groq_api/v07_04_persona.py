from dotenv import load_dotenv
import os
from groq import Groq

# 1 환경 변수 불러오기
load_dotenv()

# 2 API 입력
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3 대화 기록 맨 앞에 AI 성격 및 규칙 지정
messages =[
    {
        "role": "system",
        "content": "너는 아주 엄격한 CTO 개발자야. 답변을 짧게 해"
    }
]

# 4 질문 입력
while True:
    # 4-1 질문
    q = input("나 : ")
    # 4-2 종료 입력
    if q == "exit":
        print("exit 를 눌러서 종료.")
        break
        
    # 4-3 내 질문을 기록에 추가
    messages.append(
        {
            "role" : "user",
            "content" : q
        }
    )
    # 4-4 질문 보내기
    res = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages= messages,
        temperature=0.1,    # 낮을수록 일관된 답
        max_completion_tokens=300,  # 답변 최대 길이 (오타 수정)
        reasoning_effort="low"
    )

    # 4-5 답변 받기!
    answer = res.choices[0].message.content
    print(f"AI의 답변 : {answer}")

    # 4-6 AI 답변도 기록에 추가
    messages.append(
        {
            "role": "assistant",
            "content" : answer
        }
    )