from transformers import pipeline

# 1 감정 분석 파이프라인 생성
classfier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")

# 2 분석할 문장 입력
# 2-1 긍정 문장
text = "오늘 기분이 정말 최고야!"
# 2-2 부정 문장
# text = "오늘은 정말 우울하고 안 좋은 날이야."
# 2-3 부정 단어
# text = "화남"

# 3 문장 분석                               
results = classfier(text)

# 4 결과 확인
print(f"문장 분석 결과 : {results[0]['label']}")
# 긍정, 부정
print(f"문장 분석 점수 : {results[0]['score']:.4f}")
# 1에 가까울수록 모델 확신도 높음

# 문장 분석 결과 : positive
# 문장 분석 점수 : 0.9195

# 문장 분석 결과 : negative
# 문장 분석 점수 : 0.9178

# 문장 분석 결과 : negative
# 문장 분석 점수 : 0.7929