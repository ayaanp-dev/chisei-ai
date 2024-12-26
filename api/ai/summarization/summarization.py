import torch
from transformers import AutoTokenizer, LongT5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("google/long-t5-tglobal-base")
model = LongT5ForConditionalGeneration.from_pretrained("google/long-t5-tglobal-base").to("cuda")

def summarize_long_text(text, model, tokenizer, chunk_size=16384):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []
    
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", max_length=chunk_size, truncation=True)
        inputs = {key: value.to("cuda") for key, value in inputs.items()}
        summary_ids = model.generate(inputs["input_ids"], max_length=1500, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)
    
    combined_summary = " ".join(summaries)
    final_summary = summarize_long_text(combined_summary, model, tokenizer)
    
    return final_summary

def summarize(text: str):
    if len(text) > 16384:
        return summarize_long_text(text, model, tokenizer)
    else:
        inputs = tokenizer(text, return_tensors="pt", max_length=16384, truncation=True)
        inputs = {key: value.to("cuda") for key, value in inputs.items()}
        summary_ids = model.generate(inputs["input_ids"], max_length=1500, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary