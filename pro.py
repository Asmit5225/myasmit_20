import pandas as pd 
import json
df= pd.read_csv("wine-ratings-small.csv") #here we read a csv file usuing pandas
#print(df) #here we print the csv file in python in table form
#df1=df.head() #here we print the first 10 items of the table
#print(df1)
#dictonary=df1.to_dict() #here we convert the table into a dictonary format 
#print(dictonary['name']) #here we print all the values of name key... 
dict1=df.to_dict()
#print(dict1)
newlist=[]
for key, rows in df.iterrows():
    if rows['variety'] in ['Red Wine ','White Wine']: 
        if rows['rating']== 90:
            if rows['region'] == 'Austria':
                newlist.append(rows.to_dict())
#print(newlist) 
 
df2=pd.DataFrame(newlist)
#print(df2)
#reqfile=json.dumps(newlist)
with open("sample_data_wine_of_austria_90rating.json", "w") as f:
    json.dump(newlist,f, indent=4)

               

 

    




