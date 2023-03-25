class Node:
    def __init__(self, data):
        self.data = data
        self.red = False
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.red = False
        self.root = self.nil
        self.size = 0

    def rotateLeft(self, node_y):
        node_x = node_y.right
        node_y.right = node_x.left
        if node_x.left != self.nil:
            node_x.left.parent = node_y
        node_x.parent = node_y.parent
        if node_y.parent == self.nil:
            self.root = node_x
        elif node_y == node_y.parent.left:
            node_y.parent.left = node_x
        else:
            node_y.parent.right = node_x
        node_x.left = node_y
        node_y.parent = node_x
        return

    def rotateRight(self, node_y):
        node_x = node_y.left
        node_y.left = node_x.right
        if node_x.right != self.nil:
            node_x.right.parent = node_y
        node_x.parent = node_y.parent
        if node_y.parent == self.nil:
            self.root = node_x
        elif node_y == node_y.parent.left:
            node_y.parent.left = node_x
        else:
            node_y.parent.right = node_x
        node_x.right = node_y
        node_y.parent = node_x
        return

    def insert(self, data):
        node = Node(data)
        parent = self.nil
        traverse_node = self.root
        while traverse_node != self.nil:
            parent = traverse_node
            if data < traverse_node.data:
                traverse_node = traverse_node.left
            else:
                traverse_node = traverse_node.right
        node.parent = parent
        if parent == self.nil:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node
        node.left = self.nil
        node.right = self.nil
        node.red = True
        self.size += 1
        self._fix_RB(node)

    def _fix_RB(self, node):
        while node.parent.red:
            parent = node.parent
            grand_parent = parent.parent
            if parent == grand_parent.left:
                uncle = grand_parent.right
                if uncle.red:
                    parent.red = False
                    uncle.red = False
                    grand_parent.red = True
                    node = grand_parent
                else:
                    if node == parent.right:
                        self.rotateLeft(parent)
                        (node, parent) = (parent, node)
                    parent.red = False
                    grand_parent.red = True
                    self.rotateRight(grand_parent)
            elif parent == grand_parent.right:
                uncle = grand_parent.left
                if uncle.red:
                    parent.red = False
                    uncle.red = False
                    grand_parent.red = True
                    node = grand_parent
                else:
                    if node == parent.left:
                        self.rotateRight(parent)
                        (node, parent) = (parent, node)
                    parent.red = False
                    grand_parent.red = True
                    self.rotateLeft(grand_parent)
        self.root.red = False

    def _searchNode(self, node, key):
        if node == self.nil:
            return False
        if node.data == key:
            return True
        if key > node.data:
            return self._searchNode(node.right, key)
        else:
            return self._searchNode(node.left, key)

    def search_RB(self, key):
        return self._searchNode(self.root, key)

    def print_height(self):
        print("height = ", self._print_height(self.root))

    def _print_height(self, node):
        if node == self.nil:
            return -1
        return max(1 + self._print_height(node.right), 1 + self._print_height(node.left))

    def print_tree_size(self):
        print("size of tree = ", self.size)


class DictTree:
    def __init__(self, file_path: str):
        self.t = RBTree()
        self.f = open(file_path, "r+")
        while True:
            word = self.f.readline()
            word = word.strip('\n')
            if word == "":
                break
            self.t.insert(word)

    def addToDict(self, word: str):
        if self.t.search_RB(word):
            print("ERROR!! WORD ALREADY EXISTS")
        else:
            self.t.insert(word)
            self.f.write('\n' + word)
        return

    def searchDict(self, word: str):
        if self.t.search_RB(word):
            print("YES")
        else:
            print("NO")
        return


D = DictTree("EN-US-Dictionary.txt")
D.addToDict("youssef")
D.addToDict("raid")
D.addToDict("battawy")
D.addToDict("youssef")
D.searchDict("battawy")
D.searchDict("ahmedhany")
print(D.t.size)
print(D.t.print_height())
D.f.close()
