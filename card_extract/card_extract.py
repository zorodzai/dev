#Utility to parse Postcard card-accounts extract files to create output file of active cards
import pandas as pd
cardspath = r'C:\Zoro\dev\python\card_extract\uob\cards.txt'
cardaccountspath = r'C:\Zoro\dev\python\card_extract\uob\cardaccounts.txt'
output=r'C:\Zoro\dev\python\card_extract\uob\output.txt'

#only cards with expiry date >= 'period' to be returned
period = int(input("Enter date in YYMM of last expiry: "))
print(" ")
#clean extract files of apostrophes around data (Standard 3 format)


def cardcleaner():
	try:
		with open(cardspath,'r') as file:
			filedata=file.read()
		filedata=filedata.replace('"','')
		with open(cardspath,'w') as file:
			file.write(filedata)
		print("cleaning card data complete")
	except:
		print("error occured in cleaning cards file")


def cardaccountscleaner():
	try:
		with open(cardaccountspath,'r') as file:
			filedata=file.read()
		filedata=filedata.replace('"','')
		with open(cardaccountspath,'w') as file:
			file.write(filedata)
		print("cleaning accounts data complete")
	except:
		print("error occured in cleaning cardaccounts file")
				
cardcleaner()
cardaccountscleaner()
print("\nextracting\n")

#use pandas to filter data and merge into one file
df = pd.read_csv(cardspath,usecols=[0,4,6,7],names=['a','b','c','d'])
hold=['41.0','42.0','43.0','1.0','45.0','5.0','01']
df0=df[df.b >= 1]
df1 = df0[df0.c >= period]
dfcards = df1[~df1.d.isin(hold)]
dfcardaccounts = pd.read_csv(cardaccountspath,usecols=[0,2,3],names=['a','b','c'])
merged=pd.merge(dfcards,dfcardaccounts,on='a',how='inner')
merged.to_csv(output,header=False,index=False)

print("extraction complete")
