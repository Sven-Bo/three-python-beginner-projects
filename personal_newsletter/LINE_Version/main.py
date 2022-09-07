import os
from pathlib import Path
from flask import Flask, request, abort
from dotenv import load_dotenv

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from src import utils

app = Flask(__name__)

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_ACCESS_SECRET"))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    message = event.message.text.lower()
    
    if  message == "btc":
        btc_rate = utils.get_btc_rate()
        response = f"The current BTC rate is {btc_rate} USD."        
        return line_bot_api.reply_message(event.reply_token,TextSendMessage(text=response))

    if message == "fact":
        useless_fact = utils.get_useless_fact()
        response = f"Did you know: {useless_fact}"        
        return line_bot_api.reply_message(event.reply_token,TextSendMessage(text=response))

    if message == "python": 
        return line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Executing your Python code..."))

    if  message.startswith("chuck"):
        joke = utils.get_chuck_norris_joke()
        return line_bot_api.reply_message(event.reply_token,TextSendMessage(text=joke))
    
    else:
        return line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Sorry, I do not understand that command 😕"))



if __name__ == "__main__":
    app.run()