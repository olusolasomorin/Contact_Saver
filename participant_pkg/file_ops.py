import csv
from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
path = workspace / "contact.csv"


def save_participant(path, participant_dict):
    fieldname = participant_dict.keys()

    file_exists = path.exists()

    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)
        if not file_exists:

            writer.writeheader()

        writer.writerow(participant_dict)


def load_participant(path):

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        # print(reader)
        for row in reader:
            print(row)