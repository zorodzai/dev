import datetime
import pyodbc
import csv

print "This utility extracts ATM cash count for selected bank."
print" "
print" "
print"1. Urwego"
print"2. Zigama"
print"3. CBA"
print" \n"




filename = datetime.datetime.now().strftime("-%d%m%Y-%H%M")
connection_str =    """
DSN=realtime;
Trusted_Connection=yes;
"""

#Trusted_Connection=yes;
#UID=sa;
#PWD=$post123;

db_connection = pyodbc.connect(connection_str,timeout=60)
if (db_connection == False):
    print"error in connecting to database"
else:    
    db_connection.autocommit = True
    #db_connection.autocommit = False
    db_cursor = db_connection.cursor()


while True:
    sponsor = raw_input("Select bank (1 - 3) from list: ")   
    if sponsor=="1":
    
        csv_file = open('C:\\AtmReports\\UrwegoATMCash'+filename+'.csv', 'wb')
        rows = db_connection.execute("EXEC AtmCashCount 'UOB','UOBANK' ")        
        writer = csv.writer(csv_file)
        writer.writerow(['ATM ID', 'Location', 'Cassette', 'Notes', 'Value', 'Denomination', 'Diverted notes', 'Extraction date'])
        writer.writerows(rows)
        csv_file.close()
        
        print"cash count for Urwego extracted"

                           
    elif sponsor=="2":
    
        csv_file = open('C:\\AtmReports\\ZigamaATMCash'+filename+'.csv', 'wb')
        rows = db_connection.execute("EXEC AtmCashCount 'Zigama','' ")        
        writer = csv.writer(csv_file)
        writer.writerow(['ATM ID', 'Location', 'Cassette', 'Notes', 'Value', 'Denomination', 'Diverted notes', 'Extraction date'])
        writer.writerows(rows)
        csv_file.close()
        
        print"cash count Zigama CSS Bank extracted"  

    elif sponsor=="3":
    
        csv_file = open('C:\\AtmReports\\CBA_ATMCash'+filename+'.csv', 'wb')
        rows = db_connection.execute("EXEC AtmCashCount 'CBR','' ")        
        writer = csv.writer(csv_file)
        writer.writerow(['ATM ID', 'Location', 'Cassette', 'Notes', 'Value', 'Denomination', 'Diverted notes', 'Extraction date'])
        writer.writerows(rows)
        csv_file.close()
        
        print"cash count CBA Rwanda extracted" 
        
             
    else:
        print "enter valid option"
    print" \n"    
    exit_prog = raw_input("To exit type X or press Enter to extract another bank: ")
    print" \n"
    if exit_prog=='X':
        break
db_cursor.close()
   
    
    


    
    


#if sponsor == "1":
    
    
