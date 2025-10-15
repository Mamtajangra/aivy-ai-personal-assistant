# aivy-ai-personal-assistant

A command-line AI-powered personal assistant that can answer questions, provide weather updates, and deliver the latest news headlines using Gemini LLM and external APIs.

## Features

- **Weather Updates:** Get current weather information for any city.
- **News Headlines:** Fetch the latest news on a given topic.
- **Conversational AI:** Powered by Gemini LLM for natural language interaction.

## Setup

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd aivy-ai-personal-assistant# aivy-ai-personal-assistant

2. **Install dependencies**
       pip install -r requirements.txt  

3. **Configure environment variables**
    Create a .env file in the root directory with your API keys:   
    GOOGLE_API_KEY=your_google_api_key
    WEATHER_API_KEY=your_openweathermap_api_key
    NEWS_API_KEY=your_newsapi_key     


## Usage
   Run the assistant:
   python [main.py](http://_vscodecontentref_/0)

   
- Type your queries (e.g., "What's the weather in London?" or "Give me the      latest technology news"). Type exit or quit to stop.

## Project Structure

- main.py — Main entry point and chat loop.
- tools/weather_tool.py — Weather API integration.
 tools/news_tool.py — News API integration.
- .env — API keys (not tracked by git).
- README.md — Project documentation.


## Dependencies
- langchain
- langchain-google-genai
- python-dotenv
- requests

## License
 MIT License
 You can replace `<your-repo-url>` with your actual repository URL.
