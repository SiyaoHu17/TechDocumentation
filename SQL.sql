
GetDate()
regular expression
https://docs.oracle.com/cd/B14117_01/appdev.101/b10795/adfns_re.htm
listunagg
https://stackoverflow.com/questions/13189575/listunagg-function
join....on...and....
rank() over (partition by..order by….desc ):rank inside group
create temporary table a select * from b
SELECT TIMESTAMP("2017-07-23")




MySQL Syntax:

SELECT column_name(s) FROM table_name WHERE condition LIMIT number;

Oracle Syntax:

SELECT column_name(s) FROM table_name WHERE ROWNUM <= number;




import cx_Oracle as ora


import pandas as pd


username ="SiyaoHu"
password = "xxxxx"
connectString="CNUDC029DF-SCAN.CNB.CORP.NET:1521/CITYACCESS_DEV"
mode=ora.SYSDBA
connection = ora.connect(username, password, connectString)

data=pd.read_sql("SELECT * FROM ETLACH.STG_ACH_TRANSACTION LIMIT 10", con=connection)



Oracle:
select 1
from dual 
WHERE sysdate BETWEEN TO_DATE('28/02/2014', 'DD/MM/YYYY') AND TO_DATE('20/06/2014', 'DD/MM/YYYY');

select 1
from dual 
WHERE trunc(sysdate) BETWEEN TO_DATE('28/02/2014', 'DD/MM/YYYY') AND
                             TO_DATE('20/06/2014', 'DD/MM/YYYY');


SELECT MIN(TRANSACTION_EFFECTIVE_DATE),MAX(TRANSACTION_EFFECTIVE_DATE),trunc(sysdate, 'month'),add_months(trunc(sysdate, 'month'), -12),sysdate
FROM ETLACH.STG_ACH_TRANSACTION 
WHERE TRANSACTION_EFFECTIVE_DATE  
between add_months(sysdate, -12) and sysdate


CREATE TABLE new_table
  AS (SELECT * FROM old_table);
  
  
rolling 12 month between add_months(trunc(sysdate, 'month'), -12) and trunc(sysdate, 'month')
