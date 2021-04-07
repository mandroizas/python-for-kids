answer = input("Хотите увидеть спираль? д/н:")
if answer == 'д':
    print("Работаем...")
    import turtle
    t = turtle.Pen()
    t.speed(0)
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
print("Ну вот, всё готово!")
    
