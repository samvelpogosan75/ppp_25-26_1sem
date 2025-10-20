

if __name__ == "__main__":
def brackets(text):
    stack = []
    for index, symbol in enumerate(text, 1):
        if symbol in '([{':
            stack.append(symbol)
        elif symbol in ')]}':
            if not stack:
                return f"Ошибка на позиции {index}"
            last = stack.pop()
            if last + symbol not in ['()', '[]', '{}']:
                return f"Ошибка на позиции {index}"
    if stack:
        return "Ошибка: не все скобки закрыты"
    return "ok"
print(brackets("(a)(b(c[d{e{r}f{g}s}w]r)tasd)"))