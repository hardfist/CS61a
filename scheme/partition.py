S=set()
def part(total,max_value,max_piece,stk):
    if max_value <=0 or total < 0:
        return 
    if total == 0:
        S.add(stk)
    if len(stk) >=max_piece:
        return
    lst1=part(total,max_value-1,max_piece,stk)
    lst2=part(total-max_value,max_value,max_piece,stk+(max_value,))
part(5,3,4,())
class Tree:
    def __init__(self,val,child=[]):
        self.val = val
        self.child=child
    def addchild(ch):
        self.child.append(ch)
root=Tree(5,[
    Tree(6,
         [Tree(9),Tree(8)]),
    Tree(7,
         [Tree(1)]),
    Tree(2,
         [Tree(6,[Tree(3)]),
          Tree(4)])])
def tree_sum(root,s,S):
    if root.child == []:
        return S.add(s+root.val)
    for ch in root.child:
        tree_sum(ch,s+root.val,S)
S=set()
tree_sum(root,0,S)
print(S)
