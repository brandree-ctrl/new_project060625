import pandas as pd
from re import search
import csv
import json




with open (r'/Users/brandree/Downloads/appleinc/Apple_CHexported_users_compare_result_20220604.csv') as f:
	columns = (
			
			"uid",
			"User Email",
			"webexFirstName",
            "webexLastName",
            "webexDisplayName",            
            "Userstatus",
            "lastService",
            "Date"
            )
            

	reader = csv.DictReader(f, columns)
	rows = list(reader)
	for row in rows:
		emails = (row["User Email"])
		displayname = (row["webexDisplayName"])
		family_name = (row["webexFirstName"])
		given_name = (row["webexLastName"])
		print("given", given_name)
		print("emails", emails)
		print("displayname", displayname)
		print("family_name", family_name)






