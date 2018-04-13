# -*- coding: utf-8 -*-

class CmdBot(object):
    """docstring for ClassName"""
    def __init__(self, at_robot_string):
        super(CmdBot, self).__init__()
        self.at_robot_string = at_robot_string

    def get_response(self, text):
        ret = None
        text = text.strip()
        if text = self.at_robot_string + " 文件":
            ret = "http://192.168.10.220:8080/robot/"
        elif text = self.at_robot_string + " tapd":
            ret = "https://www.tapd.cn/my_worktable"
        elif text = self.at_robot_string + " ppt":
            ret = "http://192.168.10.220:8080/robot/转正申请表/"
        return ret
