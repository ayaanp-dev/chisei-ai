import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class TextSummarizer:
    def __init__(self, model_name="google/long-t5-tglobal-large"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)

    def preprocess(self, text: str) -> str:
        """
        Preprocess input text by removing unwanted elements and normalizing.
        """
        # Remove URLs
        text = re.sub(r'http\S+', '', text)

        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        # Split into sentences to ensure meaningful truncation
        sentences = re.split(r'(?<=[.!?])\s+', text)
        processed_text = " ".join(sentences)

        return processed_text

    def summarize(self, text: str, compression_ratio=0.3) -> str:
        """
        Generate a summary for the given text.
        """
        # Preprocess text
        preprocessed_text = self.preprocess(text)

        # Tokenize and truncate input as needed
        inputs = self.tokenizer(preprocessed_text, return_tensors="pt", max_length=16384, truncation=True).to(self.device)
        input_length = inputs["input_ids"].shape[1]

        # Set dynamic max_length for output
        max_length = max(50, min(1024, int(input_length * compression_ratio)))

        try:
            # Generate summary
            summary_ids = self.model.generate(
                inputs["input_ids"],
                max_length=max_length,
                min_length=max(30, int(max_length * 0.2)),
                length_penalty=2.0,
                num_beams=8,  # Higher beams for better quality
                no_repeat_ngram_size=3
            )
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        except Exception as e:
            summary = "An error occurred during summarization: " + str(e)

        return summary