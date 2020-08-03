# 元组不仅仅是不可变的列表
# 元素不仅仅是不可变的列表,还可以用于没有字段名的记录.

# 2.3.1 元组和记录
# 元组其实是对数据的记录: 元祖中的每个元素都存放了记录中一个字段的数据,外加这个字段的位置.正是这个位置信息给数据赋予了意义.

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)


for country, _ in traveler_ids:
    print(country)

# 2.3.2 元组拆包
# 最好辨认的元组拆包形式就是平行赋值,也就是说把一个可迭代对象里的元素,一并赋值到由对应的变量组成的元组中.

# 用*来处理剩下的元素
# 在 python 中,函数用*args 来获取不确定数量的参数算是一种经典写法了.
a,b, *rest = range(5)
print(a,b, rest)

a,b, *rest = range(3)
print(a,b, rest)

a,b, *rest = range(2)
print(a,b, rest)

# 在平行赋值中,*前缀只能用在一个变量名前面,但是这个变量可以出现在赋值表达式的任意位置:
a, *body, c, d = range(5)
print(a, body, c, d)

*head, b ,c ,d = range(5)
print(head, b, c, d)
# 另外拆包还有一个强大功能,那就是可以应用在嵌套结构中.

# 2.3.3 嵌套元组拆包

# 2.3.4 具名元素
# collections.namedtuple 是一个工厂函数,他可以用来构建一个带字段名的元组和一个有名字的类--这个带名字的类对调试程序
# 有很大帮助.
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# 如何用具名元组来记录一个城市的信息

from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo, tokyo.name)
# 创建一个具名元组需要两个参数,一个是类名,另一个是类的各个字段的名字.后者可以由数个字符组成的可迭代对象,或者是由空格分隔开的字段名组成
# 的字符串.
# 存放在对应字段里的数据要以一串参数的形式传入到构造函数中(注意,元组的构造函数却只接受单一的可迭代对象)
# 可以通过字段名或者位置来获取一个字段的信息.

print(City._fields)

# _fields 属性是一个包含这个类所有字段名名称的元组.
# _make()通过接口一个可迭代对象来生成这个类的一个实例
# _asdict()把具名元组以 collections.OrderdDict 的形式返回,我们可以利用它来吧元组里的信息友好地呈现出来.

# 2.3.5 作为不可变列表的元组
# 如果要把元组当做列表来用的话,