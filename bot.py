# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

class Bot(object):
    """docstring for Bot"""
    def __init__(self):
        super(Bot, self).__init__()
        self.chatbot = ChatBot("wxRobot")
        self.chatbot.set_trainer(ListTrainer)

    def Train(self):
        self.chatbot.train('chatbot.corpus.chinese')
        self.chatbot.train('chatbot.corpus.english')
        self.chatbot.train([
        "你好",
        "你好，我是WeShare开发的智能机器人。很高兴为你服务。",
        "提前批针对哪些岗位的招聘？",
        "提前批面向2018年应届毕业生，开放软件开发、技术运营、安全技术、软件测试、技术研究等技术类岗位，以及游戏策划、游戏运营岗位。",
        "什么时候面试？以什么样的形式面试？",
        "简历通过筛选就会被发起面试，将会在7月27日-9月8日安排电话面试或视频面试，部分同学会被邀请至北上广深的办公大厦进行现场面试，我们将报销来回路费和住宿费用，请同学们保持手机畅通，并留意短信和邮件通知。考虑到筛选简历的时间，建议投递简历的时间为7月27日-8月25日。",
        "意向事业群的选择有什么用处？",
        "提前批中，你所选择的意向事业群会优先看到你的简历。而在正式校招中，意向事业群只作为参考，并不会完全按照意愿分配。如果你有强烈想加入某一个事业群的意愿，提前批是唯一可以主动选择事业群的机会。如果你的简历没有通过意向事业群的筛选，一样有机会被其他事业群发起面试。建议在面试时询问面试官所在的事业群，以免发生不必要的误会。",
        "如果提前批失败了会影响之后的正式校招么？",
        "如果提前批面试失败，或是未被发起面试，都会自动转为参加正式校招的对应岗位，也可以修改应聘岗位。正式校招不受影响。 需要说明的是，提前批未通过的面试记录将会留在系统中，供后续面试官参考。",
        "其他岗位什么时候开始招聘？",
        "其他岗位将在8月初全面开放投递，涵盖产品、市场、设计、职能等众多岗位，大家可以持续关注“腾讯招聘”微信公众号，将在第一时间推送。也可关注校招官网join.qq.com的更新。",
        "好的",
        "不客气",
        "谢谢",
        "拜~~~"
        ])

    def get_response(self, text):
        return self.chatbot.get_response(text).text