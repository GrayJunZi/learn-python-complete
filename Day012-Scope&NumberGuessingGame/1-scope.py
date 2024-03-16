enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside funciton: {enemies}")

# Local Scope (局部作用域)
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# 以下代码将报错，因为 potion_strength 是在 drink_potion函数中定义的，属于该函数的局部变量
# print(potion_strength) 


# Global Scope (全局作用域)
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)


# Block Scope (块级作用域)
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope (修改全局作用域)
enemies_global = "Skeleton"

def increase_enemies_global():
    global enemies_global 
    enemies_global = "Zombie"
    print(f"enemies_global inside function:{enemies_global}")

increase_enemies_global()
print(f"enemies_global outside funciton: {enemies_global}")