class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __len__(self):
        return self.length + self.width
    
    def __add__(self, r):
        return self.width + r.width
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def __get_item__(self)


r1 = Rectangle(2,3)
r2 = Rectangle(3,4)

for i in r1:
    print(i)

r1[0]