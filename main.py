
    

from telegram import Update
from telegram.ext import *
import time
from deep_translator import GoogleTranslator
import ai21


async def response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    # Save the conversation to a text file
    with open('conversation.txt', 'a', encoding='utf-8') as file:
        file.write(f"Q: {user_input}\n")

    # Translate the message from Amharic to English
    translated = GoogleTranslator(source='am', target='en').translate(text=user_input)

    # Generate response using AI21 API
    response_mid = ai21.Completion.execute(
        model="j2-light",
        prompt=translated,
        numResults=1,
        maxTokens=10,
    )

    # Extract the generated completion text
    completion_text = response_mid["completions"][0]["data"]["text"]
    res = GoogleTranslator(source='en', target='am').translate(text=completion_text)
    time.sleep(3)

    # Save the response to the conversation file
    with open('conversation.txt', 'a', encoding='utf-8') as file:
        file.write(f"A: {res}\n")

    # Send the response back to the user
    await update.message.reply_text(res)


if __name__ == '__main__':
    ai21.api_key = "add your api key from free api giving big AI modules"

    app = Application.builder().token("use your own telegram api key in order to run the bot").build()

    app.add_handler(MessageHandler(None, response))

    print('Polling...')

    app.run_polling(poll_interval=5)

