import sys
import json
from dotenv import load_dotenv
from pdf_processor import extract_text_from_pdf
from question_answer import get_answers
from slack_client import post_to_slack

# Load environment variables from .env file
load_dotenv()

def main(pdf_path, questions, slack_channel):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Get answers using Langchain with OpenAI embeddings
    answers = get_answers(text, questions)
    
    # Post answers to Slack
    for question, answer in zip(questions, answers):
        if not answer:
            answer = "Data Not Available"
        post_to_slack(slack_channel, f"Q: {question}\nA: {answer}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <PDF_PATH> <QUESTIONS_JSON> <SLACK_CHANNEL>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    questions = json.loads(sys.argv[2])  # Use json.loads for safety
    slack_channel = sys.argv[3]
    
    main(pdf_path, questions, slack_channel)
