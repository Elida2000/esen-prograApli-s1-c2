# lista
numberList = []
print(numberList)

numberList = [1, 2, 3, 4]
print(numberList)
print(len(numberList))
numberList.append(5)
print(numberList)

numberList[0] = 0
print(numberList)

for number in numberList:
    print(number)

fruitList = ["apple", "strawberry"]
for fruit in fruitList:
    print(fruit)

# ejercicio
numberList = range(1, 20)
# sacar la suma de todos los numeros
result = 0
for number in numberList:
    result += number
print(result)

print(type(numberList))


# tuplas
dataTuple = (1, "java", 1981)
print(type(dataTuple))

print(dataTuple[1])

# los elementos de una tupla pueden ser asignados
id, language, year = dataTuple
print(id)
print(year)

for data in dataTuple:
    print(data)

# modificar una tupla
# convertir la lista a tupla
dataList = list(dataTuple)
dataList.append("bal")
dataTuple = tuple(dataList)
id, language, year, developer = dataTuple

for data in dataTuple:
    print(data)


# ejercicio
dataTuple = (1, "dragonball", "japon", ("goku", "krilin"))
# id, serie, pais, personajes, listar los personajes
id, serie, pais, personajes = dataTuple
print(id)
print(serie)
print(pais)
print("personajes-->")

for personaje in personajes:
    print("-", personaje)


# set
# no es ordenado y tampoco puede ser modificado
# delimitar informacion para que solo se repita una vez
dataSet = {1, 2, 3, 4, 5, 6, 6, 7}
print(dataSet)

print(1 in dataSet)
print(9 in dataSet)

for data in dataSet:
    print(data)

# agregar un elemento
dataSet.add(10)
print(dataSet)



# diccionario
# no nos permite tener duplicados

dataDict = {"id":1, "name": "bal", "age": 23}
print(dataDict["id"])
print(dataDict.keys())

for key in dataDict.keys():
    print(dataDict[key])

for value in dataDict.values():
    print(value)

dataDict["name"] = "balx"
print(dataDict)

for key, value in dataDict.items():
    print(key, value)

print(type(dataDict.items()))

# agregar elementos
dataDict["year"] = 1981
for key, value in dataDict.items():
    print(key, value)


# class
# estructura que permite guardar informacion dentro de ella
# permite colocar metodos

# representar una suma en un formato digital
# 2 + 3 = 5
# input: num1, num2 [clase tiene variables]
# operacion: + [metodos]
# result: result [metodos retornan resultados]

class Operation:
    def __init__(self, pNum1, pNum2):
        self.num1 = pNum1
        self.num2 = pNum2

    def add(self):
        return self.num1 + self.num2

oper = Operation(2, 3)
result = oper.add()
print(result)


