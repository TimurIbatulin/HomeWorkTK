# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# import random
# candy = int(2021)
# print('Мы начинаем эпичную битву! \n Теперь твои джинсы станут тебе малы! \n (при поддержке асоциации стоматологов России)')
# test = int(input('Ты одинок? Хочешь с кем-то поиграть? Нажми "1" и я тебя развлеку :-) - '))
# if test != 1:
#     fortunaplayer = str(input('Сейчас мы разыграем право первого хода! \n Необходимо ввестии какую сторону монетки вы выбрали орел/решка - '))
#     fortuna = ['орел', 'решка']
#     index = random.randint(0, len(fortuna) -1)
#     print(fortuna[index])
#     if fortunaplayer == fortuna:
#         print('Фортуна на твоей стороне, твой ход первый')
#         m = 'Игрок_1'
#         n = 'Игрок_2'
#     else:
#         print('Может не будешь играть, тебе уже не везет?')
#         m = 'Игрок_2'
#         n = 'Игрок_1'
#     print(f'Итак, на столе лежит {candy} конфета, каждый игрок может взять на свое усмотрение от 1 до 28 конфет. \n Победит тот кто заберет последние конфеты!')
#     for index in range(candy):
#         print(f'{index + 1} ход')
#         if candy > 0:
#             candy1 = int(input(f'{m}, сколько конфет ты возьмешь? '))
#             while (candy1 < 1) or (candy1 >28) or (candy1 > candy):
#                 if candy1 > 28:
#                     candy1 = int(input(f'{m}, бери ношу по себе, что бы не падать при ходьбе! слишком много, можно взять от 1 до 28. еще раз - '))
#                 elif candy1 < 1:
#                     candy1 = int(input(f'{m}, в некоторых странах за это тебе отрежут уши! слишком мало,  можно взять от 1 до 28. еще раз -  '))
#                 elif candy1 > candy:
#                     candy1 = int(input(f'{m}, нельзя взять больше чем осталось -  '))     
#         candy = candy - candy1
#         print(f'Конфет осталось - {candy} шт.')
#         if candy == 0:
#             print(f'{m}, ты победил!!!')
#             break
#         if candy > 0:
#             candy2 = int(input(f'{n}, сколько конфет ты возьмешь? '))
#             while (candy2 < 1) or (candy2 >28) or (candy2 > candy):
#                 if candy2 > 28:
#                     candy2 = int(input(f'{n}, бери ношу по себе, что бы не падать при ходьбе! слишком много, можно взять от 1 до 28. еще раз - '))
#                 elif candy2 < 1:
#                     candy2 = int(input(f'{n}, в некоторых странах за это тебе отрежут уши! слишком мало,  можно взять от 1 до 28. еще раз -  '))
#                 elif candy2 > candy:
#                     candy2 = int(input(f'{n}, нельзя взять больше чем осталось -  '))     
#         candy = candy - candy2
#         print(f'Конфет осталось - {candy} шт.')
#         if candy == 0:
#             print(f'{n}, ты победил!!!')
#             break
# if test == 1:
#     print('Ну что же, ходи первый, тебе это не поможет')
#     m = 'Игрок_1'
#     n = 'Чак Норис'
#     print(f'Итак, на столе лежит {candy} конфет, ты и Чак Норис можете на свое усмотрение взять от 1 до 28 конфет. \n Победит тот кто заберет последние конфеты!')
#     for index in range(candy):
#         print(f'{index + 1} ход')
#         if candy > 0:
#             candy1 = int(input(f'{m}, сколько конфет ты возьмешь? '))
#             while (candy1 < 1) or (candy1 >28) or (candy1 > candy):
#                 if candy1 > 28:
#                     candy1 = int(input(f'{m}, бери ношу по себе, что бы не падать при ходьбе! слишком много, можно взять от 1 до 28. еще раз - '))
#                 elif candy1 < 1:
#                     candy1 = int(input(f'{m}, в некоторых странах за это тебе отрежут уши! слишком мало,  можно взять от 1 до 28. еще раз -  '))
#                 elif candy1 > candy:
#                     candy1 = int(input(f'{m}, нельзя взять больше чем осталось -  '))     
#         candy = candy - candy1
#         print(f'Конфет осталось - {candy} шт.')
#         if candy == 0:
#             print(f'{m}, ты победил!!!')
#             break
#         if candy > 0:
#             candy2 = candy%28 - 1
#             if candy < 100 and candy > 56:
#                 candy2 = (candy - 28) % 28 - 2
#             if candy < 56 and candy > 29:
#                 candy2 = (candy - 28) - 1
#             if candy2 < 1:
#                 candy2 = 7
#             if candy < 28:
#                 candy2 = candy     
#         candy = candy - candy2
#         print(f'{n} взял {candy2} конфет, теперь их осталось - {candy} шт.')
#         if candy == 0:
#             print(f'{n}, ты победил!!!')
#             break

# from tkinter import *
# from tkinter import ttk
# import random
# root = Tk()
# root.title('КОНФЕТНЫЕ БАТАЛИИ')
# root.geometry('2000x1000')
# root.update_idletasks()
# l = Label(text='Мы начинаем эпичную битву!  Теперь твои джинсы станут тебе малы! \n (При поддержке асоциации стоматологов России)', font=('Arial Bold', 25))
# l.pack()
# l1 = Label(text='Сейчас мы разыграем право первого хода! ВЫБИРАЙ:', font=('Arial Bold', 30))
# l1.pack()
# fort = 0
# fortuna = ['орел', 'решка']

# def take():
#     global fort
#     fort = combo.get()
    

# combo = ttk.Combobox(values=fortuna)

# combo.pack()
# ttk.Button(text='Выбрать', command=take).pack()

# # z = take()



# print(fort)




# index = random.randint(0, len(fortuna) -1)
# print(fortuna[index])
# print(f'get =', fort)
# print(fort)
# if fortunaplayer == fortuna:
#     m = 'Игрок_1'
#     n = 'Игрок_2'


# b100 = Button(text='ОРЕЛ', font=('Arial Bold', 15))
# b100.grid(column = 1, row=4)
# b200 = Button(text='РЕШКА', font=('Arial Bold', 15))
# b200.grid(column = 8, row=4)
# def clicked():





# svits = int(2021)
# # print('Мы начинаем эпичную битву! \n Теперь твои джинсы станут тебе малы! \n При поддержке асоциации стоматологов России')
# fortunaplayer = str(input('Сейчас мы разыграем право первого хода! \n Необходимо ввестии какую сторону монетки вы выбрали орел/решка - '))

# fortuna = ['орел', 'решка']
# index = random.randint(0, len(fortuna) -1)
# print(fortuna[index])
# if fortunaplayer == fortuna:
#     m = 'Игрок_1'
#     n = 'Игрок_2'



# player1 = int(input('За каждый Ваш ход вы можете взять от 1 до 28 конфет. Сколько конфет вы хотите взять? - '))



# root.protocol('WM_DELETE_WINDOW', finish)
# 1
#root.mainloop()




# Создайте программу для игры в ""Крестики-нолики"".
# list = [[1, '|', 2, '|', 3], ['-','-','-','-','-'], [4, '|', 5, '|', 6], ['-','-','-','-','-'], [7, '|', 8, '|', 9]]
# # list.append()

# for i1 in range(len(list)):
#     for i2 in range(len(list[i1])):
#         print(list[i1][i2], end='')
#     print('')
#     listBUF = []
# print('Перед Вами поле из 9 ячеек, для того, чтобы поставить "Х" или "О" нужно указать номер ячейки. \n Ну, что поехали?')
# for index in range(9):
#     cell = input('Введите номер ячейки для "Х" - ')
#     if cell == str(1):
#         for index1 in range(3):
#             w = index1 + 1
#             listBUF.append(list[[0][w]])
#         list[[0][0]] = 'X'
#         for index11 in range(3):
#             list[[0][index11 + 1]].append(listBUF[index11])
#     for i1 in range(len(list)):
#         for i2 in range(len(list[i1])):
#             print(list[i1][i2], end='')
#         print('')
    
from tkinter import *
import random, time

def stop_game():
    global game_left
    for item in game_left:
        buttons[item].config(bg='white', state = 'disabled')

def win(n):
    global game
    if game[0] == n and game[1] == n and game[2] == n or game[3] == n and game[4] == n and game[5] == n or\
        game[6] == n and game[7] == n and game[8] == n or game[0] == n and game[3] == n and game[6] == n or\
        game[1] == n and game[4] == n and game[7] == n or game[2] == n and game[5] == n and game[8] == n or\
        game[0] == n and game[4] == n and game[8] == n or game[2] == n and game[4] == n and game[6] == n:
        return True


def push(b):
    global game
    global game_left
    global turn
    game[b] = 'X'
    buttons[b].config(text = 'X', bg = 'white', state = 'disabled')
    game_left.remove(b)
    if b == 4 and turn == 0:
        t = random.choice(game_left)
    elif b != 4 and turn == 0:       
        t = 4
    if turn > 0:
            t = 8 - b
    if t not in game_left:
        try:
            t = random.choice(game_left)
        except IndexError:
            label['text'] = 'Игра окончена!'
            stop_game()
        
    
    game[t] = '0'
    time.sleep(0.5)
    buttons[t].config(text = '0', bg = 'white', state = 'disabled')
    if win('X'):
        label['text'] = 'Вы победили!'
        stop_game()
    elif win('0'):
        label['text'] = 'Вы проиграли!'
        stop_game()
    else:
        if (len(game_left) > 1):
            game_left.remove(t)
        else:
            label['text'] = 'Игра окончена!'
        turn += 1



game = [None] * 9
game_left = list(range(9))
turn = 0

window = Tk()
label = Label(width=20, text = 'Игра крестики-нолики', font=('Arial', 20, 'bold'))
buttons = [Button(width=5, height=3, font=('Arial', 28, 'bold'), bg = 'blue', command = lambda x = i: push(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3)
row = 2; col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0




window.mainloop()











# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.