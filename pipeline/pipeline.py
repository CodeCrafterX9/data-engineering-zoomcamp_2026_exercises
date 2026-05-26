import sys
import pandas as pd
try :
    month = sys.argv[1]
    year=sys.argv[2]
except:
    month=year="Not found"

df = pd.DataFrame({"A":[1,2],"B":[3,4]})
df['month']=month
df["year"]=year
print(df.head())

df.to_parquet("hello.parquet")

print(f"hello world , month : {month}, year: {year}")