import random


for _ in range(10):
    print(
        f'{round(random.uniform(-1000, 1000), 2)}, {round(random.uniform(-1000, 1000), 2)}'
    )