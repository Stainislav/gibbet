#!/usr/bin/env python3

import random
import turtle
import sys

# PEP8

# функция поднимает курсор и переносит его в заданное место
def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# функция рисует прямую линию по заданным точкам
def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

# функция стирает надпись
def erase(x, y):
    gotoxy(x, y)
    turtle.color('white')

    turtle.begin_fill()
    turtle.begin_poly()

    turtle.fd(700)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)

    turtle.fd(700)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)

    turtle.end_poly()
    turtle.end_fill()

# ускорим нашу черепашку
turtle.speed(0)

# случайным образом определим число, которое будет угадывать пользователь 
x = random.randint(1, 100)

# список для координат
coord_list = []

coord = open('coordinat.txt')

# преобразуем список со строками в список с числами, уберём перевод на следующую строку
for line in coord:
    line = line.strip().split(',')
    nums = []
    for n in line:
        nums.append(int(n))
        
    coord_list.append(nums)

while True:
    # спросим у пользователя, хочет ли он играть
    answer = turtle.textinput("Играть?", "y/n")

    # если пользователь не хочет играть, выходим из программы
    if answer == 'n':
        sys.exit()
    # если пользователь хочет играть, прерываем бесконечный цикл
    if answer == 'y':
        break

# счётчик кол-ва предоставлямых пользователю ошибочных попыток
try_count = 0
 
# запускаем бесконечный цикл игры
while True:
    number = turtle.numinput("Угадайте","Число", 0, 0 , 100)   
    n = 0
    # если пользователь угадал число, поздравляем его
    if number == x:
        erase(-150, 200)

        turtle.color('green')
        gotoxy(-150, 200)
        turtle.write("Ура! Вы победили!", 
               font=("Arial", 28, "normal"))
        break

    # если пользователь не угадал число сообщаем ему в какую сторону думать
    else:
        # стираем с экрана всё, что было написано до этого
        erase(-150, 200)

        turtle.color('red')
        gotoxy(-150, 200)
 
        if number > x:
            turtle.write("Неверно! Число должно быть меньше!",
                font=("Arial", 28, "normal"))
        else:
            turtle.write("Неверно! Число должно быть больше!",
                font=("Arial", 28, "normal"))
        
        # обновляем счётчик ходов
        line_index = 0
        try_count += 1
        line_index = try_count - 1
        
        turtle.color('black')

        # пошагово рисуем виселицу: на пятом шаге рисуем голову, в остальных случаях берём части виселицы из списка
        if line_index == 4:
            gotoxy(-100, 0)
            turtle.circle(20)
        else:
            draw_line(*coord_list[line_index])

        # если пользователь не угадал число за 10 попыток, сообщаем ему, что он проиграл
        if try_count == 10:
            # стираем с экрана всё, что было написано до этого
            erase(-150, 200)

            turtle.color('red')
            gotoxy(-20, 230)
            turtle.write("Вы проиграли!",
                font=("Arial", 44, "normal"))
            break
 
# ставим input, чтобы окно графического приложения не закрывалось
input('Нажмите любую клавишу...')


