import turtle
t = turtle.Pen()
# Запросить у пользователя количество сторон или окруностей, по умолчанию 6
number = int(turtle.numinput("Количество сторон или окружностей", "Сколько сторн или окружностей будет у фигуры?", 6))
# Спросить у пользователя, хочет ли он отобразить многоугольник или розетку
shape = turtle.textinput("Какую фигуру вы хотите?", "Введите 'м' для многоугольника или 'р' для розетки:")
for x in range(number):
    if shape == 'р':        # Пользователь выбрал розетку
        t.circle(100)
    else:                   # Многоугольник по умолчанию
        t.forward (150)
    t.left(360/number)