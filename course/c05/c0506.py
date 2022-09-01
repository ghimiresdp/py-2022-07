# Dictionary Comprehension
# %%
v1 = [x**2 for x in range(100000000)]

# print(v1)

print(v1.__sizeof__())
# 168
# 8448712

# %%
v1 = (x**2 for x in range(10))

# print(v1)

print(v1.__sizeof__())
for value in v1:
    print(value)

# %%
x = list(range(1000000))

# %%
