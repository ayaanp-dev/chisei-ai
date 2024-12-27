from ..utils import create_chat_completion

# Define a function to summarize text specifically for notes and textbooks
def summarize(text: str) -> str:
    # Refined and academic-focused prompt for the model
    prompt = (
    "You are a helpful assistant specializing in summarizing academic material, such as notes and textbooks. "
    "Your goal is to extract and present the main ideas, key concepts, and crucial details in a concise, clear, and organized manner. "
    "Omit any unnecessary or irrelevant information, and focus on the most important takeaways. "
    "If appropriate, use bullet points or numbered lists to highlight key points. "
    "Ensure the summary is understandable and accessible for a general audience, avoiding overly technical language unless necessary.\n\n"
    f"Text:\n{text}"
    )

    return create_chat_completion(
        messages=[{"role": "system", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )