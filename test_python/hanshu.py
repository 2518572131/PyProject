#函数调用
def greet_user():
    print("Hello!");
greet_user();

#传递参数信息
def greet_user01(message):
    print("hello,"+message.title()+"!");
greet_user01('jesson');


#小动物
def describe_name(animal_type,anmli_name):
    print("I have an "+animal_type+"!");
    print("it is name "+anmli_name+"!");
describe_name('cat','pet');
describe_name('dog','yiyi');

#返回值
def get_full_name(first_name,last_name):
    full_name=first_name  + ' ' + last_name;
    return full_name.title();
musicname=get_full_name('yiyi','lili');
print(musicname);