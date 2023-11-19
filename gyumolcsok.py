gyumolcsok = ["korte", "barack", "ananász", "banán", "alma"]

print(gyumolcsok)
# sorbarendezés:

x = sorted(gyumolcsok)
print(f"sorbarendezve:  {x} ")

for gyumolcs in x:
    print(gyumolcs)

# "a"-val kezdődők:
string = 'a'
avalkezdodolista = [item for item in gyumolcsok if item.startswith(string)]
print(f"a-val kezdődök listája: {avalkezdodolista} startswith-el")
