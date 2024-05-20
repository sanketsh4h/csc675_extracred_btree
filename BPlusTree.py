class BPlusTree:
    class Node:
        def __init__(self, is_leaf=False):
            self.is_leaf = is_leaf
            self.keys = []
            self.children = []

        def __str__(self):
            return f"{'Leaf' if self.is_leaf else 'Node'}: {self.keys}"

    def __init__(self, order):
        self.root = self.Node(is_leaf=True)
        self.order = order
        self.min_keys = (order - 1) // 2

    def _find(self, node, key):
        for i, item in enumerate(node.keys):
            if key < item:
                return i
        return len(node.keys)

    def _insert_non_full(self, node, key, data=None):
        index = self._find(node, key)
        if node.is_leaf:
            node.keys.insert(index, key)
            print(f"Inserted key {key} in leaf: {node.keys}")
        else:
            child = node.children[index]
            if len(child.keys) == self.order - 1:
                self._split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self._insert_non_full(node.children[index], key, data)

    def _split_child(self, parent, index):
        child = parent.children[index]
        new_node = self.Node(is_leaf=child.is_leaf)
        mid_index = len(child.keys) // 2
        split_key = child.keys[mid_index]

        new_node.keys = child.keys[mid_index + 1:]
        child.keys = child.keys[:mid_index]
        if not child.is_leaf:
            new_node.children = child.children[mid_index + 1:]
            child.children = child.children[:mid_index + 1]

        parent.keys.insert(index, split_key)
        parent.children.insert(index + 1, new_node)
        print(f"Split child node at key {split_key}: left {child.keys}, right {new_node.keys}")

    def _split_root(self):
        old_root = self.root
        new_root = self.Node()
        new_root.children.append(old_root)
        self._split_child(new_root, 0)
        self.root = new_root
        print(f"Split root: new root keys {self.root.keys}")

    def insert(self, key, data=None):
        if len(self.root.keys) == self.order - 1:
            self._split_root()
        self._insert_non_full(self.root, key, data)
        self.show()  # Display tree after each insertion for debugging

    def _merge_nodes(self, parent, index):
        left = parent.children[index]
        right = parent.children[index + 1]
        left.keys.append(parent.keys.pop(index))
        left.keys.extend(right.keys)
        left.children.extend(right.children)
        parent.children.pop(index + 1)
        if not parent.keys and parent == self.root:
            self.root = left
        print(f"Merged nodes at index {index}: {left.keys}")

    def _borrow_from_sibling(self, node, index, left_sibling, right_sibling, parent):
        if left_sibling and len(left_sibling.keys) > self.min_keys:
            node.keys.insert(0, parent.keys[index - 1])
            parent.keys[index - 1] = left_sibling.keys.pop()
            if not node.is_leaf:
                node.children.insert(0, left_sibling.children.pop())
        elif right_sibling and len(right_sibling.keys) > self.min_keys:
            node.keys.append(parent.keys[index])
            parent.keys[index] = right_sibling.keys.pop(0)
            if not node.is_leaf:
                node.children.append(right_sibling.children.pop(0))
        print(f"Borrowed from sibling at index {index}: {node.keys}")

    def delete(self, key):
        self._delete_recursive(self.root, key)
        if not self.root.keys and not self.root.is_leaf:
            self.root = self.root.children[0]
        print(f"Deleted key {key}: {self.root.keys}")

    def _delete_recursive(self, node, key):
        if node.is_leaf:
            if key in node.keys:
                node.keys.remove(key)
        else:
            index = self._find(node, key)
            if index < len(node.keys) and node.keys[index] == key:
                self._delete_internal_node(node, key, index)
            else:
                child = node.children[index]
                if len(child.keys) > self.min_keys:
                    self._delete_recursive(child, key)
                else:
                    left_sibling = node.children[index - 1] if index > 0 else None
                    right_sibling = node.children[index + 1] if index < len(node.children) - 1 else None
                    if left_sibling and len(left_sibling.keys) > self.min_keys:
                        self._borrow_from_sibling(child, index, left_sibling, None, node)
                    elif right_sibling and len(right_sibling.keys) > self.min_keys:
                        self._borrow_from_sibling(child, index, None, right_sibling, node)
                    else:
                        if left_sibling:
                            self._merge_nodes(node, index - 1)
                            self._delete_recursive(left_sibling, key)
                        else:
                            self._merge_nodes(node, index)
                            self._delete_recursive(child, key)

    def _delete_internal_node(self, node, key, index):
        left_child = node.children[index]
        right_child = node.children[index + 1]
        if len(left_child.keys) > self.min_keys:
            predecessor = self._get_max_key(left_child)
            node.keys[index] = predecessor
            self._delete_recursive(left_child, predecessor)
        elif len(right_child.keys) > self.min_keys:
            successor = self._get_min_key(right_child)
            node.keys[index] = successor
            self._delete_recursive(right_child, successor)
        else:
            self._merge_nodes(node, index)
            self._delete_recursive(left_child, key)

    def _get_max_key(self, node):
        while not node.is_leaf:
            node = node.children[-1]
        return node.keys[-1]

    def _get_min_key(self, node):
        while not node.is_leaf:
            node = node.children[0]
        return node.keys[0]

    def show(self):
        levels = [self.root]
        while levels:
            current = levels
            levels = []
            for node in current:
                if not node.is_leaf:
                    levels.extend(node.children)
            print(' | '.join(str(node) for node in current))
        print('-' * 50)

def main():
    if len(sys.argv) != 2:
        print("Usage: python BPlusTree.py <order>")
        sys.exit(1)

    order = int(sys.argv[1])
    tree = BPlusTree(order)
    print("B+ Tree created with order:", order)
    print("Available commands: INSERT <value>, DELETE <value>, UPDATE <old_value> <new_value>, SHOW")

    while True:
        command = input("Enter command: ").strip()
        if command.startswith('INSERT'):
            _, value = command.split(maxsplit=1)
            tree.insert(eval(value))  # Using eval to handle different data types
            tree.show()
        elif command.startswith('DELETE'):
            _, value = command.split(maxsplit=1)
            tree.delete(eval(value))  # Using eval to handle different data types
            tree.show()
        elif command.startswith('UPDATE'):
            _, old_value, new_value = command.split(maxsplit=2)
            tree.delete(eval(old_value))  # Using eval to handle different data types
            tree.insert(eval(new_value))  # Using eval to handle different data types
            tree.show()
        elif command == 'SHOW':
            tree.show()
        elif command.lower() == 'exit':
            print("Exiting B+ Tree Interactive Shell.")
            break

if __name__ == '__main__':
    main()
