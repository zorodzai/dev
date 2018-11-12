import pyodbc
print("*********************************************************")
print(" ")
expiry = input("Enter date after which cards expire in YYMM format: ")
print(" ")
print("card program,  active cards")
cnxn = pyodbc.connect("DSN=postcard")
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM fn_active_card_count("+expiry+");")
rows = cursor.fetchall()
for row in rows:
	print(row)
print(" ")
print("*********************************************************")
print(" ")
print("Total cards (active and not active):")
print("card program,  active cards")
cnxn = pyodbc.connect("DSN=postcard")
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM fn_card_count("+expiry+");")
rows = cursor.fetchall()
for row in rows:
	print(row)
print(" ")
print("*********************************************************")
cursor.close()






