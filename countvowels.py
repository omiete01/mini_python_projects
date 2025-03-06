# this program counts the number of each vowel in a string

user_str = input("Enter a string: ").lower()
vowel = "aeiou"
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
for word in user_str:
    if word == "a":
        a_count += 1
    if word == "e":
        e_count += 1
    if word == "i":
        i_count += 1
    if word == "o":
        o_count += 1
    if word == "u":
        u_count += 1
    
print(f"a = {a_count}")
print(f"e = {e_count}")
print(f"i = {i_count}")
print(f"o = {o_count}")
print(f"u = {u_count}")
