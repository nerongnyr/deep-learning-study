from transformers import pipeline

# 1 텍스트 생성 파이프라인 생성
generator = pipeline("text-generation", model="gpt2") # 최초 1회 모델 다운

# 2 시드 문장 입력 (이어 쓸 첫 부분)
q = input("이어서 쓸 첫 문장을 입력해주세요 : ")

# 3 텍스트 생성 실행
results = generator(
    q,
    max_new_tokens=50,       #추가 생성할 토큰 수
    num_return_sequences=1    # 반환 문장 1개로 설정
)

# 4 결과 출력
print(results[0]["generated_text"])

# The best way to build muscle at home is... Choose a workout plan that is conducive to your body's optimal function.
# 집에서 근육을 키우는 가장 좋은 방법은... 본인 몸의 최적화된 기능에 도움이 되는 운동 계획을 선택하는 것입니다.
# Some of these workouts may be as simple as a workout you can do while feeling good, like hiking, cycling, or
# 이러한 운동 중 일부는 하이킹, 자전거 타기 등 기분 좋게 할 수 있는 단순한 운동만큼이나 간단할 수 있습니다.

# When you're extremely sleepy, the brain produces more sugar, which is a problem.
# In reality, sugar is not a problem in the first place. 
# People with a sugar intolerance have a brain that's more adapted to the sugars in their diets, and a brain that's