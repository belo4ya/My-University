import os
import random

MIN_IN = 300
MAX_IN = 911

header_in = "День,Поставка\n"
header_out = "День,Продажа\n"
row = "{d},{param1}\n"
for i in range(10):
    os.mkdir(f"Магазин{i + 1}")
    with open(f"Магазин{i + 1}/in.txt", "w", encoding="UTF-8") as f:
        f.write(header_in)
    with open(f"Магазин{i + 1}/out.txt", "w", encoding="UTF-8") as f:
        f.write(header_out)
    for d in range(7):
        with open(f"Магазин{i + 1}/in.txt", "a") as f:
            random_in = random.randint(MIN_IN, MAX_IN)
            f.write(row.format(d=d + 1, param1=random_in))
        with open(f"Магазин{i + 1}/out.txt", "a") as f:
            f.write(row.format(d=d + 1, param1=random.randint(MIN_IN, random_in)))
