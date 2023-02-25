# represa 
# entradas

nivelAgua=float(input('Digite el nivel del agua: '))

#proceso
if nivelAgua >=0 and nivelAgua<=250:
    print(f'el sensor marca {nivelAgua}, muy bajo')
elif nivelAgua >250 and nivelAgua <=400:
    print(f'el sensor marca {nivelAgua},operando normalmente')
else :
    print(f'el sensor marca {nivelAgua},PELIGRO')






