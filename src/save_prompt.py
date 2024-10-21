from textual.widgets import Label, Input, Static, Select, SelectionList, Button, TextArea
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from node import MessageNode
import json

class SavePrompt(Static):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        if button_id == "save":
            self.action_save_file()
        if button_id == "cancel":
            self.action_cancel()


    def compose(self) -> ComposeResult:
        yield Container(
            Static("Are you sure you want to overwrite '%s'?"%self.app.json_file, classes="save_question"),
            Horizontal(Button("Yes", id="save", classes="save_button"), Button("No", id="cancel", classes="save_button"), id="save_buttons")  
        )      

    def action_save_file(self) -> None:
        serialize_dict = {}
        for key in self.app.message_nodes.keys():
            serialize_dict[key] = self.app.message_nodes[key].__dict__

        with open(self.app.json_file, "w") as f:
            json.dump(serialize_dict, f, indent=4)
        self.app.save_prompt_exists = False
        self.remove()

    def action_cancel(self) -> None:
        self.app.save_prompt_exists = False
        self.remove()