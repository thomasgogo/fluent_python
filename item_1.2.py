# 如何使用特殊方法
# 通过内置的函数来使用特殊方法是最好的选择.这些内置函数不仅会调用特殊方法,通常还提供额外的好处,而且对于内置的类来说,他们的速度更快.

# 模拟数值类型
# 我们来实现一个二维向量(vector)类,这里的向量就是欧几里得几何中常用的概念.

from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v = Vector(3, 4)
print(abs(v))

# 字符串表示形式
# python 有一个内置的函数叫 repr,它能把一个对象用字符串的形式表达处理啊以便辨认,这就是字符串表示形式.repr 就是通过__repr__这个特殊方法
# 来得到一个对象的字符串表示形式的.

# __repr__所返回的字符串应该准确,无歧义,并且尽可能表达出如何用代码创建出这个被打印的对象.因此这里使用了类似调用对象构造器的表达形式
# __repr__和__str__的区别在于,后者是在 str()函数被使用,或是在用 print 函数打印一个对象的时候才被调用的,并且他返回的字符串对终端用户
# 更友好.

# 如果你只想实现这两个特殊方法中的一个,__repr__是更好的选择,因为如果一个对象没有__str__函数,而 python 又需要调用它的时候,解释器
# 会用__repr__作为替代.

# 自定义的布尔值
# 尽管 python 里有 bool 类型,但实际上任何对象都可以用于需要布尔值的上下文中.为了判定一个值 x 为真还是为假,python 会调用 bool(x),
# 这个函数只能返回 True 或 False.
# 默认情况下,我们自己定义的类的实例总被认为是真的,除非这个类对__bool__或者__len__函数有自己的实现.bool(x)的背后是调用 x.__bool__()的
# 结果;如果不存在__bool__方法,那么 bool(x)会尝试调用 x.__len__().若返回 0,则 bool 会返回 False;否则返回 False.
