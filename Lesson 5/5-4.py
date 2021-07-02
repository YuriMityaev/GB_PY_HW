r_d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file_4ru.txt", "w", encoding="utf-8") as new_file:
    with open("file_4en.txt", encoding="utf-8") as my_file:
        new_file.writelines([line.replace(line.split()[0], r_d.get(line.split()[0])) for line in my_file])