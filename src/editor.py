from textual.widgets import Label, Input, Static, Select, SelectionList, Button, TextArea
from textual.app import ComposeResult
from textual.containers import ScrollableContainer, Horizontal
from node import MessageNode

class Editor(Static):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        if button_id == "add":
            self.action_add_goto_node()
        if button_id == "remove":
            self.action_remove_goto_node()
        if button_id == "save":
            self.action_save_current()

    def set_nodes(self, nodes):
        self.message_nodes = nodes

    def compose(self) -> ComposeResult:
        self.node_container = ScrollableContainer(id="GotoNodes")

        yield ScrollableContainer(
            Label("Character"),
            Input("", id="char_input", placeholder="Character Name"),
            Label("Dialogue"),
            TextArea("", id="text_input", show_line_numbers=True),
            Label("If"),
            Input("", id="if_input", placeholder="Flag Conditions"),
            Label("Emit Signal"),
            Input("", id="signal_input", placeholder="Signals to Emit"),
            Label("Goto"),
            self.node_container,
            Horizontal(Button("Add Goto Node", id="add"), Button("Remove Goto Node", id="remove"), id="ButtonContainer"),
            Button("Save Node", id="save")
        )

        self.current_node_id = None
        

    def action_add_goto_node(self) -> None:
        goto_selector = Select([(node_name, node_name) for node_name in self.message_nodes.keys() if (node_name != self.current_node_id and node_name not in self.app.diatree.get_node_parents(self.current_node_id))])
        self.node_container.mount(goto_selector)
        goto_selector.scroll_visible()

    def action_remove_goto_node(self) -> None:
        selectors = self.query("Select")
        if selectors:
            selectors.last().remove()

    def action_save_current(self) -> None:

        curr_node = self.app.message_nodes[self.current_node_id]
        curr_node.node_id = curr_node
        curr_node.character = self.query_one("#char_input").value
        curr_node.text = self.query_one("#text_input").text
        curr_node.goto = goto_nodes = [goto_node.value for goto_node in self.node_container.children if goto_node.value != Select.BLANK]
        curr_node.if_cond = self.query_one("#if_input").value
        curr_node.signal = self.query_one("#signal_input").value
        curr_node.diceroll = 0

        self.app.reconstruct_node_list()
        self.app.diatree.construct_tree()
    
