#狗狗年紀vs人類
age = int(input('請輸入你家狗狗的年齡:'))
print("")
if age == 0:
	print('你是在逗我吧？')
elif age == 1:
	print('相當於人14歲')
elif age == 2:
	print('相當於人22歲')
elif age > 2:
	human = 22 + (age -2)*5
	print('對應人類年齡為:', human)
input('點擊 enter 鍵退出')	
