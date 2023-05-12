class Tree:
    pass

class Leaf(Tree):
    pass

class Branch(Tree):
    def __init__(self, left, right):
        self.left = left
        self.right = right

def treeToParens(tree):
    if isinstance(tree, Leaf):
        return '()'
    elif isinstance(tree, Branch):
        left_parens = treeToParens(tree.left)
        right_parens = treeToParens(tree.right)
        return '(' + left_parens + right_parens + ')'

def parensToTree(parens):
    stack = []
    for char in parens:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                if len(stack) >= 2 and isinstance(stack[-1], Tree) and isinstance(stack[-2], Tree):
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(Branch(left, right))
            else:
                raise ValueError("Invalid parentheses string")
        else:
            raise ValueError("Invalid parentheses string")

    if len(stack) != 1 or not isinstance(stack[0], Tree):
        raise ValueError("Invalid parentheses string")

    return stack[0]
