import time

print("Hola, Bienvenidos");
print("");
print("1.- Numeros primos");
print("2.- Serie de Fibonacci");
print("");
opt=int(input("Digite su opcion: "));

if (opt == 1):
    print("*** NUMEROS PRIMOS ***");
    print("");
    num = int(input("Ingrese un numero entero: "))
    if (num < 0):
        num = num *-1;
    print("");
    print("=== LISTADO DE NUMEROS PRIMOS ENTRE 1 Y ", num);
    print("");
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print("*",i);
    time.sleep(5);
    print("Hasta pronto!");
    time.sleep(2);
elif (opt == 2):
    print("=*** SUCESION DE FIBONACCI ***=");
    print("");
    n = int(input("Digite el numero máximo para la sucesion: "));
    a = 0;
    b = 1;
    print("SUCESION RESULTANTE: ");
    print(a);
    print(b);
    while True:
        a += b;
        b += a;
        if b > n:
            break
        print(a);
        print(b);
    time.sleep(5);
    print("Hasta pronto!");
    time.sleep(2);
else:
    print("Error, opcion no valida!!");
    time.sleep(2);
    print("Hasta pronto!");
    time.sleep(2);