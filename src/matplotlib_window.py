import matplotlib.pyplot as plt
import numpy as np

def ExtractWeekValues(month_data):
    labels_and_data = {
        'Income': [0.0, 0.0, 0.0, 0.0, 0.0],
        'Savings': [0.0, 0.0, 0.0, 0.0, 0.0],
        'Debt': [0.0, 0.0, 0.0, 0.0, 0.0]
    }

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
                labels_and_data["Savings"][i] = total_income
                labels_and_data["Debt"][i] = 0
        else:
            last_week_savings = labels_and_data["Savings"][i - 1]
            last_week_debt = labels_and_data["Debt"][i - 1]

            if total_income < 0:
                labels_and_data["Income"][i] = 0

                if abs(total_income) < last_week_savings:
                    # plus since the number is negative to begin with
                    labels_and_data["Savings"][i] = abs(last_week_savings + total_income)
                else:
                    labels_and_data["Savings"][i] = 0
                    labels_and_data["Debt"][i] = abs(total_income + last_week_savings) + last_week_debt
            else:
                if total_income < last_week_debt:
                    labels_and_data["Income"][i] = 0
                    labels_and_data["Savings"][i] = last_week_savings
                    labels_and_data["Debt"][i] = abs(total_income - last_week_debt)
                else:
                    labels_and_data["Income"][i] = abs(total_income - last_week_debt)
                    labels_and_data["Savings"][i] = abs(total_income - last_week_debt) + last_week_savings
                    labels_and_data["Debt"][i] = 0

    return labels_and_data

def DisplayGraph(month_data):
    weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
    width = 0.25
    multiplier = 0

    figure, axes = plt.subplots(layout = "constrained")

    for name, value in ExtractWeekValues(month_data).items():
        rectangle = axes.bar(np.arange(len(weeks)) + width * multiplier, value, width, label = name)
        axes.bar_label(rectangle, padding = 5)
        multiplier += 1

    axes.set_title("Month")
    axes.set_ylabel("Euros")
    axes.legend(loc = "upper right", ncols = 3)
    axes.set_xticks(np.arange(len(weeks)) + width, weeks)

    plt.title("Month Data")
    plt.show()