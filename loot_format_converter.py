import json
import pandas as pd
infile = open('loot_prio.json')

loot_prio = json.load(infile)

for lootname in loot_prio:
	print(lootname)
	printstring = lootname + " >"
	l = 50
	if (l > 0):
		for prio_list in loot_prio[lootname]:
			l = 50
			#sprint(prio_list)
			for prioentry in loot_prio[lootname][prio_list]:
				#sprint(priolist)
				print(lootname,prioentry)
				l = l -1
		#print(printstring)
