import platform

class System():
    def __init__(self):
        self.platform = platform

class SystemA(System):
    def get_info(self):
        print(self.platform.system())

class SystemB(System):
    def get_info(self):
        print(self.platform.release())

class SystemC(System):
    def get_info(self):
        print(self.platform.version())

