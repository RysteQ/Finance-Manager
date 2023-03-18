import matplotlib.pyplot as plt
import numpy as np

week_number = 0
weed_data = []

# TODO
def SetWeekData(week_data_to_set):
    weed_data = week_data_to_set

def SetWeekNumber(week_number_to_set):
    if week_number <= 5:
        week_number = week_number_to_set
    else:
        week_number_to_set = 1

def DisplayGraph():
    plt.title("Week " + str(week_number))
    plt.show()