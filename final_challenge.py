temperatures = ["Label", 32, 50, 77, 104]


for temp in temperatures[1:]:

    map(int, temperatures[1:])
    celsius = map(lambda temp: (temp - 32) * 5.0 / 9.0, temperatures[1:])


print(list(celsius))







    