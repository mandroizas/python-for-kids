import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
# Запросить кол-во сторон, по умолчанию 4, мин 2, макс 6
sides = int(turtle.numinput("Количество сторон", "Сколько будет сторон у вашей спирали спиралей? (2-6) ", 4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
# "Внешний" цикл спирали
for m in range(100):
    t.forward(m*4)
    position = t.position() # Запомнить этот угол спирали
    heading = t.heading() # Запомнить направление следования
    print(position, heading)
    # "Внутренний" цикл спирали
    # Отрисовывает маленькую спираль в каждом углу большой
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    t.setx(position[0]) # Вернуться в позицию x большой спирали
    t.sety(position[1]) # Вернуться в позицию y большой спирали
    t.setheading(heading) # Указать направление большой спирали
    t.left(360/sides + 2) # Нацелиться на следующую точку большой спирали
