from datetime import datetime,date
from math import ceil
import numpy as np

def generateUUID(table,id):
    print(f"{table}-{id}")
    return f"{table}-{id}"

def calculateDuration(start_date, end_date):
    delta = np.busday_count(np.datetime64(start_date),np.datetime64(end_date))
    print(delta)
    return delta * 8

def calculateEndDate(start_date, duration):
    end_date = np.busday_offset(np.datetime64(start_date),ceil(duration / 8) ,roll="forward")
    return str(end_date)