def factorial(n: int) -> int:
    if n < 0:
        return -1  
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

n = int(input("Nhập số nguyên không âm n: "))
if n < 0:
    print("Không tính được giai thừa của số âm.")
else:
    print(f"Giai thừa của {n} là {factorial(n)}.")

