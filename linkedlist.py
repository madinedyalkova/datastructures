class Node:
    def __init__(self, data, n = None):
        self.data = data
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data

class LinkedList:
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, data):
        p_node = self.root
        pr_node = None
        while p_node:
            if p_node.get_data() == data:
                if pr_node:
                    pr_node.set_next(p_node.get_next())
                else:
                    self.root = p_node
                self.size -=1
                return True
            else:
                pr_node = p_node
                p_node = p_node.get_next()
        return False
    
    def find(self, data):
        p_node = self.root
        while p_node:
            if p_node.get_data() == data:
                return data
            else:
                p_node = p_node.get_next()
        return None
            
    
