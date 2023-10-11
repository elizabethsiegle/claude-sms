from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

load_dotenv()

anthropic = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)
app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms():
    resp = MessagingResponse()
    inb_msg = request.form['Body'].lower().strip()
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT}{inb_msg}{AI_PROMPT}",
    )
    print(completion.completion)
    resp.message(completion.completion)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)