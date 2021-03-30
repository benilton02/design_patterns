class Singleton():
    
    singleton = None
    def __new__(cls):
        if cls.singleton is None:
            cls.singleton = object.__new__(cls)
            print(cls.singleton)
        return cls.singleton