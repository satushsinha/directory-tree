class DirectoryNode:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.children = []

    def add_folder(self, id, name):
        new_folder = DirectoryNode(id, name)
        self.children.append(new_folder)
        return new_folder

    def remove_folder(self, id):
        for child in self.children:
            if child.id == id:
                self.children.remove(child)
                return True
        return False

    def get_folder_path(self, id):
        if self.id == id:
            return [self.name]
        for child in self.children:
            folder_path = child.get_folder_path(id)
            if folder_path:
                return [self.name] + folder_path
        return None

    def update_folder_name(self, id, new_name):
        if self.id == id:
            self.name = new_name
            return True
        for child in self.children:
            if child.update_folder_name(id, new_name):
                return True
        return False
