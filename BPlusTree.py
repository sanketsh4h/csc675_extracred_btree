class BPlusTree:
    class Node:
        def __init__(self, is_leaf=False):
            self.is_leaf = is_leaf
            self.keys = []
            self.children = []
        
        def __str__(self):
            if self.is_leaf:
                return f"Leaf: {self.keys}"
            return f"Node: {self.keys}"
    
    def __init__(self, order):
        self.root = self.Node(is_leaf=True)
        self.order = order

    def _find(self, node, key):
        for i, item in enumerate(node.keys):
            if key < item:
                return i
        return len(node.keys)

    def _insert_non_full(self, node, key, data):
        index = self._find(node, key)
        if node.is_leaf:
            node.keys.insert(index, (key, data))
            node.children.insert(index, None)
        else:
            child = node.children[index]
            if len(child.keys) == self.order:
                self._split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self._insert_non_full(node.children[index], key, data)
    
    def _split_child(self, parent, index):
        new_node = self.Node(is_leaf=parent.children[index].is_leaf)
        child = parent.children[index]
        mid_point = len(child.keys) // 2
        split_key = child.keys[mid_point]

        new_node.keys = child.keys[mid_point + 1:]
        new_node.children = child.children[mid_point + 1:]
        child.keys = child.keys[:mid_point]
        child.children = child.children[:mid_point + 1]

        parent.keys.insert(index, split_key)
        parent.children.insert(index + 1, new_node)

    def insert(self, key, data=None):
        root = self.root
        if len(root.keys) == self.order:
            new_root = self.Node()
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, data)

    def show(self):
        nodes = [self.root]
        while nodes:
            next_nodes = []
            line = " | ".join(str(node) for node in nodes)
            print(line)
            for node in nodes:
                if not node.is_leaf:
                    next_nodes.extend(node.children)
            nodes = next_nodes

tree = BPlusTree(3)  # A small order for easy testing and visualization

# Demonstration of operations
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.show()

tree.insert(40)
tree.show()
