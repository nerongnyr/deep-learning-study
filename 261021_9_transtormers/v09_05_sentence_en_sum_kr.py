from deep_translator import GoogleTranslator
from transformers import pipeline

# 1. 요약 파이프라인
summarizer = pipeline("summarization", model="t5-small")

text = """A special 25th anniversary edition of the extraordinary
international bestseller... Santiago's journey teaches us about
the essential wisdom of listening to our hearts..."""

summary = summarizer(text, min_length=20, max_length=100, do_sample=False)
sum_txt = summary[0]["summary_text"]
print(f"요약된 문장 (영어): {sum_txt}")

# 2. NLLB 번역 파이프라인 생성
translator = pipeline(
    "translation", 
    model="facebook/nllb-200-distilled-600M"
)

# 3. 실행할 때 src_lang과 tgt_lang을 파라미터로 전달
ko_summary = translator(
    sum_txt, 
    src_lang="eng_Latn", 
    tgt_lang="kor_Hang"
)

print(f"요약된 문장 (한국어): {ko_summary[0]['translation_text']}")