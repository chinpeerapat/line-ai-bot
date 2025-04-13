from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
import asyncio
from dotenv import load_dotenv
import nest_asyncio
from openai import OpenAI
from bot_agents import create_runner, process_message

# Load environment variables
load_dotenv()

# Apply nest_asyncio for async compatibility
nest_asyncio.apply()

# Initialize Flask app
app = Flask(__name__)

# Initialize LINE API
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))

# Create OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# Create agent runner
runner = create_runner()

@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Get message from user
    user_message = event.message.text
    
    # Process message with agent runner
    try:
        response = asyncio.run(process_message(runner, user_message))
        
        # Send response back to user
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response)
        )
    except Exception as e:
        # Send error message if something goes wrong
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"Sorry, I encountered an error: {str(e)}")
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)