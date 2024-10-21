from textual.widgets import Label, Input, Static, Select, SelectionList, Button
from textual.app import ComposeResult
from textual.containers import ScrollableContainer, Horizontal
from node import MessageNode


class NewNodeEditor(Static):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        if button_id == "add":
            self.action_add_goto_node()
        if button_id == "remove":
            self.action_remove_goto_node()
        if button_id == "save":
            self.action_save_node()
        if button_id == "cancel":
            self.action_cancel()

    def set_nodes(self, nodes):
        self.message_nodes = nodes

    def compose(self) -> ComposeResult:
        self.node_container = ScrollableContainer(id="new_GotoNodes")

        yield ScrollableContainer(
            Label("Node ID"),
            Input("", id="new_node_id_input", placeholder="Node ID"),
            Label("Character"),
            Input("", id="new_char_input", placeholder="Character Name"),
            Label("Dialogue"),
            Input("", id="new_text_input", placeholder="Dialogue"),
            Label("If"),
            Input("", id="new_if_input", placeholder="If Conditions"),
            Label("Emit Signal"),
            Input("", id="new_signal_input", placeholder="Emit Signals"),
            Label("Goto"),
            self.node_container,
            Horizontal(Button("Add Goto Node", id="add"), Button("Remove Goto Node", id="remove"), id="ButtonContainer"),
            Horizontal(Button("Save", id="save"), Button("Cancel", id="cancel"), id="new_confirm")
        )


    def action_add_goto_node(self) -> None:
        goto_selector = Select([(node_name, node_name) for node_name in self.message_nodes.keys()])
        self.node_container.mount(goto_selector)
        #self.mount()
        goto_selector.scroll_visible()

    def action_remove_goto_node(self) -> None:
        selectors = self.query("Select")
        if selectors:
            selectors.last().remove()

    def action_save_node(self) -> None:
        new_node = MessageNode()
        goto_nodes = [goto_node.value for goto_node in self.node_container.children if goto_node.value != Select.BLANK]
        new_node.from_manual(
            self.query_one("#new_node_id_input").value,
            self.query_one("#new_char_input").value,
            self.query_one("#new_text_input").value,
            goto_nodes,
            self.query_one("#new_if_input").value,
            self.query_one("#new_signal_input").value
        )

        self.app.message_nodes[self.query_one("#new_node_id_input").value] = new_node
        self.app.reconstruct_node_list()
        self.app.diatree.construct_tree()
        self.app.new_editor_exists = False
        self.remove()
    
    def action_cancel(self) -> None:
        if self.app.new_editor_exists:
            self.app.new_editor_exists = False
            self.remove()
