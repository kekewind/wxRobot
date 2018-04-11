# -*- coding: utf-8 -*-
import itchat
from itchat.content import *
import pymongo
from util import *
from bot import *
import time

class App(object):
    """全局唯一进程实例"""
    def __init__(self):
        super(App, self).__init__()
        self.itchat = itchat
        self.wx_robot_conn = pymongo.MongoClient(host='127.0.0.1',port=27017)

        #所有的单独对话,比如 filehelper(文件助手),公众号,单个好友
        @self.itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isFriendChat = True)
        def FriendChat(msg):
            self.wx_robot_conn.db[DB_NAME].insert(msg)
            self.itchat.send(self.get_response(msg['Content']), msg['FromUserName'])

        @self.itchat.msg_register(FRIENDS, isFriendChat = True)
        def addFriendChat(msg):
            self.itchat.send(self.get_response(msg['Content']), msg['FromUserName'])

        @self.itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat = True)
        def download_person_files(msg):
            print(msg)
            if msg['FromUserName'] != self.at_robot_string:
                user = self.itchat.search_friends(userName = msg['FromUserName'])
                FileName = msg['FileName']
                if not os.path.exists(FILE_STORAGE_ROOT):
                    os.mkdir(FILE_STORAGE_ROOT)
                path = os.path.join(FILE_STORAGE_ROOT, user['PYQuanPin'])
                if not os.path.exists(path):
                    os.mkdir(path)
                localtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
                path = os.path.join(path, localtime)
                if not os.path.exists(path):
                    os.mkdir(path)
                file_path = os.path.join(path, FileName)
                download_fun = msg['Text']
                with open(file_path, 'wb') as f:
                    f.write(download_fun())

        @self.itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat = True)
        def download_group_files(msg):
            print(msg)
            if msg['ToUserName'] != self.at_robot_string:
                user = self.itchat.search_chatrooms(userName = msg['ToUserName'])
                print(user)
                FileName = msg['FileName']
                if not os.path.exists(FILE_STORAGE_ROOT):
                    os.mkdir(FILE_STORAGE_ROOT)
                path = os.path.join(FILE_STORAGE_ROOT, user['NickName'])
                if not os.path.exists(path):
                    os.mkdir(path)
                localtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
                path = os.path.join(path, localtime)
                if not os.path.exists(path):
                    os.mkdir(path)
                file_path = os.path.join(path, FileName)
                download_fun = msg['Text']
                with open(file_path, 'wb') as f:
                    f.write(download_fun())

        #群聊天
        @self.itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat = True)
        def GroupChat(msg):
            self.wx_robot_conn.db[DB_NAME].insert(msg)
            if self.at_robot_string in msg['Content']:
                if "@@" in msg['FromUserName']:
                    self.itchat.send(self.get_response(msg['Content']), msg['FromUserName'])
                elif "@@" in msg['ToUserName']:
                    self.itchat.send(self.get_response(msg['Content']), msg['ToUserName'])

        #
        @self.itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isMpChat = True)
        def MpChat(msg):
            self.wx_robot_conn.db[DB_NAME].insert(msg)

    def get_response(self, text):
        return self.bot.get_response(text)

    def run(self):
        try:
            self.bot = Bot()
            self.bot.Train()
            if os.name == 'nt':
                self.itchat.auto_login(enableCmdQR=False, hotReload=True)
            else:
                self.itchat.auto_login(enableCmdQR=True, hotReload=True)
            self.at_robot_string = '@' + self.itchat.search_friends()['PYQuanPin']
            self.itchat.run()
        except Exception as e:
            self.itchat.logout()

if __name__ == '__main__':
    app = App()
    app.run()