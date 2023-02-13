# 세탁소 사장 동혁
for t in range(int(input())):
    cent = int(input())
    coin = {'Quarter': 0, 'Dime': 0, 'Nickel': 0, 'Penny': 0}
    while cent > 0:
        if cent >= 25:
            cent -= 25
            coin['Quarter'] += 1
        elif cent >= 10:
            cent -= 10
            coin['Dime'] += 1
        elif cent >= 5:
            cent -= 5
            coin['Nickel'] += 1
        elif cent >= 1:
            cent -= 1
            coin['Penny'] += 1
    print(*coin.values())