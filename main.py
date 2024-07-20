import json
from extract_text_from_pdf import extract_text_from_pdf
from question_answer import answer_questions
from slackPost import post_to_slack
import config

def main():
    try:
        # Input PDF file path and questions
        pdf_file_path = input("Enter the PDF file path: ")
        questions = input("Enter questions (comma-separated): ").split(',')

        # Extract text from PDF
        text = extract_text_from_pdf(pdf_file_path)
        
        # Answer questions
        answers = answer_questions(text, questions)
        
        # Format results
        results_json = json.dumps(answers, indent=2)
        
        # Post results to Slack
        success = post_to_slack(config.SLACK_CHANNEL, results_json, config.SLACK_BOT_TOKEN)
        
        if success:
            print("Results posted to Slack successfully!")
        else:
            print("Failed to post results to Slack.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
