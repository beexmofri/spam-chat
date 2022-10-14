import pyautogui
import time

print("t minus")

count = 10
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Fire in the hole!!!")

for i in range(0,int(100)):
	pyautogui.typewrite("p" + '\n')