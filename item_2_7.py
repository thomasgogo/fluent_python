# list.sort 方法和内置函数 sorted

# list.sort 方法会就地排序列表,也就是说不会把原列表复制一份.这也就是这个方法的返回值是 None 的原因,提醒你本方法不会新建一个列表.
# 在这种情况下返回 None 其实是 python 的一个惯例:如果一个函数或者方法对对象进行的是就地改动,那它就应该返回 None,好让调用者
# 知道传入的参数发生了变动,而且并未产生新的对象

# 与 list.sort 相反的内置函数sorted,它会新建一个列表作为返回值.这方法可以接收任何形式的可迭代对象作为参数,甚至包括不可变序列或生成器
# 两者都有可选的关键字参数
# reverse 如果被设定为 True,被排序的序列里的元素会以降序输出.参数默认值为 False
# key 一个只有一个参数的函数,这个函数会被用在序列里的每一个元素上,所产生的结果将是排序算法依赖的对比关键字.

fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits))

print(fruits)

print(sorted(fruits, reverse=True))

print(sorted(fruits, key=len))

print(sorted(fruits, key=len, reverse=True))

fruits.sort()
print(fruits)

