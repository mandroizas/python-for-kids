rainy = input("Как погодка? Идёт дождь? (д/н) ").lower()
cold = input("На улице холодно? (д/н) ").lower()
if (rainy == 'д' and cold == 'д'):
    print("Лучше наденьте плащ.")
elif (rainy == 'д' and cold != 'д'):
    print("Возьмите с собой зонт.")
elif (rainy != 'д' and cold == 'д'):
    print("Наденьте пальто: на улице холодно!")
elif (rainy != 'д' and cold != 'д'):
    print("Надевайте, что хотите: на улице прекрасно!")
