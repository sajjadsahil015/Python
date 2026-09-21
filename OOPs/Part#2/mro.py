class A:
    def greet(self):
        return "Hello from A"
class B(A):
    def greet(self):
        return "Hello from B"
class C(A):
    def greet(self):
        return "Hello from C"
class D(B,C):
    pass
d = D()
print(D.mro())
print(d.greet())