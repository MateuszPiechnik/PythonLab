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

    def min_value(self):

        min_val = self.value  # Initialize with the root value

        # Check left subtree
        if self.left:
            min_val_left = self.left.min_value()
            min_val = min(min_val, min_val_left)

        # Check right subtree
        if self.right:
            min_val_right = self.right.min_value()
            min_val = min(min_val, min_val_right)

        return min_val


r = TreeStructure(3)
print(r)
r.insert_left(2, '1424')
r.insert_right(8, '1427')
print(r)
r.get_right_child().insert_right(10, '1467')
r.get_right_child().insert_left(1, '1459')
print(r)

print(r.min_value())