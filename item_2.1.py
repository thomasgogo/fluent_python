# 内置序列类型概览

#python 标准库用 C 实现了丰富的序列类型,列举如下:
# 容器序列
# list, tuple和 collections.deque 这些序列能存放不同类型的数据

# 扁平序列
# str,bytes,bytearray,memoryview 和 array.array,这类序列只能容纳一种类型.

#容器序列存放的是他们所包含的任意类型的对象的引用,而扁平序列里存放的是指而不是引用.换句话说,
# 扁平序列其实是一段连续的内存空间,更加紧凑,但是他里面只能存储诸如字符,字节和数值这种基础类型.

# 序列类型还能按照能否修改来分类
# 可变序列
# list, bytearray, array.array,collections.deque 和 memoryview.

# 不可变序列
# tuple,str 和 bytes

# 可变序列(MutableSequence) 和不可变序列(Sequence)的差异,同时也能看出前者从后者哪里继承了一些方法.

#                                                                MutableSequence
# Container                                                      __setitem__
# __contains__                                                   __delitem__
#                                                                insert
#                          Sequence                              append
#                          __getitem__                           reverse
#                          __contains__    <-------------        extend
#                          __iter__                              pop
#                          __reversed__                          remove
#                          index                                 __iadd__
#                          count
# Iterable
# __iter__
#
#
#
# Sized
# __len__
# 这个 UML 类图列举了 collections.abc 中的几个类(超类在左边,箭头从子类指向超类,斜体名称代表抽象类和抽象方法)

# 通过记住这些类的共有特性,把可变和不可变序列或是容器与扁平序列的概念融会贯通,在探索并学习新的序列类型时,你会更加得心应手.