import pandas

file=pandas.ExcelFile("myshop.xlsx")
df=file.parse("mobiles")
df.to_pickle("mobilesdata")
print("data stored in file for future use")