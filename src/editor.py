from textual.containers import Container
from textual.widgets import Label, Input


class Editor(Container):
    def compose(self):
        yield Label("Character")
        yield Input("name")
        yield Label("Text")
        yield Input("name")
        yield Label("If")
        yield Input("name")
        yield Label("Emit Signal")
        yield Input("name")
        yield Label("Goto")
        yield Input("name")

