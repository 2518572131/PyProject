#字典取值一般有两种方法，一种是根据key值，取value
#一种是使用get方法来取值
#不同之处是第一种取值，当value值不存在时，会报错；而get方法取值当value值不存在时，则会返回none
score={'张三':'90','李四':'98','李四':'92'}
print(score)
print(score['张三'])
print(score.get('李四'))