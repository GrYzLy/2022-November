# list = [1,2,3,4]
# strings = ["asda","Asdas","sdasdas"]

#touple
# t = (1231,123123,"sdsadas")

# # print(t)
# # for item in t:
# #     print(int(item))

# #set
# set_example = {'apple', 'orange', 'pear'}

# print(set_example)

#dictionary
dict_example = dict([('klucz','wartosc'), ("klucz2", "wartosc2"), ("klucz3", "wartosc3")])
print(dict_example.keys())
print(dict_example.values())

for k,v in dict_example.items():
    print(k, v)
    key = k
    value = v
    print("Klucz : " + key + " , wartosc : " + value)

print(dict_example["z"])