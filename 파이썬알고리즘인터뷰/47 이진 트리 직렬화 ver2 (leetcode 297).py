# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    seq = 0
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def do_serialize(root):
            if not root:
                output.append("None")
                return

            output.append(str(root.val))
            do_serialize(root.left)
            do_serialize(root.right)

        output = []
        do_serialize(root)

        return ','.join(output)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        list_data = self.str_to_list(data)
        self.seq = 0
        root = self.do_deserialize(list_data)
        return root


    def str_to_list(self, data):
        """
        :type data: str
        :rtype: list
        """
        #list_data = list(map(int, data.split(',')))
        list_data = data.split(',')
        for i in range(len(list_data)):
            if list_data[i] == "None":
                list_data[i] = None
            else:
                list_data[i] = int(list_data[i])

        return list_data

    def do_deserialize(self, list_data):
        cur_val = list_data[self.seq]
        self.seq += 1

        #if not cur_val: #이렇게 하면 cur_val 가 int 0 일 때도 조건에 포함된다. None 인지 체크하려면 is None 으로 확인해야 할듯.
        if cur_val is None:
            return cur_val

        node = TreeNode(cur_val)
        node.left = self.do_deserialize(list_data)
        node.right = self.do_deserialize(list_data)
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

data_list = Codec().str_to_list(serialized)
print(data_list)
root = Codec().deserialize(serialized)
print(root.val)