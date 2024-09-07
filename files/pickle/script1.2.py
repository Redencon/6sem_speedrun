import pickle

with open('data1.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data)
print(next(data))
print(next(data))


with open('data2.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)

data("Hello")

with open('data3.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data())

with open('data4.pickle', 'rb') as f:
    # Версия протокола определяется автоматически,
    # нет необходимости явно указывать его.
    data = pickle.load(f)
print(data(2))
