import sys

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
        if len(parent.keys) == self.order:
            self._split_root()

    def _split_root(self):
        old_root = self.root
        new_root = self.Node()
        new_root.children.append(old_root)
        self._split_child(new_root, 0)
        self.root = new_root

    def insert(self, key, data=None):
        if len(self.root.keys) == self.order - 1:
            self._split_root()
        self._insert_non_full(self.root, key, data)

    def delete(self, key):
        if not self._delete_recursive(self.root, key) and not self.root.keys:
            self.root = self.root.children[0] if not self.root.is_leaf else self.Node(is_leaf=True)

    def _delete_recursive(self, node, key):
        index = self._find(node, key)
        if node.is_leaf:
            if index < len(node.keys) and node.keys[index] == key:
                node.keys.pop(index)
                return True
            return False
        if index < len(node.keys) and node.keys[index] == key:
            node.keys[index] = self._delete_internal(node.children[index])
            return True
        elif self._delete_recursive(node.children[index], key):
            if len(node.children[index].keys) < self.min_keys:
                self._fix_deficiency(node, index)
            return True
        return False

    def _delete_internal(self, node):
        if node.is_leaf:
            return node.keys.pop()  # Return last key
        return self._delete_internal(node.children[-1])

    def _fix_deficiency(self, node, index):
        child = node.children[index]
        left_sibling = node.children[index - 1] if index > 0 else None
        right_sibling = node.children[index + 1] if index < len(node.children) - 1 else None

        if left_sibling and len(left_sibling.keys) > self.min_keys:
            child.keys.insert(0, node.keys[index - 1])
            node.keys[index - 1] = left_sibling.keys.pop()
            if not left_sibling.is_leaf:
                child.children.insert(0, left_sibling.children.pop())
        elif right_sibling and len(right_sibling.keys) > self.min_keys:
            child.keys.append(node.keys[index])
            node.keys[index] = right_sibling.keys.pop(0)
            if not right_sibling.is_leaf:
                child.children.append(right_sibling.children.pop(0))
        else:
            if left_sibling:
                left_sibling.keys.extend([node.keys.pop(index - 1)] + child.keys)
                left_sibling.children.extend(child.children)
                node.children.pop(index)
            else:
                child.keys.extend([node.keys.pop(index)] + right_sibling.keys)
                child.children.extend(right_sibling.children)
                node.children.pop(index + 1)
            if len(node.keys) == 0 and node == self.root:
                self.root = child  # Reduce tree height

    def show(self):
        levels = [self.root]
        while levels:
            current = levels
            levels = []
            for node in current:
                if not node.is_leaf:
                    levels.extend(node.children)
            print(' | '.join(str(node) for node in current))

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
            _, value = command.split()
            tree.insert(int(value))
            tree.show()
        elif command.startswith('DELETE'):
            _, value = command.split()
            tree.delete(int(value))
            tree.show()
        elif command.startswith('UPDATE'):
            _, old_value, new_value = command.split()
            tree.delete(int(old_value))
            tree.insert(int(new_value))
            tree.show()
        elif command == 'SHOW':
            tree.show()
        elif command.lower() == 'exit':
            print("Exiting B+ Tree Interactive Shell.")
            break

if __name__ == '__main__':
    main()
