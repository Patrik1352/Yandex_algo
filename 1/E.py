n,k,d = list(map(int, input().split()))

def optimized_cats(n, k, d):
    # Initial check if the current number is already divisible by k
    if n % k == 0:
        return n * (10 ** d)  # Directly append d zeroes at the end

    for _ in range(d):
        r = n % k  # Find the remainder of the current number divided by k
        found = False
        for i in range(10):
            # Check if appending this digit makes the number divisible by k
            if (r * 10 + i) % k == 0:
                n = n * 10 + i  # Update n by appending the digit
                found = True
                break
        if not found:
            return -1  # If no digit found that makes the number divisible, return -1
    return n


print(optimized_cats(n, k, d))