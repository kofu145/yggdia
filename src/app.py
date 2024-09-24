from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer, Placeholder, Tabs, Tree, Label, Input
from dialogue_tree import DialogueTree
from content_view import ContentView
from editor import Editor

class Yggdia(App):
    """Editor w/ textual to manage writing nodes"""

    CSS_PATH = "app.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        self.header = Header()
        self.footer = Footer()
        self.diatree = DialogueTree("LABEL THING", id="dtree")
        self.content = ContentView(id="content")
        yield self.header
        yield Horizontal(Container(
            # Placeholder("tree area", id="p1"),
            self.diatree,
            id="ctree"
            ),
            Editor(id="input")
        )
        """yield Container(
            Placeholder("editor", id="editor"),
            self.content,
            id="input"
        )"""

        yield Tabs("New", "Edit", "Connect Nodes", "Save", id="tabs")
        yield self.footer

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
 
    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        self.content.update("{}".format(event.node.label))
