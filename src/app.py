from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer, Placeholder, Tabs, Tree, Label
from dialogue_tree import DialogueTree
from content_view import ContentView
from editor import Editor


class Yggdia(App):
    """Editor w/ textual to manage writing nodes"""

    CSS_PATH = "app.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("tab", "save_values", ""),
        ("n", "new_node", "New Dialogue Node")
        ]

    def __init__(self, json_file: str):
        super().__init__()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        self.header = Header()
        self.footer = Footer()
        self.diatree = DialogueTree("LABEL THING", id="dtree")
        self.content = ContentView(id="content")
        editor = Editor(id="input")

        yield self.header
        yield Horizontal(Container(
            # Placeholder("tree area", id="p1"),
            self.diatree,
            id="ctree"
            ),
            editor,
            id="main"
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

    def action_save_values(self) -> None:
        self.query_one("#char_input").value = "BABOOMBA"

    def action_new_node(self) -> None:
        self.mount(Editor(id="new"))

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        # self.content.update("{}".format(event.node.label))
        self.query_one("#input").border_title = str(event.node._label)
        self.query_one("#char_input").value = str(event.node._label)

    def action_remove_stopwatch(self) -> None:
        """Called to remove a timer."""
        timers = self.query("Stopwatch")
        if timers:
            timers.last().remove()
