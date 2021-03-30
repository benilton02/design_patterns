from system import (
	SystemA,
	SystemB,
	SystemC,
)

class Facade:
    def __init__(self, 
        system_a = SystemA(), 
        system_b = SystemB(), 
        system_c = SystemC()
    ):
    
        system_a.get_info()   
        system_b.get_info()
        system_c.get_info()