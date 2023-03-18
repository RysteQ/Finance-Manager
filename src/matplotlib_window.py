import matplotlib.pyplot as plt
import numpy as np

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
offset = 0.75

week_number = 0
week_data = []

# TODO
def SetWeekData(week_data_to_set):
    weed_data = week_data_to_set

def SetWeekNumber(week_number_to_set):
    if week_number <= 5:
        week_number = week_number_to_set
    else:
        week_number_to_set = 1

# TODO
def BiggestNumberInWeekData():
    return 1000

    biggest_value = week_data[0][0][0]

    for week in range(len(week_data)):
        for day in range(7):
            for item in range(4):
                if biggest_value < week_data[week][day][item]:
                    biggest_value = week_data[week][day][item]
    
    return biggest_value

# TODO
def ExtractWeekValues():
    labels_and_data = {
        'Income': (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        'Expenses': (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        'Savings': (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        'Debt': (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    }

    return labels_and_data

def DisplayGraph():
    figure, axes = plt.subplots(layout = "constrained")

    values = ExtractWeekValues()

    axes.set_title("Week " + str(week_number))
    axes.set_ylabel("Euros")
    axes.set_ylim(0, BiggestNumberInWeekData())
    axes.set_xticks(np.arange(len(days)) + offset, days)

    plt.title("Week " + str(week_number))
    plt.show()