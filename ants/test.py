class A:
    watersafe = True
    def __init__(self):
        print(self.watersafe)
        
class B(A):
    watersafe = False
    def __init__(self):
        print(self.watersafe)
class C(B):
    def __init__(self):
        print(self.watersafe)
