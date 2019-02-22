#Utility to parse Postcard card-accounts extract files to create output file of active cards
import pandas as pd
import datetime


def cleaner(card):
	global cardspath
	global cardaccountspath
	global outputpath
	
	cards=card
	print('card extraction utility: ',cards)
	
	if cards == 'zigama':
		cardspath = r'C:\data\card_extract\zigama\cards.txt'
		cardaccountspath = r'C:\data\card_extract\zigama\cardaccounts.txt'
		
	elif cards == 'urwego':
		cardspath = r'C:\data\card_extract\urwego\cards.txt'
		cardaccountspath = r'C:\data\card_extract\urwego\cardaccounts.txt'
		
	elif cards == 'cba':
		cardspath = r'C:\data\card_extract\cba\cards.txt'
		cardaccountspath = r'C:\data\card_extract\cba\cardaccounts.txt'
		
	else:
		print('Bank not defined')
	
	#clean cards.txt extract file of apostrophes around data (Standard 3 format)		
	try:
		with open(cardspath,'r') as file:
			filedata=file.read()
		filedata=filedata.replace('"','')
		with open(cardspath,'w') as file:
			file.write(filedata)
		print("cleaning card data for "+cards+" complete")
	except:
		print("error occured in cleaning cards file")
	
	try:
		with open(cardaccountspath,'r') as file:
			filedata=file.read()
		filedata=filedata.replace('"','')
		with open(cardaccountspath,'w') as file:
			file.write(filedata)
		print("cleaning account data for "+cards+" complete")
		print("")
	except:
		print("error occured in cleaning cardaccounts file")
	

				
cleaner('zigama')
cleaner('urwego')
cleaner('cba')


#use pandas to filter data and merge into one file
def createOutput(output):
	print('')
	print('------###------')
	print("")
	outputpath=output
	print("Creating report for ",outputpath)
	period = int(input("Enter date in YYMM of last expiry: "))
	if outputpath == 'zigama':
		report=r'C:\data\card_extract\zigama\zigama_%s.txt' % datetime.datetime.now().strftime('%Y%m%d%H%M')
	elif outputpath == 'urwego':
		report=r'C:\data\card_extract\urwego\urwego_%s.txt' % datetime.datetime.now().strftime('%Y%m%d%H%M')	
	else:
		print('Bank not defined')
	#only cards with expiry date >= 'period' to be returned	
	df = pd.read_csv(cardspath,usecols=[0,4,6,7],names=['a','b','c','d'])
	hold=['41.0','42.0','43.0','1.0','45.0','5.0','01']
	df0=df[df.b >= 1]
	df1 = df0[df0.c >= period]
	dfcards = df1[~df1.d.isin(hold)]
	dfcardaccounts = pd.read_csv(cardaccountspath,usecols=[0,2,3],names=['a','b','c'])
	merged=pd.merge(dfcards,dfcardaccounts,on='a',how='inner')
	merged.to_csv(report,header=False,index=False)
	print("extraction complete for ",outputpath)

def cbaOutput():
	print("")
	print('------###------')
	print("")
	print("creating report for CBA")
	period = int(input("Enter date in YYMM of last expiry: "))
	report=r'C:\data\card_extract\cba\cba_%s.txt' % datetime.datetime.now().strftime('%Y%m%d%H%M')
	df = pd.read_csv(cardspath,usecols=[0,3,4,6,7,20],names=['a','b','e','c','d','f'])
	hold=['41.0','42.0','43.0','1.0','45.0','5.0','01']
	df0=df[df.b >= 1]
	df1 = df0[df0.c >= period]
	dfcards = df1[~df1.d.isin(hold)]
	dfcardaccounts = pd.read_csv(cardaccountspath,usecols=[0,2],names=['a','b'])
	merged=pd.merge(dfcards,dfcardaccounts,on='a',how='inner')
	merged.to_csv(report,header=False,index=False)
	print("extraction complete for CBA")

createOutput('zigama')
createOutput('urwego')
cbaOutput()
