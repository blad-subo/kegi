# Повтори 3 [Вперёд 39 Направо 90 Вперёд 48 Направо 90]
# Поднять хвост
# Вперёд 27 Направо 90 Вперёд 24 Налево 90
# Опустить хвост
# Повтори 3 [Вперёд 29 Направо 90 Назад 18 Направо 90]

from turtle import *
screensize(10000, 10000)
tracer(0)
lt(90)
m = 10

for i in range (3):
    fd(39 * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()

fd(27 * m)
rt(90)
fd(24 * m)
lt(90)

down()
for i in range (3):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)

for x in range(24, 43):
    for y in range(0, 13):
        teleport(x * m, y * m)
        dot(3,'red')

print(39 * 48 + 29 * 18 - (43 - 24 - 1) * (13 - 0 - 1))
update()
done()






update()
down()














