from singleton import Singleton

if __name__ == "__main__":
    
    first_instance = Singleton()
    second_instance = Singleton()

    print(first_instance is second_instance)