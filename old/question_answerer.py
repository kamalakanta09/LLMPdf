from langchain_community.pipeline import SequentialPipeline
from langchain_community.task import QuestionAnsweringTask
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

def get_answers(text, questions):
    openai_embeddings = OpenAIEmbeddings(api_key=os.getenv('OPENAI_API_KEY'))
    
    pipeline = SequentialPipeline(tasks=[
        QuestionAnsweringTask(model="gpt-3.5-turbo-0125", embeddings=openai_embeddings)
    ])
    
    answers = []
    for question in questions:
        result = pipeline.run(context=text, question=question)
        answer = result['answer']
        answers.append(answer)
    
    return answers
