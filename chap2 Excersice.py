uname, wrd = input("Enter your Name and char with commaa (,): ").split(",")
user_length = len(uname)
u_lower = uname.lower()
u_char = wrd.lower()
c_count = str(wrd.count(u_char))

print(f"Your name length is {user_length} and char came for {c_count} times")



name, char = input("Enter Comma separeted name and chars : ").split(",")
print(f"Length of name {len(name)}")
print(f"Chars count in name : {name.lower().count(char.lower())}")
