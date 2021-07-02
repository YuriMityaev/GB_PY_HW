with open("file_3.txt", "r", encoding="utf-8") as f:
    empl_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f"Средняя ЗП = {round(sum(empl_dict.values()) / len(empl_dict), 3)}\n"
          f"Работники с заработной платой меньше 20 т.р. - {[e[0] for e in empl_dict.items() if e[1] < 20000]}")
