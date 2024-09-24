from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Placeholder, Tabs, Tree


class yggeditor(App):
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
            # Placeholder("tree area", id="p1"),
            tree,
            Placeholder("editor", id="p2"),
            Placeholder("Log", id="p3"),
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
        self.query_one("#p3").label = self.widget_ids[self.current_focus]
        self.query_one("#{}".format(self.widget_ids[self.current_focus])).focus()

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        self.query_one("#p3").label = event.node.label
        self.query_one("#p3").refresh()
