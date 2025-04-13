# LINE AI Multi-Agent Bot

This is a LINE messaging bot that uses OpenAI's models to provide responses to user queries. The bot uses a multi-agent system to handle different types of queries:

1. **Triage Agent**: Determines which specialized agent should handle the query
2. **Response Agent**: Provides general responses
3. **Web Search Agent**: Handles web search queries
4. **File Search Agent**: Searches in vector databases for document-based queries

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- LINE Developer Account
- OpenAI API key
- Ngrok or similar for local development (or a deployed server)

### Installation

1. Clone this repository:
```
git clone https://github.com/chinpeerapat/line-ai-bot.git
cd line-ai-bot
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy the `.env.example` file to `.env`
   - Fill in the required environment variables:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `LINE_CHANNEL_ACCESS_TOKEN`: Your LINE Channel Access Token
     - `LINE_CHANNEL_SECRET`: Your LINE Channel Secret
     - `VECTOR_STORE_ID`: Your vector store ID for document search

### Setting up LINE Messaging API

1. Create a LINE Developer account at [developers.line.biz](https://developers.line.biz/)
2. Create a new provider and channel (Messaging API)
3. Get your Channel Access Token and Channel Secret
4. Set the webhook URL to your server's URL + "/callback" (e.g., https://your-server.com/callback)

### Running the Bot

1. Start the Flask server:
```
python app.py
```

2. If testing locally, use Ngrok to expose your local server:
```
ngrok http 8000
```

3. Set the webhook URL in your LINE Channel settings to the Ngrok URL + "/callback"

4. Test your bot by sending a message to it on LINE

## Usage

- Send any text message to the bot
- The bot will determine which agent should handle the query and respond accordingly
- For web searches, include words like "search" or "find" in your query
- For file searches, include words like "file" or "document" in your query

## Customization

- Modify the agent instructions in `bot_agents.py` to customize the bot's behavior
- Add additional agents or tools as needed
- Adjust the triage logic to better route user queries

## License

[MIT License](LICENSE)