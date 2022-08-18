import csv
import json
count = 0
loot_list = {}
with open('loot_export.csv') as loot_import:
	lootreader = csv.DictReader(loot_import)
	count_row = 0
	for row in lootreader:
		count_col = 0
		for col in row:
			if (count_col == 0):
				prio_list = []
				loot_name = row['Loot_name']
			if (count_col != 0) and (count_row > 1) and (row[col] != ''):
				prio_split = row[col].split(":")
				temp_raider= prio_split[0]
				temp_prio= prio_split[1]
				temp_json = { 'name':temp_raider, 'Prio':temp_prio}
				prio_list.append(temp_json)
			count_col = count_col +1
		temp_loot_name = row['Loot_name']
		temp_loot_list = {'Prio List':prio_list }

		if count_row > 0:
			if (len(temp_loot_list['Prio List'])>0) and (temp_loot_name in loot_list):
				loot_list[eval('temp_loot_name')].append(temp_loot_list)
			if temp_loot_name not in loot_list and (len(temp_loot_list['Prio List'])>0):
				loot_list[eval('temp_loot_name')] =temp_loot_list
		if count_row == 0 and (len(temp_loot_list['Prio List'])>0):
			loot_list[eval('temp_loot_name')]= temp_loot_list
		count_row = count_row +1
with open("loot_prio.json", "w") as outfile:
	outfile.write(json.dumps(loot_list))
