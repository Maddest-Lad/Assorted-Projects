import csv
import os
from collections import Counter

# Stat to Track
user_messages = Counter()
user_words = Counter()

# Pull Up The CSV Folder the Lazy Way
os.chdir("Data")

# Pick Directory
for file_name in os.listdir(os.getcwd()):

    # Open Files
    with open(file_name, encoding="utf_8") as csv_file:

        reader = csv.reader(csv_file, delimiter=',')

        # For Rows in the CSV (Author ID, Author, Date, Content, Attachments, Reactions)

        try:

            for row in reader:
                user_messages[row[1]] += 1  # Message Count
                user_words[row[1]] += len(row[3].split())  # Word Count
        except:
            continue

    # By God Close The File Before Memory Dies
    csv_file.close()

# new_list = Counter()
#
# for i in user_words.most_common():
#
#     try:
#         new_list[i[0]] = i[1] / user_messages[i[0]]
#
#     except:
#
#         continue

# Nice Aligned Print
for x in user_messages.most_common():
    print("%-*s Total: %s" % (30, x[0], round(x[1], 2)))
