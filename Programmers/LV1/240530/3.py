# 2016년

import datetime

def solution(a, b):
    time = datetime.datetime(2016, a, b)
    return time.strftime("%A")[:3].upper()