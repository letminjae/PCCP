# 4949 균형잡힌 세상

while True:
    sentence = input()
    stack = []
    
    if sentence == ".":
        break

    for s in sentence:
        if s == "[" or s == "(":
            stack.append(s)
        elif s == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif s == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")