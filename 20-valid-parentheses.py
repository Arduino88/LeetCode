def trimString(index: int, string: str) -> str:
    if index < (len(string) - 1):
        string = string[:index] + string[(index + 1):]
    else:
        string = string[:index]
    return(string)

s = '()[]{}'

stack = []
removeIndex = []

if len(stack) > 0:
    print(stack[-1])

for i in range(len(s)):
    if s[i] == ')':
        if stack[-1:] == '(':
            stack.pop()
        else:
            removeIndex.append(i)
            