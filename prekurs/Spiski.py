my_list = ['as', 'hh', 2, 7, 8, 8, 8, 9, 9, 0]
z = 0
while z < len(my_list):
    print(my_list[z])
    z = z+1
my_list.clear()
print(my_list)
my_list.insert(0, 'test')
my_list.append('222')
my_list.insert(0, 'prime')
print(my_list)
ind = my_list.index('222')
my_list.sort()
print(my_list)
