# - *- coding: utf- 8 - *-
from __future__ import unicode_literals

import errno
import os
import sys
import tempfile
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('a', None)
channel_access_token = os.getenv('b', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
int('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')


# function for create tmp dir for download content

def make_static_tmp_dir():
  try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text






    if text == 'songs':
     buttons_template = ButtonsTemplate(
      title='ชีวิตเธอดีอยู่แล้ว', text='Hello, my buttons', actions=[
        URIAction(label='listen', uri ='https://www.youtube.com/watch?v=rMrTHasf4uk'),
        ])

     template_message = TemplateSendMessage(
       alt_text='Buttons alt text', template=buttons_template)
     line_bot_api.reply_message(event.reply_token, template_message)

    elif text == 'เนื้อเพลง':
     if isinstance(event.source, SourceGroup):
        line_bot_api.reply_message(
         event.reply_token, [
         TextSendMessage(text='''ไม่รู้ทำไมต้องคิดทุกที ที่เธอเข้ามาทักทายทำให้รักทำให้หลง
         ทำให้ฉันไม่มั่นคง
แอบคิดไปไกล
เกินตัว
ก็รู้ทั้งรู้ว่าเธอมีใครหนึ่งคน
ให้แชร์หัวใจ
คนคนนั้นไม่ใช่ฉัน
ได้แค่ฝัน ได้แค่นั้นแค่คิดในใจ

รู้ดีถึงรักเธอหมดหัวใจ
ให้ตายก็เป็นไปไม่ได้
รู้ดีไม่มีทางแต่หัวใจ
ยังรักเธอยังคิดถึงเธออย่างนี้

บอกกับตัวเอง
ชีวิตเธอดีอยู่แล้ว
ไม่เคยต้องการเรา
เธอมีคนดูแลที่ดีกว่าฉัน
ไม่เคยเป็นคนสำคัญ
แค่เพียงในวันนั้น
อาจดูเหมือนเรารักกัน
แต่ฉันนั้นคิดไปเอง

ทุกทีที่คิดถึงเธอ
อาจทำให้ใจฉันลอย
อาจจะเผลออาจจะพลั้ง
ให้เธอคิดว่ามีหวัง
อาจฝันไปไกล

รู้ดีถึงรักเธอหมดหัวใจ
ให้ตายก็เป็นไปไม่ได้
รู้ดีไม่มีทางแต่หัวใจ
ยังรักเธอยังคิดถึงเธออย่างนี้
บอกกับตัวเอง
ชีวิตเธอดีอยู่แล้ว
ไม่เคยต้องการเรา
เธอมีคนดูแลที่ดีกว่าฉัน
ไม่เคยเป็นคนสำคัญ
แค่เพียงในวันนั้น
อาจดูเหมือนเรารักกัน
แต่ฉันนั้นคิดไปเอง

บอกกับตัวเอง
ชีวิตเธอดีอยู่แล้ว
ไม่เคยต้องการเรา
เธอมีคนดูแลที่ดีกว่าฉัน
ไม่เคยเป็นคนสำคัญ
แค่เพียงในวันนั้น
อาจดูเหมือนเรารักกัน
แต่ฉันนั้นคิดไปเอง

ชีวิตเธอดีอยู่แล้ว
ไม่เคยต้องการเรา
เธอมีคนดูแลที่ดีกว่าฉัน
ไม่เคยเป็นคนสำคัญ
แค่เพียงในวันนั้น
อาจดูเหมือนเรารักกัน
แต่ฉันนั้นคิดไปเอง

เราไม่เคยรักกัน
ฉันนั้นคิดไปเอง ''')
         ])
    



if __name__ == "__main__": arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
         )
arg_parser.add_argument('-p','--port', type=int, default=8000, help='port')
arg_parser.add_argument('-d', '--debug', default=False, help='debug')
options = arg_parser.parse_args()

    # create tmp dir for download content
make_static_tmp_dir()

app.run(debug=options.debug, port=options.port)






                                                              59,7  

