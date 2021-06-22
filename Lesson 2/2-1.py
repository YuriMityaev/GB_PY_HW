list = [1 , "str", 32.2 , True, None]
for a,b in  enumerate (list, 1):
    print(f"{a} = {b} - {type(b)}")