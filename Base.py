import mysql.connector as dc
con=dc.connect(host="localhost",username="chandra",password="@chennai1",database='jesus')
cur=con.cursor()
#insert data from stage_policy to base_policy
try:
	#Update data if already exists in base_policy
	up_polqry='''UPDATE jesus.base_policy
	SET  Active_indicater = 'N'
	WHERE PolicyId IN (SELECT PolicyId FROM jesus.stg_policy WHERE Action_indicater = 'U');'''
	cur.execute(up_polqry)
	#Insert new data into base_policy
	in_polqry='''INSERT ignore  INTO jesus.base_policy(PolicyId,PolicyNumber,PolicYHolderName,PolicyStartDate,PolicyExpirationDate,PolicyType,CreateDate,UpdateDate,policy_key,Active_indicater)
select PolicyId,PolicyNumber,PolicYHolderName,PolicyStartDate,PolicyExpirationDate,PolicyType,CreateDate,UpdateDate,policy_key ,'Y' from jesus.stg_policy;'''
	cur.execute(in_polqry)
	#commit changes
	con.commit() 
except Exception as e:
	print("Error : ", e)
	con.rollback()  
#insert data from stage_claims base_claims

try:
	#Update data if already exists in base_claims
	up_clqry='''UPDATE jesus.base_claims
	SET  Active_indicater = 'N'
	WHERE PolicyId IN (SELECT PolicyId FROM jesus.stg_claims WHERE Action_indicater = 'U')'''
	cur.execute(up_clqry)
	#Insert new data into base_claims
	in_clqry='''INSERT ignore  INTO jesus.base_claims(PolicyId,ClaimID,ClaimType,ClaimApplyDate,ClaimServiceDate,ClaimStatus,ClaimCompletionDate,CreateDate,UpdateDate,policy_key,claims_key,Active_indicater)
select PolicyId,ClaimID,ClaimType,ClaimApplyDate,ClaimServiceDate,ClaimStatus,ClaimCompletionDate,CreateDate,UpdateDate,policy_key,claims_key,'Y' from jesus.stg_claims;'''
	cur.execute(in_clqry)
	#commit changes
	con.commit()
except Exception as e:
	print("Error : ", e)
	con.rollback()
