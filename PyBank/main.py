import pandas as pd
import os

bank_csv = "Resources/budget_data.csv"

bank_df = pd.read_csv(bank_csv)

num_months = bank_df["Date"].count

net_total = bank_df["Profit/Losses"].sum()

difference_in_value = bank_df["Profit/Losses"].diff()

bank_df["Difference"] = difference_in_value

total_of_diff = bank_df["Difference"].sum()

number_of_diff = bank_df["Difference"].count()

average_of_diff = total_of_diff / number_of_diff

average_of_diff = round(average_of_diff,2)

bank_df_descending = bank_df.sort_values("Difference", ascending=False)

bank_df_descending = bank_df_descending.reset_index(drop=True)

highest_increase_amount = bank_df_descending.iloc[0]["Difference"]

highest_increase_date = bank_df_descending.iloc[0]["Date"]

budget_increasing = bank_df.sort_values('Difference')

budget_increasing = budget_increasing.reset_index(drop=True)

highest_decrease_amount = budget_increasing.iloc[0]['Difference']

highest_decrease_date = budget_increasing.iloc[0]["Date"]

print("-----------------------------------")
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {num_months}")
print("Total: ${:,.2f}".format(net_total))
print("Average Change: ${:,.2f}".format(average_of_diff))
print("Greatest Increase in Profits: " + highest_increase_date +
      ", ${:,.2f}".format(highest_increase_amount))
print("Greatest Decrease in Profits: " + highest_decrease_date +
      ", ${:,.2f}".format(highest_decrease_amount))

with open("financial_results.txt", 'w') as file:

    file.write("-------------------------------------------------------\r\n")
    file.write("Financial Analysis\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(f"Total Months: {num_months}\r\n")
    file.write("Total: ${:,.2f}\r\n".format(net_total))
    file.write("Average Change: ${:,.2f}\r\n".format(average_of_diff))
    file.write("Greatest Increase in Profits: " + highest_increase_date +
               ", ${:,.2f}\r\n".format(highest_increase_amount))
    file.write("Greatest Decrease in Profits: " + highest_decrease_date +
               ", ${:,.2f}\r\n".format(highest_decrease_amount))