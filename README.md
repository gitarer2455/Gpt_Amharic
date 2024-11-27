# Telegram Translation and AI Response Bot

This is a **Telegram bot** that integrates **AI-based language generation** and **translation** capabilities. It receives messages in **Amharic**, translates them to **English**, sends the translated text to an AI model for generating a response, and then translates the response back to **Amharic** before sending it back to the user. Additionally, all conversations are saved to a text file for record-keeping.

## Key Features

- **Amharic to English Translation**: Translates user input from Amharic to English using Google Translate.
- **AI-Powered Responses**: Sends the translated English text to the AI21 model to generate relevant responses.
- **English to Amharic Translation**: Translates the AI-generated response back to Amharic for user interaction.
- **Conversation Logging**: Saves the conversation (both user input and AI response) to a text file for record-keeping.

## How It Works

1. **Receive Message**: The bot receives an input message from the user in **Amharic**.
2. **Translate to English**: The message is translated into **English** using Google Translate.
3. **Generate Response**: The translated text is sent to the **AI21 API** (a language generation model) to produce a meaningful response.
4. **Translate Back to Amharic**: The AI response is translated back into **Amharic** and sent to the user.
5. **Log Conversation**: Both the user's message and the AI's response are saved in a file named `conversation.txt`.

## Built With 💻

- **Python Telegram API**: To interact with Telegram users and send/receive messages.
- **deep_translator**: To perform translation between Amharic and English.
- **AI21 API**: To generate AI-powered responses based on the translated text.
- **time**: To implement delays between requests to ensure smooth execution.

## Prerequisites

Before running the bot, make sure to have the following:

- **Telegram Bot Token**: Create a Telegram bot and get your API key from [BotFather](https://core.telegram.org/bots#botfather).
- **AI21 API Key**: Sign up at [AI21](https://www.ai21.com/) and get a free API key.
- Install the necessary Python packages.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/telegram-ai-translator-bot.git
    cd telegram-ai-translator-bot
    ```

2. Install the required Python libraries:

    ```bash
    pip install python-telegram-bot deep-translator ai21
    ```

3. Replace the placeholders in the code with your actual API keys:

   - `ai21.api_key = "your_ai21_api_key"`
   - `app = Application.builder().token("your_telegram_bot_token").build()`

4. Run the bot:

    ```bash
    python main.py
    ```

The bot will now be running and responding to messages sent to it on Telegram!

## Conversation Log

All interactions (questions and AI responses) are logged in a file named `conversation.txt`. This file is saved in the same directory as the bot.

---

## Example Workflow

1. **User Message**: The user sends a message in **Amharic**.
2. **Translation**: The bot translates the message to **English**.
3. **AI Response**: The bot uses the AI21 model to generate a response based on the English translation.
4. **Back to Amharic**: The AI's response is translated back to **Amharic** and sent to the user.
5. **Logging**: The conversation is saved to `conversation.txt`.

---

### Key Modifications:
- **Structured Overview**: Clear and concise explanation of what the bot does.
- **Detailed Features**: A list of key functionalities describing the interaction flow.
- **How It Works**: A simple step-by-step explanation of the workflow.
- **Installation Instructions**: Provided a straightforward way to clone and run the bot.
- **Conversation Log**: Mentioned how the bot logs the conversation.

### Final Structure for `README.md`
This file can now be placed in your GitHub project repository to provide users with all the information they need to understand and run your bot. When they visit your repository, they'll see a well-documented project that's easy to understand and use.

Let me know if you need any adjustments!
