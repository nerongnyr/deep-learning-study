from transformers import pipeline

# 1 요약
summarizer = pipeline("summarization", model="t5-small")

# 2 요약할 원문 (영어 단락)
text = """A special 25th anniversary edition of the extraordinary
international bestseller... Santiago's journey teaches us about
the essential wisdom of listening to our hearts..."""

# 3 요약 실행
summary = summarizer(
    text,
    min_length=20,  # 최소 토큰 수
    max_length=100, # 최대 토큰 수
    do_sample=False # 매번 동일 결과 값 출력
)

# 4 결과 확인
sum_txt = summary[0]["summary_text"]
print(f"요약된 문장 : {sum_txt}")

"""요약된 문장 : 25th anniversary edition of the extraordinary international bestseller . 
Santiago's journey teaches us about the essential wisdom of listening to our hearts ."""