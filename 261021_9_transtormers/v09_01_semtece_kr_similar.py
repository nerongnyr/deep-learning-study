from sentence_transformers import SentenceTransformer, util

# 1 모델 로드
model = SentenceTransformer("jhgan/ko-sroberta-multitask")
# 모델 설명 :
    # 한국어 문장을 의미 공간에 벡터화
    # 한국어 문맥 이해도가 높음

# 2 비교할 두 문장 정의
sen1 = "고양이가 소파 위에서 자고 있어요"
sen2 = "내일 학교에서 수학 시험이 있어"
# 2-2 의미상 비슷한 두 문장 예시 => 높은 유사도 기대
# sen1 = "그는 도서관에서 책을 읽고 있다"
# sen2 = "그는 도서관에 가서 독서를 하고 있는 중이다"
# 2-3 비슷한 단어
# sen1 = "개"
# sen2 = "강아지"

# 3 문장 -> 숫자 좌표로 바꾸기(인코딩)
emb1 = model.encode(sen1, convert_to_tensor=True)
emb2 = model.encode(sen2, convert_to_tensor=True)

# 4 두 문장 유사도 측정 (코사인 유사도)
cos_sim = util.pytorch_cos_sim(emb1, emb2)

# 5 결과 출력
print(f"두 문장의 유사도{cos_sim.item():.4f}")