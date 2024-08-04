# Parent class
class Parent:
    _protected_field = "This is protected"

    def _protected_method(self):
        print("Accessing protected field: {_protected_field}")

# Class in the same package
class SamePackage:
    def access_parent(self, parent_obj):
        print(parent_obj._protected_field)
        parent_obj._protected_method()

# Child class in different package
class Child(Parent):
    def access_protected(self):
        print(self._protected_field)
        self._protected_method()

# Class in different package
class DifferentPackage:
    def __init__(self, parent_obj):
        self._parent = parent_obj

    def access_protected(self):
        # Accessing protected field through protected method
        self._parent._protected_method()

# Usage
parent = Parent()
same_package = SamePackage()
same_package.access_parent(parent)

child = Child()
child.access_protected()

different_package = DifferentPackage(parent)
different_package.access_protected()