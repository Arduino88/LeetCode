class Stack:
    def __init__(self):
        self.stack = []

    def returnTop(self) -> str:
        if len(self.stack) > 0:
            return(self.stack[-1])
        else:
            return('')
        
    def pop(self):
        self.stack.pop()

def trimString(index: int, string: str) -> str:
    if index < (len(string) - 1):
        string = string[:index] + string[(index + 1):]
    else:
        string = string[:index]
    return(string)

s = '()[]{()(())))))}}'
closing = [')', ']', '}']

bracketStack = Stack()
removeIndex = []

for i in range(len(s)):
    if s[i] in closing:
        if s[i] == ')':
            if bracketStack.returnTop() == '(':
                bracketStack.pop()
            else:
                removeIndex.append(i)
        elif s[i] == ']':
            if bracketStack.returnTop() == '[':
                bracketStack.pop()
            else:
                removeIndex.append(i)
        else:
            if bracketStack.returnTop() == '{':
                bracketStack.pop()
            else:
                removeIndex.append(i)
    else:
        bracketStack.stack.append(s[i])

for i in reversed(removeIndex):
    s = trimString(i, s)

print(s + "\n" + str(len(removeIndex)) + " characters removed.")


            