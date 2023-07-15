# import datetime
# g = datetime.datetime.utcnow()
# local_time = datetime.datetime.now()
# print(f"Гринвич: ", g)
# print(f"Местное время:", local_time)
#TODO task2
from datetime import datetime
d1 = datetime.strptime('2023-04-30')
d2 = datetime.strptime('2023-05-10')
d = d2 - d1
days = d.days
print(d)