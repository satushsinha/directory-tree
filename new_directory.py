from directory_tree import DirectoryTree

tree = DirectoryTree()

print("Id for Root Folder is: 0, Please use this to create subfolders")
while(True):
    operation = int(input("Press 1 to add folder\nPress 2 to remove folder\nPress 3 to get path\nPress 4 to rename folder\nPress 5 to Quit...\n"))
    if operation == 1:
        parent_id = int(input("Enter the  Id for the Parent Folder\n"))
        id = int(input("Enter the Id for the Folder\n"))
        name = input("Enter the name for the folder\n")
        tree.add_folder(parent_id, id, name)
    if operation == 2:
        id = int(input("Enter the Id for the Folder\n"))
        tree.remove_folder(id)
    if operation == 3:
        id = int(input("Enter the Id for the Folder\n"))
        path = tree.get_folder_path(id)
        if path:
            print(f"Path of Folder '{id}':", "/".join(path))
        else:
            print("Folder does not exist")
    if operation == 4:
        id = int(input("Enter the Id for the Folder\n"))
        name = input("Enter the name to be updated for the Folder\n")
        tree.update_folder_name(id, name)
    if operation == 5:
        break
