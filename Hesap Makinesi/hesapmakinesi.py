while True:
    sayi1 =int(input("birinci sayıyı giriniz: "))
    sayi2 =int(input("ikinci sayıyı giriniz: "))

    operators = input("bir işlem seçiniz(+,-,*, /,%): ")

    if operators == "+":
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
    elif operators == "-":
        print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
    elif operators == "*":
        print(sayi1, "*", sayi2, "=", sayi1 * sayi2)   
    elif operators == "/":
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)  
    elif operators == "%":
        print(sayi1, "%", sayi2, "=", sayi1 % sayi2)    
    else:
        print("Hatalı operator girdiniz!!!") 
                     