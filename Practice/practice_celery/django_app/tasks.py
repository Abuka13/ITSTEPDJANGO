import random
import time
from celery import shared_task


@shared_task
def add(x = 2):
    res = []
    while x < 1000:
        time.sleep(0.03)
        res.append(x ** 2)# processing
    return res


@shared_task
def string(str='Hello, World!'):
    res = []
    x = 1
    while x < 100:
        time.sleep(0.3)
        res.append(str*x)
        x+=1
    return res

@shared_task
def send_mass_mail(recipients=None):
    if recipients is None:
        recipients = [f"admin{x}@mail.ru" for x in range(1, 1000)]
    res = []
    for i in recipients:
        # send
        time.sleep(0.03)  # processing
        res.append("success" if random.randint(0, 1) > 0 else "error")
    return res

