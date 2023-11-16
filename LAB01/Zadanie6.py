import unittest

class TreeStructure:
    def __init__(self, value, edge=None):
        self.value = value
        self.edge = edge
        self.left = None
        self.right = None

    def insert_left(self, value, edge=None):
        t = TreeStructure(value, edge)
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t

    def insert_right(self, value, edge=None):
        t = TreeStructure(value, edge)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_val(self, obj):
        self.value = obj

    def get_root_val(self):
        return self.value

    def __str__(self):
        if self.edge is not None:
            return f"[{self.value}; {self.edge}; {self.left}; {self.right}]"
        else:
            return f"[{self.value}; {self.left}; {self.right}]"


r = TreeStructure('Władysław Jagiełło')
print(r)
r.insert_left('Władysław Warnenczyk', '1424')
r.insert_right('Kazimierz Jagiellonczyk', '1427')
print(r)
r.get_right_child().insert_right('Zygmunt Stary', '1467')
r.get_right_child().insert_left('Jan Olbracht', '1459')
print(r)


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(r.get_root_val(), 'Władysław Jagiełło')
        self.assertEqual(r.get_left_child().get_root_val(), 'Władysław Warnenczyk')
        self.assertIsNone(r.get_left_child().get_left_child())
        self.assertEqual(r.get_right_child().edge, '1427')


if __name__ == '__main__':
    unittest.main()

