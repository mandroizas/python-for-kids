import turtle # Настройка графики Turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "brown", "gray", "pink"]
family = [] # Сщздать пустой список для имён родственников
# Запросить первое имя
name = turtle.textinput("Моя семья", " Введите имя или нажмите [ENTER], чтобы выйти:")
# Продолжить запрашивать имена
while name!= "":
    # Добавить имя у пустому списку
    family.append(name)
    # Запросить ещё одно имя или выйти
    name = turtle.textinput("Моя семья", " Введите имя или нажмите [ENTER], чтобы выйти:")
# Нарисовать на экране спараль из имён
for x in range(100):
    t.pencolor(colors[x%len(family)]) # Переключение цветов
    t.penup() # Не рисовать обычные прямые линии
    t.forward(x*4) # Просто передвинуть черепашку по экрану
    t.pendown() # Нарисовать следующее имя родственника
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold"))
    t.left(360/len(family) + 2) # Повернуть влево
input()
