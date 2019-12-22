import csv
import sys
import datetime
import mysql.connector as dc
con=dc.connect(host="localhost",username="chandra",password="@chennai1",database='jesus')
cur=con.cursor()
#Function for Converting string to date
def date_convert(x):
	if len(x) == 0:
		x = None
		return x
	else:
		format='%d-%b-%Y'
		datetime_object=datetime.datetime.strptime(x,format)
		h=datetime_object.date()
		#d=datetime.datetime.strftime(h,format)
	return h
# Function definition to read file and store in Table
try:
	#truncate before inserting
	tr='''truncate table LandZone;'''
	cur.execute(tr)
	file = sys.argv[1]
	val = []
	with open(file,'r') as c:
		daily_data = csv.DictReader(c, delimiter='|')
		for row in daily_data:
			#if date is not present replace with null and if date is present as string convert  to date format
			PolicyStartDate = date_convert(row['PolicyStartDate'])
			PolicyExpirationDate = date_convert(row['PolicyExpirationDate'])
			ClaimApplyDate = date_convert(row['ClaimApplyDate'])
			ClaimServiceDate = date_convert(row['ClaimServiceDate'])
			ClaimCompletionDate = date_convert(row['ClaimCompletionDate'])
			CreateDate = date_convert(row['CreateDate'])
			UpdateDate = date_convert(row['UpdateDate'])
			#creating list for insert multiple records
			val.append((row['TransactionId'], row['PolicyId'], row['PolicyNumber'], row['PolicYHolderName'], PolicyStartDate, PolicyExpirationDate, row['PolicyType'], row['ClaimID'], row['ClaimType'], ClaimApplyDate, ClaimServiceDate, row['ClaimStatus'], ClaimCompletionDate,CreateDate,UpdateDate))
	in_qry= '''INSERT INTO LandZone(TransactionId,PolicyId,PolicyNumber,PolicYHolderName,PolicyStartDate,PolicyExpirationDate,PolicyType,ClaimID,ClaimType,ClaimApplyDate,ClaimServiceDate,ClaimStatus,ClaimCompletionDate,CreateDate,UpdateDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
	cur.executemany(in_qry, val)
	#commit changes
	con.commit()
except Exception as e:
	print("Error : ", e)
	con.rollback()
