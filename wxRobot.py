# -*- coding: utf-8 -*-
import itchat
from itchat.content import *

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)
    # return chatbot.get_response(msg['Content']).text

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg)
    # return chatbot.get_response(msg['Content']).text

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print(msg)
    return "download_files"
    # msg.download(msg.fileName)
    # typeSymbol = {
    #     PICTURE: 'img',
    #     VIDEO: 'vid', }.get(msg.type, 'fil')
    # return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    return  "Hello"

    # msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))

itchat.auto_login(enableCmdQR=False, hotReload=True)
itchat.run()