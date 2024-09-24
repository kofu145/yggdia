import json


class MessageNode:
    """Class representing each dialogue node and its attributes"""
    def __init__(self, node_id: str, character_name: str, content: str,
                 goto: str, if_cond: str, emit_signal: str):
        self.node_id = node_id
        self.character = character_name
        self.text = content
        self.goto = goto
        self.if_cond = if_cond
        self.emit_signal = emit_signal

    def from_json(self, json_filename: str):
        self.__dict__ = json.load(json_filename)
