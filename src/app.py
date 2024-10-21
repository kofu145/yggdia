from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer, Placeholder, Tabs, Tree, Label, Select
from dialogue_tree import DialogueTree
from content_view import ContentView
from editor import Editor
from new_node_editor import NewNodeEditor
from node import MessageNode
from save_prompt import SavePrompt
import json

class Yggdia(App):
    """Editor w/ textual to manage writing nodes"""

    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("tab", "save_values", ""),
        ("n", "new_node", "New Dialogue Node"),
        ("ctrl+s", "save_dialogue", "Save dialogue tree")
        ]

    def __init__(self, json_file: str):
        super().__init__()
        self.new_editor_exists = False
        self.save_prompt_exists = False

        self.json_file = json_file
        with open(json_file, "r") as f:
            self.json_content = json.load(f)
        
        self.message_nodes = {}
        for key in self.json_content.keys():
            new_node = MessageNode()
            new_node.from_json(self.json_content, key)
            self.message_nodes[key] = new_node

    def reconstruct_node_list(self):
        self.editor.set_nodes(self.message_nodes)
        self.diatree.set_nodes(self.message_nodes)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        self.header = Header()
        self.footer = Footer()
        self.diatree = DialogueTree("%s"%self.json_file, id="dtree")
        self.diatree.set_nodes(self.message_nodes)
        #self.content = ContentView(id="content")
        self.editor = Editor(id="input")
        self.editor.set_nodes(self.message_nodes)

        yield self.header
        yield Horizontal(Container(
            # Placeholder("tree area", id="p1"),
            self.diatree,
            id="ctree"
            ),
            self.editor,
            id="main"
        )
        """yield Container(
            Placeholder("editor", id="editor"),
            self.content,
            id="input"
        )"""

        yield self.footer

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_save_values(self) -> None:
        self.query_one("#char_input").value = "BABOOMBA"

    def action_new_node(self) -> None:
        if not self.new_editor_exists:
            new_editor = NewNodeEditor(id="new")
            new_editor.set_nodes(self.message_nodes)
            self.mount(new_editor)
            self.new_editor_exists = True

    def action_cancel_new(self) -> None:
        if self.new_editor_exists:
            new_editor = self.query_one("#new")
            new_editor.remove()
            self.new_editor_exists = False

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        # self.content.update("{}".format(event.node.label))
        node_id = str(event.node._label)
        self.editor.styles.visibility = "hidden" if node_id not in self.message_nodes else "visible"

        if self.editor.styles.visibility == "visible":
            self.query_one("#input").border_title = node_id
            self.editor.current_node_id = node_id
            self.query_one("#char_input").value = self.message_nodes[node_id].character
            self.query_one("#text_input").text = self.message_nodes[node_id].text
            self.query_one("#if_input").value = self.message_nodes[node_id].if_cond
            self.query_one("#signal_input").value = self.message_nodes[node_id].signal


            selectors = self.query("Select")
            for selector in selectors:
                selector.remove()

            for goto_node in self.message_nodes[node_id].goto:
                goto_selector = Select([(node_name, node_name) for node_name in self.message_nodes.keys() if node_name != node_id], allow_blank=False, value=goto_node)

                self.editor.node_container.mount(goto_selector)

    
    def action_save_dialogue(self):
        if not self.save_prompt_exists:
            self.mount(SavePrompt(id="save_prompt"))
            self.save_prompt_exists = True