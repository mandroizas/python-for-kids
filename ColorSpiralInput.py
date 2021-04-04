import turtle # Настройка графики turtle

t = turtle.Pen()
turtle.bgcolor("black")
# Настройка списка из любых 8 действительных имен цветов
# Python
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
sides = int(turtle.numinput("Сколько сторон", "Сколько сторон вы хотите (1-8)?", 4, 1, 8))
# Запросить у пользователя количества сторон
# количество по умолчянию - 4
for x in range(360):
    t.pencolor(colors[x % sides]) # Использовать правильное количество цветов
    t.forward(x * 3 / sides + x) # Изменить размер в соответствии с кол-вом сторон
    t.left(360 / sides + 1) # Поворот на 360 градусов количество сторон + 1
    t.width(x * sides / 200) # Увеличить размер ручки по мере передвежения во внешнюю сторону
