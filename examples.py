def factorial(n):
    """Kalkulator n! """
    if n <= 1:
        return 1;
    else:
        print(n/0)
        return  n * factorial(n-1)
try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError):
    print("Program tidak bisa dijalankan kalkulasi faktorial terlalu besar")
# except ZeroDivisionError:
#     print("Tidak ada yang bisa dibagi dengan nol")
print("Program diakhiri")