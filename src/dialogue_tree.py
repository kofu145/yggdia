from textual.widgets import Tree


class DialogueTree(Tree):

    def on_mount(self):
        self.root.expand()
        init_dia = self.root.add("DIALOGUE_ONE", expand=True)
        init_dia.add_leaf("OPTION_ONE")
        init_dia.add_leaf("OPTION_TWO")
        init_dia.add_leaf("OPTION_THREE")
