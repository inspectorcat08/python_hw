a = int(input('Твой возраст: '))
if 0<a<=9:
	print('Ребенок')
elif 10<=a<15:
	print('Подросток')
elif 15<=a<30:
	print('Юный')
elif 30<=a<50:
	print('Взрослый')
else:
	print('Старый')