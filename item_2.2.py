# 列表推导和生成器表达式

# 列表推导和生成器表达式
# 列表推导是构建列表的快捷方式,而生成器表达式则可以用来创建其他任何类型的序列.如果你的代码里并不经常使用它们,那么很可能你错过了
# 许多写出可读性更好且更高效的代码的机会.

# 列表推导和可读性
symbols = '$C#!$%^&*()'

codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

# 通常的原则是,只用列表推导来创建新的列表,并且尽量保持简短.

# 在 python3 中同名变量都有自己的局部作用域,就像函数似的.表达式内部的变量和赋值只在局部其作用,表达式的上下文里的同名变量还可以被正常
# 引用,局部变量并不会影响到他们.

# 列表推导同 filter 和 map 的比较
# filter 和 map 合起来能做的事情,列表推导也可以做,而且还不需要借助难以理解和阅读的 lambda 表达式.

beyond_ascii = [ord(s) for s in symbols if ord(s) > 38]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 38, map(ord, symbols)))
print(beyond_ascii)

# map/filter组合起来不一定比列表推导快