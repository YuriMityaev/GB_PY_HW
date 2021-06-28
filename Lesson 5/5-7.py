import json

with open("text77.json", "w", encoding="utf-8") as w_f:
    with open("file_7.txt", encoding="utf-8") as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        result = [profit, {"Чистый профит": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, w_f, ensure_ascii=False, indent=4)
