# 1.  Write a PYTHON program to evaluate the student performance
nilai = int(input("masukkan nilai siswa :"))
if nilai >= 90 :
    print("Excellent performance")
elif nilai >=80 :
    print("Very Good performance")
elif nilai >=70 :
    print("Good performance")
elif nilai >=60 :
    print("average performance")
else:
    print("good luck")

# 2. Write a PYTHON program to find largest of three numbers!
a = float(input("masukkan angka pertama: "))
b = float(input("masukkan angka kedua: "))
c = float(input("masukkan angka ketiga: "))

def temukan_angkabesar(angka1, angka2, angka3):
    largest = angka1
    if angka2 > largest:
        largest = angka2
    if angka3 > largest:
        largest = angka3
    return largest

Angka_Terbesar = temukan_angkabesar(a, b, c)
print("Angka Terbesar:", Angka_Terbesar)

# 3. Write a PYTHON program to print Fibonacci series up to n!
def fibonacci(n):
    a, b = 0, 1
    angka = []
    
    while a <= n:
        angka.append(a)
        a, b = b, a + b
    
    return angka

# Input from the user
n = int(input("masukkan nilai fibonacci: "))

# Generate and print the Fibonacci series
fib_series = fibonacci(n)
print("Urutan angka fibonacci", n, ":", fib_series)

# 4. Write a PYTHON program to print odd numbers up to n!
n = int(input("masukkan nilai n :"))

for steps in range(1,n,2):
    print(steps)

# 5. Write a PYTHON program to produce following design
nilai = int(input("masukkan nilai untuk tinggi pola: "))

for i in range(1, nilai + 1):
    print(str(i) * i)