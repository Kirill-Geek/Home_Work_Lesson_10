class TypeMeta(type):
    new_obj = None
    
    @classmethod
    def __prepare__(metacls, name, bases):
        return type.__prepare__(metacls, name, bases)
       
    def __new__(cls, name, bases, dict):
        return type.__new__(cls, name, bases, dict)
        

    def __init__(cls, name, bases, dict):
        super(TypeMeta, cls).__init__(name, bases, dict)
        
    def __call__(cls, *args, **kwargs):
        if cls.new_obj is None:
            cls.new_obj = super().__call__(*args, **kwargs)
        return cls.new_obj    

class My_Class(metaclass=TypeMeta):

    def method_1():
        print("Метод - 1")

    def method_2():
        print("Метод - 2")

obj_1 = My_Class()
obj_2 = My_Class()

print(obj_1 is obj_2) #True