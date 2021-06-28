import re


sum_hours = {}

with open("file_6.txt") as f:
    for line in f.readlines():
        sum_hours[re.findall(r"^\w+", line)[0]] = sum(map(int, re.findall(r"\d+", line)))
    print(sum_hours)
