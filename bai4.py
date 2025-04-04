def fibonacci(n: int) -> int:
    if n < 0:
        return -1  
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

n = int(input("Nhập số nguyên n: "))
if n < 0:
    print("Không tính được số Fibonacci của số âm.")
else:
    print(f"Số Fibonacci thứ {n} là {fibonacci(n)}.")
