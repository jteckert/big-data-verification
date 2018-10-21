import pandas as pd
df = pd.read_csv("OHIDataSet.csv")


result =	{
  "2b1": "N/A",
  "2b2": "N/A",
  "2b3": "N/A",
  "2b4": "N/A",
  "2b5":"N/A",
  "2b6":"N/A",
  "2b7":"N/A",
  "2b8":"N/A",
  "2b9":"N/A",
  "2b10":"N/A",
  "2b11":"N/A",
  "2b12":"N/A",
  "2b13":"N/A",
  "2b14":"N/A",
  "2b15":"N/A",
  "2b16":"N/A",
  "2b17":"N/A",
  "2b18":"N/A",
  "2b19":"N/A"
}
print(result)

#metadata
documentationHeader = ['scenario', 'goal', 'long_goal', 'dimension', 'region_id', 'region_name', 'value']

#Get the header row from the .csv
header = list(df)

#Testing the header
for x in header:
	print(x)


#2b-11, Are the column names consistent with the documentation?
for headerItem in header:
	if headerItem in documentationHeader:
		result["2b11"] = "Yes"

	else:
		result["2b11"] = "No"


print(result)



#2b-8. Is the data organized so that humans and machines can easily read it?
# Checks whether it is in .csv, .json, or  xml format, which are considered machine and
# human readable standards
import json

with open('OHIDataSet.csv') as json_data:

	try:
		json.load(json_data)
		print("True")

	except ValueError as error:
		print("invalid json: %s" % error)
 		# return False