# 数据结构: 列表

fruits = ['apple', 'banana', 'cherry']

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# [0] 下标从0开始表示的是偏移量 1表示偏移一位 所以[1]是第二位
print(states_of_america[0])

# [-1] 倒数第一个元素
print(states_of_america[-1])

# 修改指定位置的元素内容
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# 追加元素
states_of_america.append('Angelaland')
print(states_of_america[-1])

# 追加列表元素
states_of_america.extend(['quartz land', 'orange land'])
print(states_of_america)
