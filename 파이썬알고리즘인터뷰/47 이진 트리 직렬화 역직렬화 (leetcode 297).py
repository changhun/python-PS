# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output_len = self.get_max_seq(root, 0) + 1
        #output = [None] * output_len
        output = ["null"] * output_len
        self.do_serialize(root, 0, output)
        ret = ','.join(map(str, output))
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        list_data = self.str_to_list(data)
        root = self.do_deserialize(list_data, 0)
        return root

    def get_max_seq(self, root, seq):
        if not root:
            return 0

        #return max(self.get_max_seq(root.left, seq*2 + 1), self.get_max_seq(root.right, seq*2 + 2), seq)
        left = self.get_max_seq(root.left, seq*2 + 1)
        right = self.get_max_seq(root.right, seq*2 + 2)
        return max(left, right, seq)

    def do_serialize(self, root, seq, output):
        if not root:
            return

        output[seq] = root.val
        self.do_serialize(root.left, seq*2 + 1, output)
        self.do_serialize(root.right, seq * 2 + 2, output)

    def str_to_list(self, data):
        """
        :type data: str
        :rtype: list
        """
        #list_data = list(map(int, data.split(',')))
        list_data = data.split(',')
        for i in range(len(list_data)):
            if list_data[i] == "null":
                list_data[i] = None
            else:
                list_data[i] = int(list_data[i])

        return list_data

    def do_deserialize(self, list_data, seq):
        if seq >= len(list_data) or list_data[seq] is None:
            return None

        node = TreeNode(list_data[seq])
        node.left = self.do_deserialize(list_data, seq*2 + 1)
        node.right = self.do_deserialize(list_data, seq * 2 + 2)
        return node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


#data = "1,2,3,null,null,4,5"
#data = input()
#root = Codec().deserialize(data)
#print(root)
#root = TreeNode(3)
cur = root = TreeNode(1)

#for i in range(2, 1001):
for i in range(2, 4):
    cur.right = TreeNode(i)
    cur = cur.right

serialized = Codec().serialize(root)
print(serialized)

