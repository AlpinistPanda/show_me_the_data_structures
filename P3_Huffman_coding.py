from collections import deque
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


class Tree:
    def __init__(self, node=None):
        self.root = node

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node


class Huffman:

    def __init__(self):
        self.char_freq = dict()
        self.encoded_data = dict()

    def huffman_encoding(self, data):

        tree = Tree()
        old_char_freq = {}
        sorted_list = list()
        code = ""
        for i in data:
            if i in old_char_freq:
                old_char_freq[i] += 1
            else:
                old_char_freq[i] = 1

        for key in old_char_freq:
            self.char_freq[Node(key)] = old_char_freq.get(key)

        sorted_list = sorted(self.char_freq, key=self.char_freq.get)
        if (len(self.char_freq.keys()) == 0):
            return code, tree
        elif (len(self.char_freq.keys()) == 1):
            tree.set_root(Node(data))
            code = "0" * (len(data))
            return code, tree
        tree = self.create_tree(tree, sorted_list)

        code = data
        self.encode_characters(tree.get_root(), "")

        for i in self.encoded_data:
            code = code.replace(i.value.value, self.encoded_data.get(i))

        return code, tree

    def create_tree(self, tree, sorted_list):

        if (tree.get_root() is None):
            node = Node(self.char_freq.get(sorted_list[0]) + self.char_freq.get(sorted_list[1]))
            node.left = Node(sorted_list[0])
            node.right = Node(sorted_list[1])
            self.char_freq.pop(sorted_list[0])
            self.char_freq.pop(sorted_list[1])
            self.char_freq[node] = node.value

        else:
            node = Node(self.char_freq.get(sorted_list[0]) + tree.get_root().value)
            node.left = tree.get_root()

            if (sorted_list[0].__class__.__name__ == "Node"):
                node.right = sorted_list[0]
            else:
                node.right = Node(sorted_list[0])
            self.char_freq.pop(sorted_list[0])
            self.char_freq.pop(sorted_list[1])
            self.char_freq[node] = node.value

        if (len(self.char_freq) == 1):
            tree.set_root(node)
            return tree

        sorted_list = sorted(self.char_freq, key=self.char_freq.get)
        return self.create_tree(tree, sorted_list)

    def huffman_decoding(self, code, tree):
        if (len(code) == 0):
            return ""
        elif (len(code) == 1):
            return tree.get_root().value

        self.encode_characters(tree.get_root(), "")

        reversed_encoded_data = dict()

        for key in self.encoded_data:
            reversed_encoded_data[self.encoded_data.get(key)] = key

        decoded_data = ""
        temp_str = ""
        for i in code:
            temp_str += i
            if temp_str in reversed_encoded_data:
                if (reversed_encoded_data.get(temp_str).value.__class__.__name__ == 'Node'):
                    decoded_data += reversed_encoded_data.get(temp_str).value.value
                else:
                    decoded_data += reversed_encoded_data.get(temp_str).value
                temp_str = ""

        return decoded_data

    def encode_characters(self, node, code):

        if (node is None):
            return None

        if (node.value.__class__.__name__ == "int"):
            if (node.get_left_child()):
                self.encode_characters(node.left, code + "0")
            if (node.get_right_child()):
                self.encode_characters(node.right, code + "1")

        elif (node.value.__class__.__name__ == "Node"):

            if (node.value.value.__class__.__name__ == "str"):
                self.encoded_data[node] = code

            elif (node.value.value.__class__.__name__ == "int"):
                if (node.value.get_left_child()):
                    self.encode_characters(node.value.left, code + "0")
                if (node.value.get_right_child()):
                    self.encode_characters(node.value.right, code + "1")
        elif (node.value.__class__.__name__ == 'str'):
            self.encoded_data[node] = "0" * len(node.value)


def codeencode(a_great_sentence):
    hufenc = Huffman()

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}\n")
    print(f"The content of the data is: {a_great_sentence}\n")
    encoded_data, tree = hufenc.huffman_encoding(a_great_sentence)
    if (encoded_data):
        print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}\n")
    else:
        print("The size of the encoded data is: {}\n".format(encoded_data, base=2))
    print(f"The content of the encoded data is: {encoded_data}\n")

    hufdec = Huffman()
    decoded_data = hufdec.huffman_decoding(encoded_data, tree)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)} \n")
    print(f"The content of the encoded data is: {decoded_data}\n")


codeencode("Ozgun Balaban")

'''
The size of the data is: 62

The content of the data is: Ozgun Balaban

The size of the encoded data is: 32

The content of the encoded data is: 101010111100110110011101111010000100101100

The size of the decoded data is: 62 

The content of the encoded data is: Ozgun Balaban
'''

codeencode("")

'''
The size of the data is: 49

The content of the data is: 

The size of the encoded data is: 

The content of the encoded data is: 

The size of the decoded data is: 49

The content of the encoded data is: 
'''

codeencode("aaaaa")

'''
The size of the data is: 54

The content of the data is: aaaaa

The size of the encoded data is: 24

The content of the encoded data is: 00000

The size of the decoded data is: 54

The content of the encoded data is: aaaaa

'''
