for i, element in enumerate(cpdomains):
    cpdomains[i] = element.split(" ")
subdomains = []
for i in cpdomains:
    cpdomains_split = list(i[1])
    while "." in cpdomains_split:
        del cpdomains_split[0:cpdomains_split.index(".")+1]
        subdomains.append([i[0], "".join(cpdomains_split)])
alldomains = cpdomains + subdomains
dictionary = {}
for i in alldomains:
    if i[1] in dictionary:
        dictionary[i[1]] += int(i[0])
    else:
        dictionary[i[1]] = int(i[0])
res = []
for key, value in dictionary.items():
    res.append(" ".join([str(value), key]))
return res