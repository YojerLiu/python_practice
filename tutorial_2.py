# 列表
names = ['Amy', 'Bob', 'Cindy']
print(names)
print(names[0])
print('=========================')

# 修改列表中的元素
names[0] = 'Alex'
print(names)
names[1] = 'Beatles'
print(names)
print('======================')

# 往列表中添加元素
names.append('Dylan')
print(names)
# list.insert(index: 放在这个index之前的位置，element: 添加的元素)
names.insert(0, 'Eason')
print(names)
names.insert(1, 'FFF')
print(names)

# 使用del删除元素
del names[0]
print(names)
print('========================')

# 使用pop()删除列表末的元素
popped_name = names.pop()
print(popped_name)
print(names)
# 使用pop（）删除指定位置的元素
another_popped_name = names.pop(0)
print(another_popped_name)
print(names)
print('==========================')

# 根据元素的值来删除
# remove()方法只删掉第一个指定的值
names.append('Alex')
print(names)
names.remove('Alex')
print(names)
print('============================')

# 对列表进行永久排序
brands = ['bmw', 'audi', 'toyota', 'subaru']
brands.sort()
print(brands)
print('======================')

# 对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
print('======================')

# 对列表进行永久倒序
cars.reverse()
print(cars)

# 确定列表长度
print(len(cars))

# 负数索引
print(cars[-1])
print(cars[-2])
print('================================')

# 遍历列表
magicians = ['Alice', 'David', 'Caroline']
for e in magicians:
    print(e)
    print('This is ' + e)
print("=========================")

# 使用range(i, j)函数生成[i, i + 1, i + 2, ..., j - 1]. [i, j)
for value in range(1, 5):
    print(value)
# 使用range(i)生成一系列数字[0, i)
for value in range(3):
    print(value)
print()
# 指定range的步长，步长为2
for value in range(1, 11, 2):
    print(value)
print('==========================')

# 使用range创建数字列表
print(range(1, 10, 2))
numbers = list(range(1, 10, 2))
print(numbers)
print('=========================')
# 0, 1, 2
for index in range(len(magicians)):
    print(magicians[index])

# 找出列表中数字的最大值
digits = list(range(11))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析，将for循环和创建新元素的代码合成一行
results = [value**2 for value in range(11)]
print(results)

results1 = []
for value in range(11):
    results1.append(value**2)
print(results1)
print('==================================')

# 列表切片, 与range类似，在到达指定的第二个索引前面的元素后停止
bands = ['arctic monkeys', 'the wombats', 'deerhunter', 'the animals']
print(bands[1:4])
print(bands[0:2])
print(bands[:2]) # 没有指定第一个索引，将从列表头开始切片
print(bands[2:]) # 没有指定第二个索引，将一直切片到列表末
print(bands[-2:])
print(bands[-4:-2])
print('=======================')

# 遍历切片
for band in bands[1:4]:
    print(band)
print('=======================')

# 列表按引用复制
odds = [1, 3, 7]
my_odds = odds
print(my_odds)
odds.append(9)
print(odds)
print(my_odds)

# 列表按值复制
my_bands = ['Arctic Monkeys', 'B-52', 'Can']
another_bands = my_bands[:]
print(another_bands)
my_bands.append('Deerhunter')
print(my_bands)
print(another_bands)

# 元组 Tuple
dimensions = (10, 20, 30)
for e in dimensions:
    print(e)
dimensions = (20, 40, 60)
print(dimensions)
