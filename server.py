from flask import Flask, request, jsonify
from extract_text_from_pdf import extract_text_from_pdf
from question_answer import answer_questions
from slackPost import post_to_slack
import config

app = Flask(__name__)

# Prompt for PDF file path once
pdf_file_path = input("Enter the PDF file path: ")
pdf_text = extract_text_from_pdf(pdf_file_path)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Get the answer to the question
    answers = answer_questions(pdf_text, [question])

    # Post the answer to Slack
    results_json = jsonify(answers)
    success = post_to_slack(config.SLACK_CHANNEL, results_json.get_data(as_text=True), config.SLACK_BOT_TOKEN)
    
    if success:
        return jsonify({"message": "Results posted to Slack successfully!"})
    else:
        return jsonify({"error": "Failed to post results to Slack."}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
