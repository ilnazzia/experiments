class Point():
    # __instance = None

    # def __new__(cls, *args, **kwargs)
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance
    
    def clone(self):
        obj = Point(self.x, self.y)
        return obj
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
pt = Point(5, 6)
pt_clone = pt.clone()

print(id(pt), id(pt_clone))