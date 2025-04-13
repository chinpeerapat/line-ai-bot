from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Initialize LINE API
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))

def push_message(user_id, message):
    """
    Send a push message to a specific user
    
    Args:
        user_id (str): The LINE user ID to send the message to
        message (str): The message text to send
    """
    try:
        line_bot_api.push_message(
            user_id,
            TextSendMessage(text=message)
        )
        print(f"Successfully sent message to {user_id}")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python push_message.py USER_ID MESSAGE")
        sys.exit(1)
    
    user_id = sys.argv[1]
    message = sys.argv[2]
    
    push_message(user_id, message)