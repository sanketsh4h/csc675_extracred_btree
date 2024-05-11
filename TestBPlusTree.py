import unittest

class TestBPlusTree(unittest.TestCase):
    def setUp(self):
        self.tree = BPlusTree(3)

    def test_inserts(self):
        keys = [10, 20, 5, 30, 25]
        for key in keys:
            self.tree.insert(key)
        self.assertEqual(len(self.tree.root.keys), 1)

    def test_structure(self):
        keys = [10, 20, 5, 30, 25]
        for key in keys:
            self.tree.insert(key)
        self.tree.insert(15)
        self.tree.show()  # This will print the tree for visual inspection

if __name__ == '__main__':
    unittest.main()
