import csv
import os

csvpath = os.path.join('..', 'Resources','election_data.csv')

candidates = []
votes = []
votes_percent = []
total_votes = 0
winner = 0
winner_counts = 0

def fixPercent(num):
    num = "{:.3%}".format(num)
    return num


with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(1)
        else:
            candidate_index = candidates.index(row[2])
            votes[candidate_index] += 1
    for i in range (len(votes)):
        votes_percent.append(votes[i]/total_votes)
       
    for i in range (len(votes)):
        if votes[i]>winner_counts:
            winner_counts=votes[i]
            winner=candidates[i]
    print('Election Results')
    print('----------------------------')
    print(f'Total Votes: {total_votes}')
    print('----------------------------')
    for i in range(len(candidates)):
        print(f'{candidates[i]}: {fixPercent(votes_percent[i])} ({votes[i]})')
    print('----------------------------')
    print(f'Winner: {str(winner)}')

    f=open('results.txt','w+')
    f.write('\nElection Results')
    f.write('\n----------------------------')
    f.write(f'\nTotal Votes: {total_votes}')
    f.write('\n----------------------------')
    for i in range(len(candidates)):
        f.write(f'\n{candidates[i]}: {fixPercent(votes_percent[i])} ({votes[i]})')
    f.write('\n----------------------------')
    f.write(f'\nWinner: {str(winner)}')
    