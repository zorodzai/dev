import csv
import datetime
import os

inputpath = r'C:\Zoro\dev\python\cardprod\output.txt'
outputpath = r'C:\Zoro\dev\python\cardprod\output_%s.txt' % datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def outputcleaner():
	try:
		print("cleaning apostrophes from Postcard file")
		with open(inputpath,'r') as file:
			filedata=file.read()
		filedata=filedata.replace('"','')
		with open(inputpath,'w') as file:
			file.write(filedata)
		print("cleaning card data complete")
	except Exception as e:
		print("error occured in cleaning cards file")
		print(e)
		


def track1writer():
	try:
		with open(inputpath,'r') as csvinput:
			with open(outputpath,'w') as csvoutput:
				writer=csv.writer(csvoutput,lineterminator='\n')
				reader=csv.reader(csvinput)
				headers=next(reader,None)
				if headers:
					writer.writerow(headers)
			
				print("formatting track 1 data...")
				for row in reader:
					new_value='%B'+row[0]+'^'+row[10].upper()+'/'+row[8].upper()+'^'+row[4]+'2211'+row[18]+'00'+row[15]+'000000?'
					row.append(new_value)
					writer.writerow(row)
				print("formatting complete")
	except Exception as e:
		print(e)


outputcleaner()
track1writer()
			
		


