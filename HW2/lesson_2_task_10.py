def bank (summa, years):
    vklad = summa
    for i in range(0, years):
        vklad = vklad + vklad * 0.1
    return vklad
result = bank(1000, 50)
print(round(result, 2))