import mysql.connector as dc
con=dc.connect(host="localhost",username="chandra",password="@chennai1",database='jesus')
cur=con.cursor()
#insert data from landzone to stage_policy
try:
	#truncate before inserting
	tr='''truncate table stg_policy;'''
	cur.execute(tr)
	in_clqry='''INSERT ignore  INTO jesus.stg_policy(PolicyId,PolicyNumber,PolicYHolderName,PolicyStartDate,PolicyExpirationDate,PolicyType,CreateDate,UpdateDate,policy_key,Action_Indicater)select STG_A.*,
CASE WHEN STG_A.PolicyId = base_policy.PolicyId THEN 'U'
ELSE 'I' END as Action_Indicater 
from (SELECT PolicyId,PolicyNumber,PolicYHolderName,PolicyStartDate,PolicyExpirationDate,PolicyType,CreateDate,UpdateDate,md5(concat(PolicyId,CreateDate,UpdateDate)) as pol_key
FROM jesus.landzone) STG_A left join jesus.base_policy on STG_A.PolicyId=base_policy.PolicyId;'''
	cur.execute(in_clqry)
	#commit changes
	con.commit()
except Exception as e:
	print("Error : ", e)
	con.rollback()
#insert data from landzone to stage_claims
try:
	#truncate before inserting
	tr='''truncate table stg_claims;'''
	cur.execute(tr)
	in_clqry='''INSERT ignore  INTO jesus.stg_claims(PolicyId,ClaimID,ClaimType,ClaimApplyDate,ClaimServiceDate,ClaimStatus,ClaimCompletionDate,CreateDate,UpdateDate,claims_key,Action_Indicater)select STG_C.*,
CASE WHEN STG_C.ClaimID = base_claims.ClaimID THEN 'U'
ELSE 'I' END as Action_Indicater 
from (SELECT PolicyId,ClaimID,ClaimType,ClaimApplyDate,ClaimServiceDate,ClaimStatus,ClaimCompletionDate,CreateDate,UpdateDate,md5(concat(PolicyId,CreateDate,UpdateDate)) as cla_key
FROM jesus.landzone) STG_C left join jesus.base_claims on STG_C.PolicyId=base_claims.PolicyId;'''
	cur.execute(in_clqry)
	#commit changes
	con.commit()
except Exception as e:
	print("Error : ", e)
	con.rollback()
