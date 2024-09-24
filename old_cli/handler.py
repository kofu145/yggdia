import json
from messagenode import MessageNode


class Handler:
    def __init__(self):
        self.nodes: list[MessageNode] = []
        self.definitions = {
            "help": self.help, 
            "new": self.new,
            "list": self.list_nodes
        }

    def help(self, function_name) -> None:
        helpstr = """
        Help:

        Commands:
            new             Create a new dialogue node
            edit NODE_ID    Edit an existing node by id
        """
        print(helpstr)

    def new(self) -> None:
        node_id = input("Enter id of node:")
        character = input("Enter character name (of speaker):")
        text = input("Dialogue:")
        goto = input("Enter node id(s) of connected nodes (press enter for none):")
        if_cond = input("Enter if cond for script check (enter for none):")
        emit_signal = input("Enter emit signal for script (enter for none):")
        self.nodes.append(MessageNode(node_id, character, text, goto,
                                      if_cond, emit_signal))

    def edit(self, node_id: str, attr: str):
        for node in self.nodes:
            if node.node_id == node_id:
                if attr in node.__dict__:
                    val = input("What to set attr %s?" %attr)
                    setattr(node, attr, val)
                else:
                    print("Attr does not exist!")

    def list_nodes(self):
        print(self.nodes)  # this should print as a tree soon
