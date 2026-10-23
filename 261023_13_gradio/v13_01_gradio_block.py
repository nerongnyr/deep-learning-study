import gradio as gr
from ultralytics import YOLO
from deep_translator import MyMemoryTranslator

model = YOLO("yolo11n.pt")

# 1 지금까지 만든 함수 3개 정의
def say_hello(name):
    return "Hello", name

def trans_ko_to_en(text):
    en_text = MyMemoryTranslator(
            source="ko-KR", target=("en-US")
        ).translate(text)
    return en_text

def det_image(image):
    results = model(image)
    annnotated_image = results(00).plot
    return annnotated_image

with gr.Group() as gr_web:
    gr.Markdown("# 내가 만든 웹 서비스 모음")

    with gr.Tab("인사"):
        name_box = gr.Textbox(label=("이름"))
        hello_box = gr.Textbox(label=("인사함"))
        # click(실행할 함수, )
        gr.Textbox("인사하기").click(say_hello, name_box, hello_box)
    with gr.Tab("번역"):
        en_box = gr.Textbox(label="영어")
        ko_box = gr.Textbox(label="한국어")
        gr.Button("번역하기").click(trans_en_to_ko, en_box, ko_box)

    with gr.Tab("YOLO 탐지"):
        img_in = gr.Image(type="numpy", label="사진 올리기")
        img_out = gr.Image(label="탐지 결과")
        gr.Button("탐지하기").click(det_image, img_in, img_out)

gr_web.launch(share=True)