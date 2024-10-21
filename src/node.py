import json


class MessageNode:
    """Class representing each dialogue node and its attributes"""
    def from_manual(self, node_id: str, character_name: str, content: str,
                 goto: list, if_cond: str, signal: str):
        self.node_id = node_id
        self.character = character_name
        self.text = content
        self.goto = goto
        self.if_cond = if_cond
        self.signal = signal
        self.diceroll = 0
        self.parents = []

    def from_json(self, json_dict: str, node_id: str):
        self.from_manual("", "", "", [], "", "") # initializing everything just in case
        self.node_id = node_id
        self.__dict__ = json_dict[node_id]
        """
        self.character = json_dict[node_id]["character"]
        self.text = json_dict[node_id]["text"]
        self.goto = json_dict[node_id]["goto"]
        self.if_cond = json_dict[node_id]["if"]
        self.signal = json_dict[node_id]["signal"]
        self.diceroll = 0
        """

    def return_serial(self) -> str:
        serial_obj = {}
        serial_obj["character"] = self.character
        serial_obj["text"] = self.text
        serial_obj["if_cond"] = self.if_cond
        serial_obj["signal"] = self.signal
        serial_obj["diceroll"] = self.diceroll
        serial_obj["goto"] = self.goto

        return serial_obj