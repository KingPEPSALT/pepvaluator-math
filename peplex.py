# Mathematical Expression Parser and evaluator

import re

operations = {
    "^":(lambda a,b : a**b),
    "/":(lambda a,b : a/b),
    "%":(lambda a,b : a%b),
    "*":(lambda a,b : a*b),
    "+":(lambda a,b : a+b),
    "-":(lambda a,b : a-b)
}

operator_tuples = [
    ("^"), ("/", "*", "%"), ("+", "-")
]

class ArithmeticTree:
    def __init__(self, lhs, operator, rhs):
        self.lhs = lhs
        self.operator = operator
        self.rhs = rhs
        
    def isPure(self):
        return self.rhs in operations.keys() and self.lhs in operators.keys()
    
    def impurity(self):
        return (self.lhs if self.lhs not in operations.keys() else None, self.rhs if self.rhs not in operations.keys() else None)
    
    def evaluate(self):
        return operations[self.operator](self.lhs if type(lhs) is str else self.lhs.evaluate(), int(self.rhs) if type(self.rhs) is str else self.rhs.evaluate())
    
def depth(bracketed_expression):
    depth_dict = {}
    depth, position = 0, 0
    if ")" not in bracketed_expression and "(" not in bracketed_expression:
        return {}
    for character in bracketed_expression:
        if character == "(" or character == ")":
            depth += 1 if character == "(" else -1
            depth_dict[position] = depth
            position += 1
    if not depth_dict[list(depth_dict)[-1]] == 0:
        print(f"WARNING: bracket mismatch in {bracketed_expression}")
    return depth_dict

def seek_next_bracket(depth_dict, position):
    for bracket in depth_dict.items():
        if bracket[0] > position and bracket[1] == depth_dict[position]-1:
            return bracket

def create_pure_node(short_expression):
    used_operator = None
    for operator in operations.keys():
        if re.search(f'^[0-9]+\{operator}[0-9]+$', short_expression) is not None:
            used_operator = operator
            break
    if used_operator is None:
        raise Exception(f'The expression: "{expression}" is an invalid expression')
    ab = re.findall('[0-9]+', short_expression)
    return ArithmeticTree(ab[0], used_operator, ab[1])

def level_expression(long_expression):
    if "(" in long_expression or ")" in long_expression:
        raise Exception(f"There is a bracket in the long_expression: {long_expression}")
    expressions = []
    level = []
    for operator_level in operator_tuples:
        for operator in operator_level:
            level += [(m.start(0), m.end(0)) for m in re.finditer(f"[0-9]+\{operator}[0-9]+", long_expression)]
        expressions.append(level)
        level = []
    return expressions


def _debug_level_expression(long_expression):
    levelled_expression = level_expression(long_expression)
    for level in levelled_expression:
    if not level:
        continue
    print("-------------------")
    for sub_expression in level:
        if not sub_expression:
            continue
        print(long_expression[sub_expression[0]:sub_expression[1]])

def operations(long_expression):
    operations = []
    for char in long_expression:
        if char in operations.keys():
            operations += char
    return operations

def create_impure_nodes(long_expression):
    levelled_expression = level_expression(long_expression))
    root_node = ArithmeticTree()
    # being worked on
    
        
