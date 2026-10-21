import streamlit as st
from ultralytics import YOLO
import cv2
import pandas as pd         # 엑셀 같은 데이터 타입으로 만드는 도구
import time                 # 시간 측정
import plotly.express as px # 그래프 그리는 도구

# 1 화면 구성
col1, col2 = st.columns(2)  # 같은 너비 두 칸 생성

with col1:
    frame_placeholder = st.empty()

with col2:
    chart_placeholder = st.empty()

# 2 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv066.stream/playlist.m3u8")

# 3 모델 로드
@st.cache_resource
def load_model():
    return YOLO("yolo11m.pt")

model = load_model()

# 4 프레임 처리
last_chart_time = 0
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 확인")
        st.warning("프레임 확인.")
        break
        
    # 4-1 모델 추론
    result = model(frame)

    # 4-2 탐지 결과 시각화 가져오기
    annotated_frame = result[0].plot()

    # 4-3 탐지된 객체 클래스 이름 추출
    labels = []
    for c in result[0].boxes.cls:
        labels.append(model.names[int(c)])

    # 4-4 차트 그리기
    if labels:  # 뭔가 탐지했다면
        # 객체 이름 키에 따옴표 추가
        df_count = pd.DataFrame({"Object": labels})
        # Count에 따옴표 추가
        df_count = df_count.value_counts().reset_index(name="Count")

        # 4-5 px 막대 그래프 (fig 변수에 저장)
        fig = px.line(
            df_count,   # 가로축: 객체 이름
            x="Object", # 세로축 : 개수
            y="Count",  # 그래프 이름
            title="탐지 객체 수",   # 점 위에 "count" 숫자로 표시
            text="Count",
            markers=True
        )
        fig.update_traces(textposition="top center")
    else:   # 탐지 안 되었을 때
        df_count = pd.DataFrame({"Object": [], "Count": []})
        fig = px.line(
            df_count,
            x="Object",
            y="Count",
            title="탐지 객체 수",
            markers=True
        )

    # 5 st에 결과 표시
    # OpenCV 이미지를 Streamlit에 맞게 BGR -> RGB 변환 후 출력
    frame_placeholder.image(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB), channels="RGB")
    # 그래프는 1초에 한 번만 갱신 (프레임마다 새로 그리면 브라우저가 렌더링을 끝내지 못함)
    if time.time() - last_chart_time >= 1:
        chart_placeholder.plotly_chart(fig, use_container_width=True, key=str(time.time()))
        last_chart_time = time.time()

# 6 자원 해제
cap.release()   
cv2.destroyAllWindows()