from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from ai.summarization.summarization import summarize
from ai.questions.math_answering import answer_math, prettify_math_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/summarize/")
def get_summary(text: str):
    print(summarize(text))
    return summarize(text)

@app.get("/math/answer/")
def get_math_answer(question: str):
    original = answer_math(question)
    return prettify_math_answer(original)