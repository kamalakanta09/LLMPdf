import openai
import config

openai.api_key = config.OPENAI_API_KEY

# Text to Chunk 
def chunk_text(text, max_tokens=1500):
    tokens = text.split()
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    return [" ".join(chunk) for chunk in chunks]

# Prompt create
def answer_questions(text, questions):
    chunks = chunk_text(text)
    answers = {}
    for question in questions:
        chunk_answers = []
        for chunk in chunks:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Answer this question based on the text: {question}"},
                    {"role": "user", "content": chunk}
                ]
            )
            answer = response['choices'][0]['message']['content'].strip()
            chunk_answers.append(answer)
        
        combined_answer = " ".join(chunk_answers).strip()
        
        # Checking if the combined answer is meaningful or empty
        if not combined_answer or "I'm not sure" in combined_answer or "I don't know" in combined_answer:
            answers[question] = "Data Not Available"
        else:
            answers[question] = combined_answer
            
    return answers
