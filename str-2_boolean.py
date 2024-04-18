s1="YOU ARE A GREAT PERSON"
s2="iloveyou"
s3="you my 5575 friend"
s4="9977696510"
s5="You have to WORK Hard"

print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())
# print(s4.isalpha())
# print(s5.isalpha())
# print(s1.isdigit())

# ===== isalpha()
# string1 = "Hello"
# string2 = "123"
# string3 = "hello"

# print(string1.isalpha())  # Output: True
# print(string2.isalpha())  # Output: False
# print(string3.isalpha())  # Output: False

# ========= isdigit()
# string1 = "123"
# string2 = "Hello"
# string3 = "123Hello"

# print(string1.isdigit())  # Output: True
# print(string2.isdigit())  # Output: False
# print(string3.isdigit())  # Output: False

# ==========isupper()
# string1 = "HELLO"
# string2 = "Hello"
# string3 = "hello"

# print(string1.isupper())  # Output: True
# print(string2.isupper())  # Output: False
# print(string3.isupper())  # Output: False

# =========== islower()
# string1 = "hello"
# string2 = "Hello"
# string3 = "HELLO"

# print(string1.islower())  # Output: True
# print(string2.islower())  # Output: False
# print(string3.islower())  # Output: False

# =============== isalnum()

# string1 = "hello123"
# string2 = "Hello123"
# string3 = "123"
# string4 = "hello"
# string5 = "hello#@$"

# print(string1.isalnum())  # Output: True
# print(string2.isalnum())  # Output: True
# print(string3.isalnum())  # Output: True
# print(string4.isalnum())  # Output: True
# print(string5.isalnum())  # Output: False

# ================== isidentifier()

# Valid identifiers
print("foo123".isidentifier())   # True
print("_bar".isidentifier())      # True
print("spam_eggs".isidentifier()) # True

# Invalid identifiers
print("123foo".isidentifier())    # False (starts with a digit)
print("foo-bar".isidentifier())   # False (contains '-')
print("if".isidentifier())        # False (reserved keyword)


