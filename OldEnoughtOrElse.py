driving_age = eval(input("Какаой минимальный возраст для получения прав в вашей стране? "))
your_age = eval(input("Сколько вам лет? "))
if your_age >= driving_age:
    print("Вы достаточно взрослый для получения прав!")
else:
    print("Извините, вы не сможети водить ещё", driving_age - your_age, "лет.")
