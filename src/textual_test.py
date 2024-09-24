from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Header, Footer, Placeholder, Tabs, Tree
from rich.text import Text


class Editor(App):
    """Editor w/ textual to manage writing nodes"""

    CSS_PATH = "textual_test.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self):
        super().__init__()
        self.current_focus = 0
        self.widget_ids = ["p1", "tabs"]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

        tree: Tree[dict] = Tree("Dialogue Nodes", id="p1")
        tree.root.expand()
        tree_nodes = tree.root.add("DIALOGUE_ONE")
        tree.root.add("DIALOGUE_TWO")
        tree_nodes.expand_all()
        tree_nodes.add_leaf("OPTION_ONE")
        tree_nodes.add_leaf("OPTION_TWO")
        tree_nodes.add_leaf("OPTION_THREE")
        yield Container(
            #Placeholder("tree area", id="p1"),
            tree,
            Placeholder("attributes and labels", id="p2"),
            Placeholder("p3 things", id="p3"),
            id="bot"
        )
        yield Tabs("New", "Edit", "Connect Nodes", id="tabs")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    
    def action_toggle_focus(self) -> None:
        """An action to toggle widget focus"""
        self.current_focus += 1
        if self.current_focus >= len(self.widget_ids):
            self.current_focus = 0
        
        self.query_one("#%s"%self.widget_ids[self.current_focus]).focus()


if __name__ == "__main__":
    app = Editor()
    app.run()