from textual.widgets import Label, Input, Static, Select, SelectionList
from textual.app import ComposeResult


class Editor(Static):
    def compose(self) -> ComposeResult:
        yield Label("Character")
        yield Input("thing", id="char_input")
        yield Label("Text")
        yield Input("name", id="text_input")
        yield Label("If")
        yield Input("name", id="if_input")
        yield Label("Emit Signal")
        yield Input("name", id="signal_input")
        yield Label("Goto")
        yield Input("name", id="goto_input")

        yield SelectionList(*[("first", 1)])

    def action_add_goto_node(self) -> None:
        goto_selector = Select()
        self.query_one("#input").mount(goto_selector)
        goto_selector.scroll_visible()

    def action_remove_goto_node(self) -> None:
        """Called to remove a timer."""
        selectors = self.query("Select")
        if selectors:
            selectors.last().remove()
