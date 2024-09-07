import pickle

# Коллекция сериализуемых объектов
data = {
    'a': [1, 2.0, 3, 4+6j, float("nan")],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# Сериализация словаря data с использованием
# версии протокола по умолчанию.
print(pickle.dumps(data))

with open('data.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


# with open("files/write.txt") as f:
#     with open('data1.pickle', "wb") as f2:
#         pickle.dump(f, f2, pickle.HIGHEST_PROTOCOL)

l = [1, 2, 3]
it = iter(l)

with open('data1.pickle', "wb") as f2:
    pickle.dump(it, f2, pickle.HIGHEST_PROTOCOL)

with open('data2.pickle', "wb") as f2:
    pickle.dump(print, f2, pickle.HIGHEST_PROTOCOL)

from collections import deque

with open('data3.pickle', "wb") as f2:
    pickle.dump(deque, f2, pickle.HIGHEST_PROTOCOL)

def sq(x):
    return x*x

with open('data4.pickle', "wb") as f2:
    pickle.dump(sq, f2, pickle.HIGHEST_PROTOCOL)
