from transformers import pipeline

def summarize(text: str) -> str:
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="pt")
    return summarizer(text)[0]['summary_text']