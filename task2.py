n, w, d, p = list(map(int, input().split()))
# Quantity of coins: 1+2+3+...+(N-2)+(N-1)=N*(N-1)/2

# Total weight of the original coins
m = w * n * (n-1)/2

# the weight of fake coins
m_f = m - p
if m_f > 0:
    print(m_f / d)
else:
    print(n)
