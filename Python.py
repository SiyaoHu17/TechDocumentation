import cx_Oracle as ora
import pandas as pd


username ="username"
password = "password"
connectString="server:port/servicename"
mode=ora.SYSDBA
connection = ora.connect(username, password, connectString)
data=pd.read_sql("SELECT * FROM VVIJAYAK.ACH_IN_OUT", con=connection)
