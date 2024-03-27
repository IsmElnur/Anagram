import random

WORDS = ('компьютер',
		 'авторизация',
		 'браузер',
		 'транслятор',
		 'программа',
		 'утилита',
		 'модератор')

word = random.choice(WORDS)
correct = word
anagramma = ''
while word:
	pos = random.randrange(len(word))
	anagramma += word[pos]
	word = word[:pos] + word[pos + 1:]

print('''<<Игра АНАГРАММА>>''')
input('Нажмите Enter, чтобы начать.')
print('Вот анаграмма:', anagramma.upper())

version = input('Нужна подсказка? (да/нет) При выборе отказа не будет подсказок.\n')
if version == 'да':
    print('Слово начинается так:', correct[:1], '...')
else:
	print('Отгадайте!')

answer = input('Напишите слово и нажмите Enter, чтобы проверить ваш ответ:\n')
if answer != correct:
	answer = input('Неправильно! Попытайтесь отгадать (нажмите "да")\n')

	if version == 'да':
	    print('Слово продолжается так:', correct[:2], '...')
	answer = input('Отгадайте ещё раз и нажмите на Enter!\n')

if answer != correct:
	answer = input('Неверно! Попытайтесь отгадать в последний раз (нажмите "да")\n')
	
	if version != 'нет':
		print('Продолжаем:', correct[:3], '...')
	answer = input('Отгадайте ещё раз!\n')
	
if answer == correct:
	print('Молодец!')
else:
	print('К сожалению, Вы не угадали...')

print('Спасибо за игру!')
input('Нажмите Enter, чтобы выйти.')
print('')
