class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4 
        self.mem_slots = mem_slots
    
    def get_config(self):
        config = []
        config.append(f'Материнская плата: {self.name}')
        config.append(f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}')
        config.append(f'Слотов памяти: 4')   # {len(self.mem_slots)}')
        config.append('Память: ' + "; ".join([f'{mem.name} - {mem.volume}' for mem in self.mem_slots]))
        return config

cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])
print(mb.get_config())