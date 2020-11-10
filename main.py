import re
file = open("transactions.xls").read().splitlines()
transactions = []
start = False
for line in file:
    if not start and "SHBHeader" in line:
        start = True
        continue
    if start:
        datas = re.findall('(?<=">)(<[^T].*?|[^<].*?)(?=<\/TD>)', line)
        if len(datas) == 5:
            transactions.append(datas)

payees_dict = {}
for trans in transactions:
    name = trans[2]
    date = trans[1]
    sum = float(trans[3].replace(" ", "").replace(",", "."))
    if name not in payees_dict.keys():
        payees_dict[name] = {"dates": [], "sum": 0.0}

    ent = payees_dict[name]
    ent["dates"].append(date)
    ent["sum"] += sum

payees_list = [[k, i]for k, i in payees_dict.items()]
payees_list.sort(key=lambda x:x[1]["sum"])
for i in payees_list:
    print(f'{i[0]}: {i[1]["sum"]}')
