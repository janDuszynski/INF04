import random
while True:
    rundy= 0
    punkty=[]
    while (rundy<3 or rundy>10):
        rundy = int(input("ile kostek chcesz rzucic? (3/10)"))
    for i in range(1,rundy+1):
        liczba = random.randint(1,6)
        print(f"kostka {i}: {liczba}")
        punkty.append(liczba)
    def liczenie(pkt):
        result = []
        for item in pkt:
            if pkt.count(item) > 1:
                result.append(item)
        return sum(result)
    print(liczenie(punkty))
    wynik = input("czy chcesz jeszce raz zagrac?(t/n)")
    if wynik == "t":
        continue
    else:
        break