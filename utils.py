import csv
import json

def load_email_data(path):
    emails = []
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                emails.append(row)
    except:
        print("⚠️ Could not load email data.")
    return emails


def load_tasks(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("⚠️ Could not load tasks file.")
    return []
