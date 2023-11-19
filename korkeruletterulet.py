def korkerulet(r):
    return 2 * 3.14 * r

def korterulet(r):
    return 3.14 * r **2

print('a kör sugara: ')
r = int(input())

print(f'A kör kerülete: {korkerulet(r)} ')
print(f'A kör területe: {korterulet(r)} ')
