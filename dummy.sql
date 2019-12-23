--insert stage_policy to base_policy
INSERT INTO jesus.base_policy(PolicyId,PolicyNumber,PolicYHolderName,PolicyStartDate,PolicyExpirationDate,PolicyType,CreateDate,UpdateDate,policy_key,Active_indicater)
select stg_policy.PolicyId,stg_policy.PolicyNumber,stg_policy.PolicYHolderName,stg_policy.PolicyStartDate,stg_policy.PolicyExpirationDate,stg_policy.PolicyType,stg_policy.CreateDate,stg_policy.UpdateDate,stg_policy.policy_key,
CASE WHEN stg_policy.Action_indicater='U' THEN Active_indicater='N'
WHEN stg_policy.Action_indicater='I' THEN Active_indicater='Y'
END as Active_indicater FROM jesus.stg_policy;






 
