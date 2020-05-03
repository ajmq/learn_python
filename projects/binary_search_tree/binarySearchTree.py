


class Node:

    def __init__(self, val: int):
        self.val = val
        self.left_node = None
        self.right_node = None

    def set_left_node(self, left_node):
        self.left_node = left_node

    def set_right_node(self, right_node):
        self.right_node = right_node

    def get_left_node(self, ):
        return self.left_node

    def get_right_node(self, ):
        return self.right_node 


class BST:

    def __init__(self, root_val):
        self.root = Node(root_val)
    

    def add_value_iter(self,val, curr_node):
        if val> curr_node.val:
            if curr_node.right_node is None:
                curr_node.set_right_node(Node(val))
            else:
                self.add_value_iter(val,curr_node.get_right_node())

        elif val<= curr_node.val:
            if curr_node.left_node is None:
                curr_node.set_left_node(Node(val))
            else:
                self.add_value_iter(val,curr_node.get_left_node())



    def add_value(self,val):
        self.add_value_iter(val, self.root)


    

    def print_tree(self,curr_node="", level=1, parent_level=0, parent_dir=""):
        if curr_node=="":
            curr_node=self.root

        left_node = curr_node.get_left_node()
        right_node = curr_node.get_right_node()


        string = """Level :{}  
        Parent Lv : {} Parent dir: {}
            - Node Val[ {} ] 
                    LeftNode[ {} ]      RightNode[ {} ]
        =====================================
                """.format(level,parent_level, parent_dir,curr_node.val,left_node,right_node)
        print(string)
        if curr_node.get_left_node() is not None:
            self.print_tree(curr_node=curr_node.get_left_node(), level=level+1, parent_level=level, parent_dir="Left")
        if curr_node.get_right_node() is not None:
            self.print_tree(curr_node=curr_node.get_right_node(), level=level+1, parent_level=level, parent_dir="Right")
        



root = BST(10)
root.add_value(11)
root.add_value(8)
root.add_value(13)
root.add_value(5)
root.add_value(9)


root.print_tree()


