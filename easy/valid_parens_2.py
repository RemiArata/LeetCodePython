# Valid Parens using a Stack data structure

class Node:
    def __init__(self, val=None):
        self.value = val
        self.previous = None


class Stack:
    def __init__(self) -> None:
        self.current_node = None
    
    def push(self, val) -> None:
        n = Node(val)
        if self.current_node == None:
            self.current_node = n
        else:
            n.previous = self.current_node
            self.current_node = n
    
    def top(self):
        return self.current_node.value
    
    def pop(self) -> None:
        if self.current_node == None:
            pass
        elif self.current_node.previous != None:
            self.current_node = self.current_node.previous
        else:
            self.current_node = None

    def show(self):
        print("----top-----")
        n = self.current_node
        while n:
            print(f"-> {n.value}")
            n = n.previous


def valid_parens(s: str) -> bool:
    
    stack = Stack()

    for itm in s:
        if itm in "({[":
            stack.push(itm)
        else:
            val = stack.top()
            if itm == ")" and val == "(":
                stack.pop()
            elif itm == "]" and val == "[":
                stack.pop()
            elif itm == "}" and val == "{":
                stack.pop()
            else:
                return False
    return True
    
    

s = "()"
print(valid_parens(s))

s = "()[]{}"
print(valid_parens(s))

s = "(]"
print(valid_parens(s))

s = "([)]"
print(valid_parens(s))