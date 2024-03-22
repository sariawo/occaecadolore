import csv

with open('cleaned.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(user[0].keys())
    writer.writerows(user)
