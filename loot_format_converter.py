
import json
infile = open('loot_prio.json')

with open('prio_export.txt', 'w'):
    pass
outfile = open('prio_export.txt', "a")
loot_prio = json.load(infile)



for lootname in loot_prio:
	#print(lootname)
	printstring = lootname + " >"
	l = 50
	if (l > 0):
		for prio_list in loot_prio[lootname]:
			l = 50
			last_prio = 50
			while l > 0:
				for prioentry in loot_prio[lootname][prio_list]:
					if (eval(prioentry['Prio']) == l) and l ==50:
						if printstring[-1]!= '>':
							printstring = printstring + "," + prioentry['name']
							last_prio = eval(prioentry['Prio'])
						if printstring[-1]== '>':
							printstring = printstring + " " +prioentry['name']
							last_prio = eval(prioentry['Prio'])
					if (eval(prioentry['Prio']) == l) and (l < 50):					
						if (eval(prioentry['Prio']) == l) and (l < 50) and (eval(prioentry['Prio']) == last_prio):
							printstring = printstring + "," + prioentry['name']
						if (eval(prioentry['Prio']) == l) and (l < 50) and (eval(prioentry['Prio']) != last_prio):
							if printstring[-1]!= '>':
								printstring = printstring + " > " + prioentry['name']
							if printstring[-1]== '>':
								printstring = printstring + " " +prioentry['name']

							
							last_prio = eval(prioentry['Prio'])

					
				l = l-1
			print(printstring)
			outfile.write(printstring+"\n")
