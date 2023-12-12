#静态方法的创建和调用
# 由于静态方法不依赖于类或实例的状态，所以它们主要用于执行与类或实例无关的操作。
#当一个方法不需要访问类或实例的属性时，可以将其定义为静态方法。这有助于提高代码清晰度和可维护性。
class Myclass():
    @staticmethod
    def method(a, b):
        return a + b


print(Myclass.method(1, 2))
m1 = Myclass()
print(m1.method(1, 2))

#单例模型  第一次实例化对象 会存到
class SingletonMeta():
    _instance = None

    def __new__(cls, *args, **kwargs):
        print('this is __new__')
        if not cls._instance:
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self):
        print('this is __init')

s1 = SingletonMeta()
s2 = SingletonMeta()
s3 = SingletonMeta()
print(s1 is s2 is s3)
print(id(s1),id(s2),id(s3))

