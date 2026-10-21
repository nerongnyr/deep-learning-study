from transformers import pipeline

# 1 요약
summarizer = pipeline("summarization", model="eenzeenee/t5-base-korean-summarization")

# 2 요약할 원문 (영어 단락)
text = """인공지능과 머신러닝 기술의 급격한 발전은 현대 사회의 거의 모든 산업 분야에서 혁신적인 변화를 이끌어내고 있습니다. 
특히 최근 주목받고 있는 대규모 언어 모델(LLM)은 단순히 단순 노동이나 정해진 규칙에 따른 작업만을 수행하던 기존 컴퓨팅 시스템의 한계를 넘어, 
인간 고유의 영역으로 여겨졌던 자연어 이해, 문맥 파악, 그리고 창의적인 콘텐츠 생성 능력까지 갖추게 되었습니다. 
이러한 기술적 도약은 기업들의 업무 생산성을 비약적으로 향상시키고 새로운 비즈니스 기회를 창출하는 데 크게 기여하고 있지만, 
동시에 데이터 편향성 문제, 환각 현상(Hallucination), 개인정보 유출, 그리고 저작권 침해와 같은 복잡한 윤리적·법적 과제들을 수반하고 있습니다. 
따라서 향후 인공지능 기술의 지속 가능한 발전을 위해서는 기술적 성능 개선뿐만 아니라, 
안전하고 신뢰할 수 있는 인공지능 윤리 가이드라인 수립과 제도적 보완이 반드시 병행되어야 합니다."""

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