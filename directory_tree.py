from directory_node import DirectoryNode

class DirectoryTree:
    def __init__(self):
        self.root = DirectoryNode(0, "root")
        self.node_count = 1

    def add_folder(self, parent_id, id, name):
        parent_node = self._find_node_by_id(parent_id)
        if parent_node:
            new_folder = parent_node.add_folder(id, name)
            self.node_count += 1
            return new_folder is not None
        return False

    def remove_folder(self, id):
        parent_node = self._find_parent_of_node(id)
        if parent_node:
            parent_node.remove_folder(id)
            self.node_count -= 1
            return True
        return False

    def get_folder_path(self, id):
        return self.root.get_folder_path(id)

    def update_folder_name(self, id, new_name):
        return self.root.update_folder_name(id, new_name)

    def _find_node_by_id(self, id):
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.id == id:
                return node
            stack.extend(node.children)
        return None

    def _find_parent_of_node(self, id):
        stack = [(self.root, None)]
        while stack:
            node, parent = stack.pop()
            if node.id == id:
                return parent
            for child in node.children:
                stack.append((child, node))
        return None
