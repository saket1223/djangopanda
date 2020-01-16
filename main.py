import pandas as pd

dict = {'Function':["Services","Manufacturing","Digital Technology","Finance","Quality","Manufacturing","Human Resources"],
        'comment_present': ["no","yes","yes","no","yes","no","no"],
        'Accountability':["","abc","abc","","abc","",""]}

df = pd.DataFrame(dict)
df.head(7).style.format({"Function": lambda x:x.upper()})
print(df)
pivot_account= pd.pivot_table(df, values=['Accountability'], index=['Function','comment_present'],
                 aggfunc='count')

print(pivot_account)
