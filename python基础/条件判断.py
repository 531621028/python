#注意不要少写了冒号:
age = 3
if age >= 18:
	print('you age is',age)
	print('adult')
else:
	print('you age is',age)
	print('teenager')
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

height1 = input('请输入你的身高，单位m：')
weight1 = input('请输入你的体重，单位kg：')
height = float(height1)
weight = float(weight1)
bmi = weight / (height*height)
if bmi < 18.5:
	print("过轻")
elif bmi < 25:
	print("正常")
elif bmi< 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('严重肥胖')