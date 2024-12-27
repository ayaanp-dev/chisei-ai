from ..utils import create_chat_completion

def generate_multiple_choice_questions(material: str, num_questions: int) -> str:
    """
    Generate a specified number of multiple-choice questions based on the provided academic material.
    Each question will focus on key concepts, main ideas, and important details from the material.
    Provide 3-4 distinct answer choices for each question, with one correct answer and others as plausible distractors.

    Args:
        material (str): The academic material (notes, textbooks, study guides) based on which questions are generated.
        num_questions (int): The number of multiple-choice questions to generate.

    Returns:
        str: A list of generated multiple-choice questions and their options.
    """
    prompt = (
        f"You are an educational assistant tasked with generating {num_questions} multiple-choice questions based on the following academic material. "
        "For each question, focus on the key concepts, main ideas, and important details. "
        "Provide 3-4 distinct answer choices, one of which should be the correct answer, and the others should be plausible distractors. "
        "Ensure the correct answer is clear and unambiguous, and that the question is challenging yet fair.\n\n"
        f"Material:\n{material}"
    )

    # Request the model to generate the specified number of questions
    return create_chat_completion(
        messages=[{"role": "system", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

def generate_true_false_questions(material: str, num_questions: int) -> str:
    """
    Generate a specified number of True/False questions based on the provided academic material.
    Each question will focus on key concepts, main ideas, and important details from the material.
    The questions will be simple to understand and will have one True or False answer.

    Args:
        material (str): The academic material (notes, textbooks, study guides) based on which questions are generated.
        num_questions (int): The number of True/False questions to generate.

    Returns:
        str: A list of generated True/False questions and their answers.
    """
    prompt = (
        f"You are an educational assistant tasked with generating {num_questions} True/False questions based on the following academic material. "
        "For each question, focus on the key concepts, main ideas, and important details. "
        "Make sure each question is clear and concise, and provide the correct answer as either 'True' or 'False'. "
        "Ensure that the questions are fair and test important knowledge from the material.\n\n"
        f"Material:\n{material}"
    )

    # Request the model to generate the specified number of True/False questions
    return create_chat_completion(
        messages=[{"role": "system", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

def generate_essay_prompts(material: str, num_prompts: int) -> str:
    """
    Generate a specified number of essay-style prompts based on the provided academic material.
    These prompts are designed to encourage in-depth analysis, argumentation, or detailed discussion.
    
    Args:
        material (str): The academic material (notes, textbooks, study guides) based on which essay prompts are generated.
        num_prompts (int): The number of essay prompts to generate.

    Returns:
        str: A list of generated essay prompts.
    """
    prompt = (
        f"You are an educational assistant tasked with generating {num_prompts} essay prompts based on the following academic material. "
        "These prompts should encourage in-depth analysis, critical thinking, and well-supported arguments. "
        "Focus on testing the ability to synthesize information, evaluate ideas, and support arguments with evidence. "
        "Each prompt should require the student to demonstrate a deep understanding of the material and the ability to engage in thoughtful discussion.\n\n"
        f"Material:\n{material}"
    )

    # Request the model to generate the specified number of essay-style prompts
    return create_chat_completion(
        messages=[{"role": "system", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

def generate_short_answer_questions(material: str, num_questions: int) -> str:
    """
    Generate a specified number of short answer questions based on the provided academic material.
    These questions should focus on specific details, definitions, or key concepts and require concise responses.
    
    Args:
        material (str): The academic material (notes, textbooks, study guides) based on which short answer questions are generated.
        num_questions (int): The number of short answer questions to generate.

    Returns:
        str: A list of generated short answer questions.
    """
    prompt = (
        f"You are an educational assistant tasked with generating {num_questions} short answer questions based on the following academic material. "
        "The questions should focus on specific details, definitions, key concepts, or facts and should require concise and precise responses. "
        "Each question should be designed to test the student's understanding of important concepts or details from the material.\n\n"
        f"Material:\n{material}"
    )

    # Request the model to generate the specified number of short answer questions
    return create_chat_completion(
        messages=[{"role": "system", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )