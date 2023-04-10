num = int(input())
# Return an array of bytes representing an integer.
num_b = num.to_bytes(2, byteorder="big")

# Get list of bytes
items = []
for value in num_b:
    items.append(f'\\x{value:02x}')

num_b_rev = bytes("".join(items[::-1]), encoding="utf-8")

# Return the integer represented by the given array of bytes.
print(int.from_bytes(num_b_rev, byteorder="big"))
