# Reproduce the bug
# 由于 randint 范围 1 - 6，会造成数组越界，应该将范围调整至 0 - 5。
# 需要将 randint(1, 6) 改为 randint(0, 5)
from random import randint
dice_imgs = ["①","②","③","④","⑤","⑥"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])