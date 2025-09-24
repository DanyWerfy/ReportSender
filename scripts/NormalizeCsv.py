import csv
import os
import itertools
import re
import sys
sys.path.append(r"C:\Users\DanyDiab\Desktop\Work\EmailSender")
from EmailSender import CreateEmailDrafts
def main():
    csvPath = "../data/HOTEL CO OWNERS UNIT AND EMAIL ID(Information from Dec2023).csv"
    outputPath = "../data/coOwnerEmails.csv"
    payloadPath = "../data/Werfy_Luxury_Apart-Hotel_Future_Reservation_Report.html"
    emails = extractEmails(csvPath)
    


def extractEmails(csvPath):
    with open(csvPath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f=f, delimiter=";")
        emails = []
        for row in reader:
            currEmail = row["EMAIL ADDRESS"]
            emailNormal = re.sub(r"\s", "",currEmail)
            emailSplit = emailNormal.split(",")
            emails.append(emailSplit)

        flatEmails = list(itertools.chain.from_iterable(emails))
    return flatEmails
if __name__ == "__main__":
    main()