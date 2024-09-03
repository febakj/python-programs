class A:
    def method_a(self):
        return "Method A"

class B(A):
    def method_b(self):
        return "Method B"

class C(A):
    def method_c(self):
        return "Method C"

class D(B, C):
    pass

# Usage
d = D()
print(d.method_a())  # Method A
print(d.method_b())  # Method B
print(d.method_c())  # Method C
