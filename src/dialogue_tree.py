from textual.widgets import Tree


class DialogueTree(Tree):

    def set_nodes(self, nodes):
        self.message_nodes = nodes

    def get_node_parents(self, node_id):
        found_parents = []
        for parent_id in self.message_nodes.keys():
            if node_id in self.message_nodes[parent_id].goto:
                found_parents.append(parent_id)
        
        parents_exist = True
        while parents_exist:
            parents_exist = self._get_node_parent_helper(found_parents)

        return found_parents
        
    def _get_node_parent_helper(self, parents_arr):
        orig_size = len(parents_arr)
        for parent in parents_arr:
            for parent_id in self.message_nodes.keys():
                if parent in self.message_nodes[parent_id].goto:
                    parents_arr.append(parent)

        return len(parents_arr) > orig_size
        

    def construct_node(self, root_id, root_tree_node):
        for child_node in self.message_nodes[root_id].goto:
            new_rt = root_tree_node.add(child_node, expand=True, allow_expand=False)
            self.construct_node(child_node, new_rt)

    def construct_tree(self):
        self.root.remove_children()
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

                


