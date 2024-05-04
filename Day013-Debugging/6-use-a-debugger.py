# 由于 b_list.append(new_item) 没有进行缩进
# 是写在了for循环的外边，所以只会追加最后一个 new_item 的值
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

