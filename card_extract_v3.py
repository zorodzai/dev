#updated utility for extracting card data for monthly invoicing
import pandas as pd
import datetime
		
class FileExtract:
	
	def __init__(self, bank):
		self.bank = bank
		self.period = ''
		self.cardspath = ''
		self.cardaccountspath = ''
		self.outputpath = ''
	
	def files(self):
		now = str(datetime.date.today())
		try:
			if self.bank == "cba":
				print("bank is CBA")
				self.cardspath = r'C:\Zoro\dev\cards\cba\cards.txt'
				self.cardaccountspath = r'C:\Zoro\dev\cards\cba\cardaccounts.txt'
				self.outputpath = r'C:\Zoro\dev\cards\output\cba_card_extract_'+now+'.txt'
			elif self.bank == "coge":
				print("bank is Coge")
				self.cardspath = r'C:\Zoro\dev\cards\coge\cards.txt'
				self.cardaccountspath = r'C:\Zoro\dev\cards\coge\cardaccounts.txt'
				self.outputpath = r'C:\Zoro\dev\cards\output\coge_card_extract_'+now+'.txt'
			elif self.bank == "copedu":
				print("bank is COPEDU")
				self.cardspath = r'C:\Zoro\dev\cards\copedu\cards.txt'
				self.cardaccountspath = r'C:\Zoro\dev\cards\copedu\cardaccounts.txt'
				self.outputpath = r'C:\Zoro\dev\cards\output\copedu_card_extract_'+now+'.txt'
			elif self.bank == "unguka":
				print("bank is Unguka")
				self.cardspath = r'C:\Zoro\dev\cards\unguka\cards.txt'
				self.cardaccountspath = r'C:\Zoro\dev\cards\unguka\cardaccounts.txt'
				self.outputpath = r'C:\Zoro\dev\cards\output\unguka_card_extract_'+now+'.txt'
			elif self.bank == "urwego":
				print("bank is Urwego")
				self.cardspath = r'C:\Zoro\dev\cards\urwego\cards.txt'
				self.cardaccountspath = r'C:\Zoro\dev\cards\urwego\cardaccounts.txt'
				self.outputpath = r'C:\Zoro\dev\cards\output\urwego_card_extract_'+now+'.txt'
			elif self.bank == "zigamasc":
				print("bank is Zigama SmartCash")
				self.cardspath = r'C:\Zoro\dev\cards\zigama\SC\cards.txt'
				self.cardaccountspath = r'C:\Zoro\dev\cards\zigama\SC\cardaccounts.txt'
				self.outputpath = r'C:\Zoro\dev\cards\output\zigamaSC_card_extract_'+now+'.txt'
			elif self.bank == "zigamavisa":
				print("bank is Zigama Visa")
				self.cardspath = r'C:\Zoro\dev\cards\zigama\Visa\cards.txt'
				self.cardaccountspath = r'C:\Zoro\dev\cards\zigama\Visa\cardaccounts.txt'
				self.outputpath = r'C:\Zoro\dev\cards\output\zigamaVisa_card_extract_'+now+'.txt'
			else:
				print("bank not found")																
		except:
			print("Error in setting file path")

			
class CleanExtract(FileExtract):

	def __init__(self, bank):
		super().__init__(bank)
		
		
		print('---------------------------------------------')
		self.period = int(input("Enter date in YYMM of last expiry: "))
		print('---------------------------------------------')
		
	def cleaner(self):
		#clean cards.txt file of commas
		try:
			with open(self.cardspath,'r') as file:
				filedata = file.read()
			filedata = filedata.replace('"','')
			with open(self.cardspath,'w') as file:
				file.write(filedata)
			print("card data for "+self.bank+" cleaned")
		except:
			print("error in cleaning cards for "+self.bank)
			
		#clean cardaccounts.txt file of commas
		try:
			with open(self.cardaccountspath,'r') as file:
				filedata = file.read()
			filedata = filedata.replace('"','')
			with open(self.cardaccountspath,'w') as file:
				file.write(filedata)
			print("card accounts data for "+self.bank+" cleaned")
		except:
			print("error in cleaning card accounts for "+self.bank)
		
		
		df = pd.read_csv(self.cardspath,usecols=[0,4,6,7],names=['a','b','c','d'])
		hold=['41.0','42.0','43.0','1.0','45.0','5.0','01']
		df0=df[df.b >= 0]
		df1 = df0[df0.c >= self.period]
		dfcards = df1[~df1.d.isin(hold)]
		dfcardaccounts = pd.read_csv(self.cardaccountspath,usecols=[0,2,3],names=['a','b','c'])
		merged=pd.merge(dfcards,dfcardaccounts,on='a',how='inner')
		merged.to_csv(self.outputpath,header=False,index=False)
		
			
		
#bank1 = ExtractFiles("cba")
bank = CleanExtract("cba")
bank.files()
bank.cleaner()
#bank4.extract()
#bank2 = ExtractFiles("zigama")
#bank2.extract()
	
		
		
