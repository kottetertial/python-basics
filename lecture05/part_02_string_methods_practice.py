import string

random_string = 'Random String'
print(random_string)

another_random_string = "Another Random String"
print(another_random_string)

multiline_string = '''String
String
String'''
print(multiline_string)

table = "name\tsurname\nValeriia\tManaenkova"
print(table)

welcome = "Hello world"
print(welcome.upper())
print(welcome.lower())
print(welcome.title())
print(welcome.swapcase())

print(welcome.count("o"))
print(welcome.count("h"))

print(welcome.find("o"))
print(welcome.rfind("o"))

print(welcome.endswith("world"))
print(welcome.startswith("world"))

print("16E45".isalnum())
print("16E45".isdigit())

print("hello".islower())
print("hello".isalpha())

table_header = "ID\tNAME\tSURNAME\tCITY\tREGION\tAGE\tWEALTH\tREGISTERED"
print(table_header)

table_header_split = table_header.split()
print(table_header_split)
print(", ".join(table_header_split))

print(string.digits)
print(string.punctuation)
