import csv
from math import ceil,floor
from constraint import*
import csp

#assume number of centre used is same from start till end then equally distribute number of vaccine per day based on it
print("ST1")
vaccineList1, centreList1 =csp.calculateDistribution(15000,434890,115900,5000,20,15,10,21,5)

print("ST2")
vaccineList2, centreList2 =csp.calculateDistribution(35234,378860,100450,10000,30,16,15,10,2)
print("ST3")
vaccineList3, centreList3 =csp.calculateDistribution(22318,643320,223400,7500,22,15,11,12,3)
print("ST4")
vaccineList4, centreList4 =csp.calculateDistribution(23893,859900,269300,8500,16,16,16,15,1)
print("ST5")
vaccineList5, centreList5 =csp.calculateDistribution(19284,450500,221100,9500,19,10,20,15,1)


csp.displayCalculations("Combinations For ST1",vaccineList1,centreList1)
csp.displayCalculations("Combinations For ST2",vaccineList2,centreList2)
csp.displayCalculations("Combinations For ST3",vaccineList3,centreList3)
csp.displayCalculations("Combinations For ST4",vaccineList4,centreList4)
csp.displayCalculations("Combinations For ST5",vaccineList5,centreList5)

keys1 = vaccineList1[0].keys()
keys2 = centreList1[0].keys()
with open('st1vac.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys1)
    dict_writer.writeheader()
    dict_writer.writerows(vaccineList1)
with open('st1centre.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys2)
    dict_writer.writeheader()
    dict_writer.writerows(centreList1)
with open('st2vac.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys1)
    dict_writer.writeheader()
    dict_writer.writerows(vaccineList2)
with open('st2centre.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys2)
    dict_writer.writeheader()
    dict_writer.writerows(centreList2)
with open('st3vac.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys1)
    dict_writer.writeheader()
    dict_writer.writerows(vaccineList3)
with open('st3centre.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys2)
    dict_writer.writeheader()
    dict_writer.writerows(centreList3)
with open('st4vac.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys1)
    dict_writer.writeheader()
    dict_writer.writerows(vaccineList4)
with open('st4centre.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys2)
    dict_writer.writeheader()
    dict_writer.writerows(centreList4)
with open('st5vac.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys1)
    dict_writer.writeheader()
    dict_writer.writerows(vaccineList5)
with open('st5centre.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys2)
    dict_writer.writeheader()
    dict_writer.writerows(centreList5)