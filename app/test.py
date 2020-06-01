import tasks
from time import sleep

print("add 3+5")
ret = tasks.add.delay(3,5)
print("Task ID:")
print(ret)
sleep(10)
print(ret.status)
