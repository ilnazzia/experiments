class SingletonFive():
    __instance_num = 0
    __last_instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance_num < 5:
            cls.__last_instance = super().__new__(cls)
        cls.__instance_num += 1
        return cls.__last_instance
    
    def __init__(self, name):
        self.name = name
            
        

objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять





