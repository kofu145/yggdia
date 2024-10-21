from textual.widgets import Tree


class DialogueTree(Tree):

    def set_nodes(self, nodes):
        self.message_nodes = nodes

    def get_node_parents(self, node_id):
        found_parents = []
        return self._get_parent_helper(node_id, found_parents)
    
    def _get_parent_helper(self, node_id, found_parents):
        for parent in self.message_nodes[node_id].parents:
            if parent not in self.message_nodes[node_id].goto: # failsafe for infinite loops
                found_parents.append(parent)
                self._get_parent_helper(parent, found_parents)
        return found_parents


    def construct_node(self, root_id, root_tree_node):
        for child_node in self.message_nodes[root_id].goto:
            new_rt = root_tree_node.add(child_node, expand=True, allow_expand=False)
            self.message_nodes[child_node].parents.append(root_id)
            self.construct_node(child_node, new_rt)

    def construct_tree(self):
        self.root.remove_children()
        for message_node in self.message_nodes.keys():
            self.message_nodes[message_node].parents = []

        self.root.expand()
        root_nodes = []

        for message_node in self.message_nodes.keys():
            found_parents = []
            for node_id in self.message_nodes.keys():
                if message_node in self.message_nodes[node_id].goto:
                    found_parents.append(node_id)
            if len(found_parents) == 0:
                root_nodes.append(message_node)
        
        for root_node in root_nodes:
            new_rt = self.root.add(root_node, expand=True, allow_expand=False)
            self.construct_node(root_node, new_rt)

    def on_mount(self):
        self.construct_tree()

                


