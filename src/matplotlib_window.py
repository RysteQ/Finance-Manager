import matplotlib.pyplot as plt
import numpy as np

days = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
offset = 0.75

# TODO
def BiggestNumberInWeekData(month_data):
    return 1000

    biggest_value = month_data[0][0][0]

    for week in range(len(week_data)):
        for day in range(7):
            for item in range(4):
                if biggest_value < week_data[week][day][item]:
                    biggest_value = week_data[week][day][item]
    
    return biggest_value

# TODO
def ExtractWeekValues(month_data):
    labels_and_data = {
        'Income': [0.0, 0.0, 0.0, 0.0, 0.0],
        'Savings': [0.0, 0.0, 0.0, 0.0, 0.0],
        'Debt': [0.0, 0.0, 0.0, 0.0, 0.0]
    }

    print(month_data)

    for i in range(5):
        total_income = 0

        for j in range(7):
            total_income += int(month_data[i][j])

        if i == 0:
            if total_income < 0:
                labels_and_data["Income"][i] = 0
                labels_and_data["Savings"][i] = 0
                labels_and_data["Debt"][i] = abs(total_income)
            else:
                labels_and_data["Income"][i] = total_income
                labels_and_data["Savings"][i] = 0
                labels_and_data["Debt"][i] = 0
        else:
            last_week_income = labels_and_data["Income"][i - 1]
            last_week_savings = labels_and_data["Savings"][i - 1]
            last_week_debt = labels_and_data["Debt"][i - 1]

            if total_income < 0:
                labels_and_data["Income"][i] = 0

                if total_income < last_week_savings:
                    labels_and_data["Savings"][i] -= total_income
                else:
                    labels_and_data["Savings"][i] -= 0
                    labels_and_data["Debt"] = abs(total_income - last_week_savings)
            else:
                if total_income < last_week_debt:
                    labels_and_data["Income"][i] = 0
                    labels_and_data["Savings"][i] = last_week_savings
                    labels_and_data["Debt"][i] = abs(total_income - last_week_debt)
                else:
                    labels_and_data["Income"][i] = abs(total_income - last_week_debt)
                    labels_and_data["Savings"][i] = abs(total_income - last_week_debt)
                    labels_and_data["Debt"][i] = 0

    print(labels_and_data)

    return labels_and_data

def DisplayGraph(month_data):
    figure, axes = plt.subplots(layout = "constrained")

    values = ExtractWeekValues(month_data)

    axes.set_title("Week " + str(week_number))
    axes.set_ylabel("Euros")
    axes.set_ylim(0, BiggestNumberInWeekData())
    axes.set_xticks(np.arange(len(days)) + offset, days)

    plt.title("Week " + str(week_number))
    plt.show()