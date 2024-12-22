from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from ai.summarization import TextSummarizer

app = FastAPI()

summarizer = TextSummarizer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/summarize/")
def get_summary(text: str):
    return summarizer.summarize(text)