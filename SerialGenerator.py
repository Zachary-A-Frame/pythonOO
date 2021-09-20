class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, counter):
        "Instantiate counter from 100."
        self.counter = counter

    def generate(self):
        print(self.counter)
        self.counter += 1

    def reset(self):
        self.counter = 100
    ...

