def is_num(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calc(expression):
    expression = expression.split()
    expression = [float(x) if is_num(x) else x for x in expression]
    if expression[0] == "+":
        return sum(expression[1:])
    if expression[0] == "-":
        return expression[1]-expression[2]
    if expression[0] == "/":
        if expression[2] == 0:
            raise ValueError
        return expression[1]/expression[2]
    if expression[0] == "*":
        return expression[1]*expression[2]


def calc(expression):
    op, left, right = expression.split()
    left = float(left)
    right = float(right)
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "/":
        if right == 0:
            raise ValueError
        return left / right
    if op == "*":
        return left * right


assert calc("+ 1 2") == 3
assert calc("- 1 2") == -1
assert calc("* 1 2") == 2
assert calc("/ 1 2") == 0.5
assert calc("* 1 -2") == -2
assert calc("* 10.5 2") == 21
assert calc("* -10.5 -2") == 21
