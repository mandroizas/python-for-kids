import turtle
t = turtle.Pen()
turtle.bgcolor("yellow")
#Попросить пользователя задать кол-во кругов в розетке,
#по умолчанию 6
number_of_circles = int(turtle.numinput("Количество окружностей", "Сколько окружностей в вашей розетке?", 6))
for x in range(number_of_circles):
    t.circle(100)
    t.left(360/number_of_circles)
print()

