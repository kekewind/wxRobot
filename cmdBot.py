# -*- coding: utf-8 -*-

class CmdBot():
    """docstring for ClassName"""
    def __init__(self, at_robot_string):
        self.at_robot_string = at_robot_string

    def get_response(self, text):
        ret = None
        cmd = text.replace(self.at_robot_string, '')
        cmd = cmd.strip()
        if cmd == "文件":
            ret = "http://192.168.10.220:8080/robot/"
        elif cmd == "tapd":
            ret = "https://www.tapd.cn/my_worktable"
        elif cmd == "ppt":
            ret = "http://192.168.10.220:8080/robot/ppt模板/"
        return ret
