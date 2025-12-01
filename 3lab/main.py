log = []

def calc(expr):
    expr = expr.strip()
    log.append("вычисляем: " + expr)

    if "(" not in expr:
        result = eval(expr)     # самый простой способ
        log.append(f"{expr} = {result}")
        return result

    left = expr.rfind("(")
    right = expr.find(")", left)

    inside = expr[left+1:right]
    log.append("нашли скобки: " + inside)

    value = calc(inside)

    new_expr = expr[:left] + str(value) + expr[right+1:]
    log.append("после подстановки: " + new_expr)

    return calc(new_expr)


expr = "(2 + (3 * (4 - 1)))"
res = calc(expr)

print("Результат:", res)
print("\nШаги:")
for s in log:
    print(s)