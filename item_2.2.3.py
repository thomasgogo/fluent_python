# 笛卡尔积

# 使用列表推导计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

# 列表推导的作用只有一个,生成列表.如果想生成其他类型的序列,生成器表达式就派上了用场.

# 2.2.4 生成器表达式
# 生成器表达式背后遵守了迭代器协议,可以逐个地产生元素,而不是先建立一个完整的列表,然后再把这个列表传递到某个构造函数里.
# 生成器表达式的语法跟列表推导差不多,只不过把方括号换成圆括号而已.

# 如何用生成器表达式建立元组和数组.
symbols = '!@#$%^'
print(tuple(ord(symbol) for symbol in symbols))
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))
