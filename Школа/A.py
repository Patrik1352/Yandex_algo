import json

name_json = input()

with open(name_json) as json_file:
    data = json.load(json_file)

rez_dic = {}
vowels = set("aeuioy")
for key, value in data.items():
    inp = input().split("_")
    if value == '30':
        rez_dic[key] = sorted(inp, reverse=True)
    elif value == '20':
        rez_dic[key] = sorted([x for x in inp if len(x) % 2 == 0], reverse=True)
    elif value == '10':
        result = []
        for phrase in inp:
            unique_vowels = set([char for char in phrase if char in vowels])
            if len(unique_vowels) >= 2:
                result.append(phrase)
        rez_dic[key] = sorted(result, reverse=True)


with open('output.json', 'w') as outfile:
    json.dump(rez_dic, outfile)


with open('output.json') as json_file:
    data = json.load(json_file)

print(data)
