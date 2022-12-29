TEST_INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class TreeNode:
    def __init__(self, name: str, size: int = 0):
        self.name = name
        self.size = size
        self.parent = None
        self.children = []  # Deciding to go with a common structure for dirs and files

    def __str__(self):
        return f"Name: {self.name}\tSize: {self.size}"

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


class Tree:
    def __init__(self):
        self.root = TreeNode(name="/")
        self.current_node = self.root

    def cd(self, dest: str) -> None:
        if dest == "..":
            if self.current_node != self.root:
                self.current_node = self.current_node.parent
        elif dest == "/":
            self.current_node = self.root
        else:
            for child in self.current_node.children:
                if not child.size and dest == child.name:
                    self.current_node = child
                    return
            print(f"Directory {dest} not found")

    def insert_child(self, child: TreeNode) -> None:
        if self.current_node.size:
            # Not raising an exception because we want the program to continue
            print(f"This node is not a directory:\n{self.current_node}")
        elif child in self.current_node.children:
            print(f"Item already in directory:\n{child}")
        else:
            self.current_node.children.append(child)
            child.parent = self.current_node


def parse_input(input_string: str) -> Tree:
    fs_tree = Tree()
    for cmd in input_string.split("\n"):
        cmd = cmd.split()
        if not cmd:
            continue
        if cmd[0] == "$":
            if cmd[1] == "cd":
                fs_tree.cd(dest=cmd[-1])
        else:
            if cmd[0] == "dir":
                fs_tree.insert_child(child=TreeNode(name=cmd[1]))
            else:
                fs_tree.insert_child(child=TreeNode(name=cmd[1], size=int(cmd[0])))
    _load_node_sizes(node=fs_tree.root)
    fs_tree.current_node = fs_tree.root
    return fs_tree


def find_dir_total_size(tree: Tree) -> int:
    """
    Answers part 1
    """
    sizes = _get_dir_sizes(node=tree.root, sizes=list(), limit=100_000)
    return sum(sizes)


def delete_smallest_dir(tree: Tree) -> int:
    """
    Find smallest directory that will free up total space needed
    Answers part 2
    """
    total_drive_size = 70_000_000
    needed_free_space = 30_000_000
    current_free_space = total_drive_size - tree.root.size
    space_to_free_up = needed_free_space - current_free_space
    sizes = _get_dir_sizes(node=tree.root, sizes=list())
    return min([size for size in sizes if size >= space_to_free_up])


def _load_node_sizes(node: TreeNode):
    node_total_size = 0
    for child in node.children:
        if child.children:
            _load_node_sizes(node=child)
        node_total_size += child.size
    node.size = node_total_size


def _get_dir_sizes(node: TreeNode, sizes: list, limit: int = 0) -> list:
    for child in node.children:
        if child.children:
            if limit and child.size <= limit:
                sizes.append(child.size)
            elif not limit:
                sizes.append(child.size)
            _get_dir_sizes(node=child, sizes=sizes, limit=limit)
    return sizes


if __name__ == "__main__":
    tree = parse_input(TEST_INPUT)
    print(f"Total dir size for test input (part 1): {find_dir_total_size(tree=tree)}")
    print(f"Free up space (part 2): {delete_smallest_dir(tree=tree)}")
    with open("input.txt", "r") as f:
        input_string = f.read()
        tree = parse_input(input_string)
        print(
            f"Total dir size for test input (part 1): {find_dir_total_size(tree=tree)}"
        )
        print(f"Free up space (part 2): {delete_smallest_dir(tree=tree)}")
