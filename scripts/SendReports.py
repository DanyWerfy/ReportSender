import csv
import os
import itertools
import re
import sys
import asyncio
sys.path.append(r"C:/Users/DanyDiab/Desktop/Work/EmailSender/modules")
import auth,send

csvPath = "../data/HOTEL CO OWNERS UNIT AND EMAIL ID(Information from Dec2023).csv"
outputPath = "../data/coOwnerEmails.csv"
payloadPath = "../data/Werfy_Luxury_Apart-Hotel_Future_Reservation_Report.html"
configPath = "../data/config.cfg"

async def main():

    emails = extractEmails(csvPath)
    html = extractHTML(payloadPath)
    cleanedHTML = cleanHTML(html)
    token = auth.connect_to_api(configPath)

    for email in emails:
        await send.send_email(token, cleanedHTML,email,"reportTest")


    


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

def extractHTML(payloadPath):
    with open(payloadPath, "r", encoding="utf-8") as f:
        htmlContent = f.read()
    return htmlContent

def cleanHTML(html):
    clean = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    return clean

if __name__ == "__main__":
    asyncio.run(main())