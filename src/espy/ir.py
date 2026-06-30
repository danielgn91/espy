class Operation:
    pass

class WhereOperation(Operation):
    def __init__(self, filters):
        self.filters = filters