import json


def printtestfile(lt):
	fh = open("E:\courses.txt", "w", encoding="utf-8")
	for item in lt:
		fh.write("{}\n".format(item))

jf = open("E:\coursera_jul.json", "r", encoding="utf-8")


courses = json.load(jf)

cc = courses["elements"]

lt = []
for course in cc:
	lt.append([course["workload"], course["name"]])



#print(lt)	
#print()
#print(len(lt))
#print()

lt.sort()
print(lt)

printtestfile(lt)
