

def ExecutionTarget(object):
    """
    ExecutionTarget describes an abstract location where we may rehost firmware.

    Execution environments should implement this to be managed by HALucinator.
    """

    def __init__(self, *args, **kwargs):
        self.regs = dict()

    @abstract
    def read_memory(self, address, size):
        pass

    @abstract
    def write_memory(self, address, size, value):
        pass



