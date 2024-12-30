from ..utils import create_chat_completion

def answer_math(question: str):
    messages = [
        {"role": "system", "content": "Solve the given math problem step by step. The solution should include all necessary reasoning, and the final answer should be clearly boxed in \\boxed{}."},
        {"role": "user", "content": question}
    ]
    
    return create_chat_completion(messages, "llama-3.3-70b-versatile")

def prettify_math_answer(answer: str):
    """Prettify the math answer using the AI model."""
    messages = [
        {"role": "system", "content": "Prettify the given math answer, ensuring that it is neatly formatted, easy to read, and follows proper mathematical notation."},
        {"role": "user", "content": answer}
    ]
    
    return create_chat_completion(messages, "llama-3.3-70b-versatile")