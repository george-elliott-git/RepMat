class Group:
    def __init__(self, elements, operation):
        # By definition of a group, we require an identity, an inverse, and group associativity
        self.elements = set(elements)
        self.operation = operation

        # Check if closure holds
        self.check_closure()
        
        # Check for identity and inverses
        self.identity = self.find_identity()
        self.inverses = self.find_inverses()

    def check_closure(self):
        for x in self.elements:
            for y in self.elements:
                if self.operation(x, y) not in self.elements:
                    raise ValueError("Closure property does not hold!")

    def find_identity(self):
        for e in self.elements:
            if all(self.operation(e, x) == x and self.operation(x, e) == x for x in self.elements):
                return e
        raise ValueError("No identity element found!")

    def find_inverses(self):
        inverses = {}
        for x in self.elements:
            for y in self.elements:
                if self.operation(x, y) == self.identity and self.operation(y, x) == self.identity:
                    inverses[x] = y
                    break
            else:
                raise ValueError(f"No inverse found for value {x}")
        return inverses

    def group_check(self):
        return bool(self.identity) and len(self.inverses) == len(self.elements)

    def display_group_info(self):
        print(f"Group with elements: {self.elements}")
        print(f"Group operation: {self.operation}")
        print(f"Identity: {self.identity}")
        print(f"Inverses: {self.inverses}")

def create_Group(elements, operation):
    return Group(elements, operation)

