#1.Числа фибоначи*
def Fibonacci(f1):
    f2 = 1
    print(f1)
    while f2 < 1000:
        print(f2)
        f1, f2 = f2, f1 + f2

Fibonacci(1)

# f1, f2 = 1, 1
#     print(f1)
#     while f2 < 1000:
#         print(f2)
#         f1, f2 = f2, f1+f2

"""3.11"""
#Равнозначные "выражения"
zoo_pets = ['horse', 'lion', 'wolf', 'monkey', 'snake']
for i, animal in enumerate(zoo_pets):
    print(i, animal)


for i in range(len(zoo_pets)):
    animal = zoo_pets[0]
    print(i, animal)
#Распаковка словаря метод итемс для словаря, значения все под ключем и с ключем, а есть метод .values() он не возвращает
# ключ, только значения
zoo_pets_mass = {
    'horse': 400,
    'lion': 300,
    'wolf': 250,
    'monkey': 50,
    'snake': 7
}
total_mass = 0
for animal, mass in zoo_pets_mass.items():
    print(animal, mass)
    total_mass += mass
print('Общая масса животных', total_mass)
