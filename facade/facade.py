from system import (
	SystemA,
	SystemB,
	SystemC,
)

class Facade:
    def __init__(self):
        self.systems = [
            SystemA(), 
            SystemB(), 
            SystemC()
        ]
    
        self.instance()

    def instance(self):
        list(map(lambda system: system.get_info(), self.systems))  
        