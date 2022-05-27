import re
import nltk as nltk
import nltk.draw as draw

with open("StringP.txt", "r") as file:
    first_line = file.readline().rstrip()

def recTuple(x,mylist):

    for i in x:
        if type(i)==tuple:
            mylist.append('(')
            mylist.append(' ')
            recTuple(i,mylist)
            mylist.append(' ')
            mylist.append(')')
        else:
            mylist.append(i)
            mylist.append(' ')


def toTree(infixStr):
    tokens = re.split(r' *([\+\-\*/]) *', infixStr)
    tokens = [t for t in reversed(tokens) if t!='']
    precs = {'+':0 , '-':0, '/':1, '*':1}


    def toTree2(tokens, minprec):
        node = tokens.pop()
        while len(tokens)>0:
            prec = precs[tokens[-1]]
            if prec<minprec:
                break
            op=tokens.pop()

            arg2 = toTree2(tokens,prec+1)
            node = (op, node, arg2)
        return node

    return toTree2(tokens,0)
mylist=[]
mylist.append('(')
mylist.append(' ')
x=toTree(first_line)
recTuple(x,mylist)
mylist.append(' ')
mylist.append(')')

print(x)
print(mylist)
print(''.join(mylist))

txt= ''.join(mylist)
tree = nltk.Tree.fromstring(txt)
draw.draw_trees(tree)
