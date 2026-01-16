from random import randint

number = randint(1, 100)
welcome_text = 'Угадайте число от 1 до 100'

#gegege

def main():
    while True:
        guess = int(input('Введите число: '))

        if guess < number:
            print('Ваше число меньше того, что загадано.')

        elif guess > number:
            print('Ваше число больше того, что загадано.')

        elif guess == number:
            break

main()


print('Отличная интуиция! Вы угадали число :)')
