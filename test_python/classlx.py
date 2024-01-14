class Dog():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def sit(self):
        print(self.name.title());
    def rool(self):
        print('age');
my_dog=Dog('sarh',9);
print(my_dog.name);
print(my_dog.age);
print(str(my_dog.age));
my_dog.sit();
my_dog.rool();