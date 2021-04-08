driving_age = eval(input("Каков минимальный возраст для получения прав в этой стране? "))
your_age = eval(input("Сколько вам лет? "))
if your_age >= driving_age:
    print ("Вы достаточно взрослый для получения прав!")
if your_age < driving_age:
    print("Извините, вы не сможете водить ещё", driving_age - your_age, "лет.")
