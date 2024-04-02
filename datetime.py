from datetime import datetime


current_date = datetime.now().date()

current_time = datetime.now().time()


print(current_date)

print(current_time.strftime('%H:%M'))
