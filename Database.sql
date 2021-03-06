-- Database Creatation Mysql Query
CREATE DATABASE IF NOT EXISTS jesus;

-- Change Database as current database Mysql Query 
USE DATABASE jesus;

-- Create LandZone Table 
CREATE TABLE IF NOT EXISTS LandZone(TransactionId INT NOT NULL,PolicyId BIGINT NOT NULL,PolicyNumber INT NOT NULL,PolicYHolderName VARCHAR(20)NOT NULL,PolicyStartDate DATE NOT NULL,PolicyExpirationDate DATE NOT NULL,PolicyType VARCHAR(25)NOT NULL,ClaimID INT NOT NULL,ClaimType VARCHAR(20)NOT NULL,ClaimApplyDate DATE NOT NULL,ClaimServiceDate DATE,ClaimStatus VARCHAR(10)NOT NULL,ClaimCompletionDate DATE,CreateDate Date,UpdateDate Date);



-- Create Stage_Policy Table 
CREATE TABLE IF NOT EXISTS stg_policy(PolicyId BIGINT NOT NULL,PolicyNumber INT NOT NULL,PolicYHolderName VARCHAR(20)NOT NULL,PolicyStartDate DATE NOT NULL,PolicyExpirationDate DATE NOT NULL,PolicyType VARCHAR(25)NOT NULL,CreateDate Date,UpdateDate Date,policy_key varchar(40) PRIMARY KEY,Action_indicater varchar(1));

--Create Stage_claims Table 
CREATE TABLE IF NOT EXISTS jesus.stg_claims(PolicyId BIGINT NOT NULL,ClaimID INT NOT NULL,ClaimType VARCHAR(20)NOT NULL,ClaimApplyDate DATE NOT NULL,ClaimServiceDate DATE,ClaimStatus VARCHAR(10)NOT NULL,ClaimCompletionDate DATE,CreateDate Date,UpdateDate Date,policy_key varchar(40) PRIMARY KEY,claims_key varchar(40)NOT NULL,Action_indicater varchar(1)NOT NULL);



--Create base_Policy Table
CREATE TABLE IF NOT EXISTS base_policy(PolicyId BIGINT NOT NULL,PolicyNumber INT NOT NULL,PolicYHolderName VARCHAR(20)NOT NULL,PolicyStartDate DATE NOT NULL,PolicyExpirationDate DATE NOT NULL,PolicyType VARCHAR(25)NOT NULL,CreateDate Date,UpdateDate Date,policy_key varchar(40) PRIMARY KEY,Active_indicater varchar(1)NOT NULL);

--Create base_claims Table 
CREATE TABLE IF NOT EXISTS jesus.base_claims(PolicyId BIGINT NOT NULL,ClaimID INT NOT NULL,ClaimType VARCHAR(20)NOT NULL,ClaimApplyDate DATE NOT NULL,ClaimServiceDate DATE,ClaimStatus VARCHAR(10)NOT NULL,ClaimCompletionDate DATE,CreateDate Date,UpdateDate Date,policy_key varchar(40) NOT NULL ,policy_key varchar(40),claims_key varchar(40)PRIMARY KEY,Active_indicater varchar(1)NOT NULL);

