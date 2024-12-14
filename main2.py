import stack
open = ["{","[","("]
close = ["}","]",")"]

def check(equation):
    s = stack.Stack(100)
    for i in equation:
        if i in open:
            s.push(i)
            s.display()
        elif i in close:
            x = s.pop()
            print(s.pop())
            s.display()
            print(i,x)
            if not open.index(x) == close.index(i):
                return False
    if s.size() == 0:
        return True
    else:
        return False
    
print(check("(x+2)+y-z}-{5-6]"))


                