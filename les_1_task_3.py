# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
char1 = input('введите букву1')
pos1 = ord(char1) - 97 + 1
print(f'введенная буква стоит на {pos1} позиции в алфавите')
char2 = input('введите букву2')
pos2 = ord(char2) - 97 + 1
print(f'введенная буква стоит на {pos2} позиции в алфавите')
pos_count = abs(pos1 - pos2) - 1
print(f'между введенными буквами {pos_count} буквы')