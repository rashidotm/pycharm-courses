class MyClass:
    variable = 4

    def foo(self):   # we'll explain self parameter later in task 4
        print("Hello from function foo")

class noClass:
    def foo(self):
        print("hello")

my_object = noClass()
my_object.foo()

my_object = MyClass()  # variable "my_object" holds an object of the class "MyClass" that contains the variable and the "foo" function
my_object.foo()
print(my_object.variable)