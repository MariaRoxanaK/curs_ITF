#exericitii ci operatori logici si boolean

#la sedinta cu parintii poti sa vi cu mama sau tata sau (bunicu si bunica)
mama = True
tata = False
bunicu = False
bunica = False
print(mama or tata or (bunicu and bunica))
print(mama and tata or (bunicu and bunica))
print(mama or tata and (bunicu or bunica))
print((bunicu or bunica) and mama or tata)

# poti sa te inscri la facultate sau la sport sau la kineto sau la politie si drept
sport = True
kineto = True
politie = False
drept = False

print(sport and kineto or politie and drept)
print(sport or kineto and politie and drept)
print(sport and kineto and politie or drept)

#poti sa mananci ori supa ori desert sau supa si felul doi

supa=True
desert=True
felul_doi = False

print(supa and desert or supa and felul_doi)
print(supa and desert and supa and felul_doi)
print(felul_doi and desert)







