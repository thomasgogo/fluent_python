# 用 bisect 来管理已排序的序列
# bisect 模块包含两个主要函数,bisect 和 insort,两个函数都利用二分查找算法在有序序列中查找或插入元素.

# 用bisect来搜索
# bisect(haystack, needle)在 haystack(干草堆)里搜索 needle(针)的位置,该位置满足的条件是,把 needle 插入这个位置之后,haystack 还能
# 保持升序.也就是再说这个函数返回的位置前面的值,都小于或者等于 needle 的值.其中 haystack 必须是一个有序的序列.你可以先用 bisect(haystack, needle)
# 查找位置 index,再用 haystack.insert(index, needle)来插入新值.但你也可以用 insort 来一步到位,并且后者的速度更快一些.

# 式列 2-17 利用几个精心挑选的 needle,向我们展示了 bisect 返回的不同位置值
# 在有序序列中用 bisect 查找某个元素的插入值

import bisect
import sys

haystack = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
needles = [0,1,2,5,8,10,22,23,29,30,31]

row_fat = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(needles):
        position = bisect_fn(haystack, needle)
        offset = position * '  |'
        print(row_fat.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right

    print('demo: ', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in haystack))
    demo(bisect_fn)

    bisect_fn = bisect.bisect_left
    demo(bisect_fn)

# bisect的表现可以从两个方面来调教,首先可以用它的两个可选参数--lo 和 hi 来缩小搜寻的范围.lo 的默认值是 0,hi 的默认值是序列的长度,
# 即 len()作用于该序列的返回值.

# 其次, bisect 函数其实是 bisect_right 函数的别名,后者还有一个姊妹函数叫 bisect_left.他们的区别在于,bisect_left 返回的插入位置是原
# 序列中跟被插入元素相等的元素的位置,也就是新元素会被放置于它相等的元素的前面,而 bisect_right 返回的则是跟它相等的元素之后的位置.

# bisect 可以用来建立一个用数字作为索引的查询表格
# 实例2-18 根据一个分数,找到它所对应的成绩

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i= bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

# 2.8.2 用 bisect.insort 插入新元素
# 排序很耗时,因此在得到一个有序序列之后,我们最好能够能够保持它的有序.bisect.insort 就是为了这个而存在的
# insort(seq, item)把变量 item 插入到序列 seq 中,并能保持 seq 的升序顺序.


import bisect
import random


size = 7

random.seed(1729)

my_list = []
for i in range(size):
    new_item = random.randrange(size * 2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)


# insort 跟 bisect 一样,有 lo 和 hi 两个可选参数用来控制查找的范围.它也有个变体叫 insert_left,这个变体在背后用的是 bisect_left.

# bisect 不仅仅是对列表或者元组有效,还可以应用于几乎所有的序列类型