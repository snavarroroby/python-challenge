# Analysis 1: PyBank
#---------------------------------

import os
import csv

budget_data = os.path.join ('Resources', 'budget_data.csv')

profit_loss_diffs = []
highest_pl_diff = ["",0]
lowest_pl_diff = ["",10000000000000]


with open(budget_data) as csvfile_bank:

    csvreader_budget = csv.reader(csvfile_bank, delimiter = ',')

    budget_header = next(csvreader_budget)

    row1 = next(csvreader_budget)

    total_months = 1

    previous_plvalue = int(row1[1])

    total_plvalue = int(row1[1])


    for row in csvreader_budget:

        total_months = total_months + 1

        # print(total_plvalue)

        # print(row)

        # print (row[1])
        
        total_plvalue = total_plvalue + int(row[1])

        # print(total_plvalue)

        # print("*********")

        current_plvalue = int(row[1])

        difference_plvalue = current_plvalue - previous_plvalue

        profit_loss_diffs.append(difference_plvalue)

        previous_plvalue = current_plvalue

        if difference_plvalue >= int(highest_pl_diff[1]):
            highest_pl_diff[0] = row[0]
            highest_pl_diff[1] = difference_plvalue

        if difference_plvalue <= int(lowest_pl_diff[1]):
            lowest_pl_diff[0] = row[0]
            lowest_pl_diff[1] = difference_plvalue

    
       


average_pl = sum(profit_loss_diffs) / len(profit_loss_diffs)
average_pl_round = str(round(average_pl,2))


#----------------------Solution Activity 1----------------------------------
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f"Total: ${total_plvalue}")
print(f'Average Change: ${average_pl_round}')
print(f'Greatest Increase in Profits: {highest_pl_diff[0]}, ${highest_pl_diff[1]}')
print(f'Greatest Decrease in Profits: {lowest_pl_diff[0]}, ${lowest_pl_diff[1]}')





#-----------------------Second activity begins below----------------------------------------------------------

election_data = os.path.join('Resources', 'election_data.csv')


stockham_totvotes = 0
degette_totvotes = 0
doane_totvotes = 0
total_votes = 0

with open(election_data) as csvfile_election:

    csvreader_election = csv.reader(csvfile_election, delimiter = ',')

    header_row = next(csvreader_election)
    

    for row in csvreader_election:
        if row[2] == 'Charles Casper Stockham':
            stockham_totvotes = stockham_totvotes + 1
        
        if row[2] == 'Diana DeGette':
            degette_totvotes = degette_totvotes + 1

        if row[2] == 'Raymon Anthony Doane':
            doane_totvotes = doane_totvotes + 1

        total_votes = total_votes + 1

    # print(stockham_totvotes)
    # print(degette_totvotes)
    # print(doane_totvotes)
    # print(total_votes)

    stockham_pct = (stockham_totvotes / total_votes)*100
    degette_pct = (degette_totvotes / total_votes)*100
    doane_pct = (doane_totvotes / total_votes)*100

    # print(stockham_pct)
    # print(degette_pct)
    # print(doane_pct)

    stockham_pct_round = str(round(stockham_pct,3))
    degette_pct_round = str(round(degette_pct,3))
    doane_pct_round = str(round(doane_pct,3))

    # print(stockham_pct_round)
    # print(degette_pct_round)
    # print(doane_pct_round)

    #------Solution Activity 2---------------------------------
    print('----------------------------')
    print('                            ')
    print("Election Results")
    print('----------------------------')
    print(f'Total Votes: {total_votes}')
    print('----------------------------')
    print(f'Charles Casper Stockham: {stockham_pct_round}% ({stockham_totvotes})')
    print(f'Diana DeGette: {degette_pct_round}% ({degette_totvotes})')
    print(f'Raymon Anthony Doane: {doane_pct_round}% ({doane_totvotes})')
    print('----------------------------')
    print("Winner: Diana DeGette")
    print('----------------------------')

# Creating final output list with desired formatting for text file   

final_output=["Financial Analysis", "------------------", 
'Total Months: ' + str(total_months), 
'Total: ' + str(total_plvalue), 
'Average Change: ' +'$'+ str(average_pl_round),
'Greatest Increase in Profits: ' + str(highest_pl_diff[0]) +' '+ '($'+ str(highest_pl_diff[1])+')',
'Greatest Decrease in Profits: ' + str(lowest_pl_diff[0])+ ' ' +'($' +str(lowest_pl_diff[1])+')',
' ', ' ', '------------------', ' ', ' ', 
'Election Results', '------------------', 
'Total Votes: '+ str(total_votes), 
'Charles Casper Stockham: ' + str(stockham_pct_round)+'% ' + '('+ str(stockham_totvotes)+')',
'Diana DeGette: ' + str(degette_pct_round)+'% ' + '(' + str(degette_totvotes)+')',
'Raymon Anthony Doane: ' + str(doane_pct_round)+'% ' + '(' + str(doane_totvotes) + ')',
' ', '------------------', ' ',
'Winner:' ' ' "Diana DeGette",
'------------------']

with open('python_challenge_solution.txt', 'w') as final_answer:
    for line in final_output:
        final_answer.write(line)
        final_answer.write('\n')