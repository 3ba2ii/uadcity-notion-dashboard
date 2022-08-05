
import csv


def read_emails_from_csv(file_path: str = 'attendance.csv'):
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        emails = []
        for row in csvreader:
            if row[2] == 'Email':
                continue
            emails.append(row[2])
    return emails
