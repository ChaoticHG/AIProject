from math import ceil,floor
from constraint import*

def calculateDistribution(totalPopulationA,totalPopulationB,totalPopulationC,dailyLimit,cr1range,cr2range,cr3range,cr4range,cr5range):
#assume number of centre used is same from start till end then equally distribute number of vaccine per day based on it
    daysneeded = ceil((totalPopulationA+totalPopulationB+totalPopulationC)/dailyLimit)
    varange = floor(totalPopulationA/(daysneeded))
    vbrange = floor(totalPopulationB/(daysneeded))
    vcrange = floor(totalPopulationC/(daysneeded))
    problem2 = Problem()
    problem2.addVariable("va",[*range(varange-150,varange+150,1)])
    problem2.addVariable("vb",[*range(vbrange-150,vbrange+150,1)])
    problem2.addVariable("vc",[*range(vcrange-150,vcrange+150,1)])
    problem2.addVariable("finalva",[*range(varange-150,varange+150,1)])
    problem2.addVariable("finalvb",[*range(vbrange-150,vbrange+150,1)])
    problem2.addVariable("finalvc",[*range(vcrange-150,vcrange+150,1)])
    problem2.addConstraint(lambda va,finalva:va*(daysneeded-1)+finalva==totalPopulationA,("va","finalva"))
    problem2.addConstraint(lambda vb,finalvb:vb*(daysneeded-1)+finalvb==totalPopulationB,("vb","finalvb"))
    problem2.addConstraint(lambda vc,finalvc:vc*(daysneeded-1)+finalvc==totalPopulationC,("vc","finalvc"))
    problem2.addConstraint(lambda va,finalva:abs(va-finalva)<=150,("va","finalva"))
    problem2.addConstraint(lambda vb,finalvb:abs(vb-finalvb)<=150,("vb","finalvb"))
    problem2.addConstraint(lambda vc,finalvc:abs(vc-finalvc)<=150,("vc","finalvc"))
    problem2.addConstraint(lambda va,vb,vc:va+vb+vc <=dailyLimit,["va","vb","vc"])
    problem2.addConstraint(lambda finalva,finalvb,finalvc:finalva+finalvb+finalvc <=dailyLimit,["finalva","finalvb","finalvc"])
    solutions2=problem2.getSolutions()
    #this part will calculate the maximum population needed to cover per day 
    for a in range(len(solutions2)):
        solutions2[a]['differ'] =  ( abs(solutions2[a]['finalva']-solutions2[a]['va']) + abs(solutions2[a]['finalvb']-solutions2[a]['vb']) + abs(solutions2[a]['finalvc']-solutions2[a]['vc']) )
        maxb=solutions2[a]['finalva']+solutions2[a]['finalvb']+solutions2[a]['finalvc']
        maxa=solutions2[a]['va']+solutions2[a]['vb']+solutions2[a]['vc']
        if(maxa>maxb):
            maxpop=maxa
        else:
            maxpop=maxb
        maxpop -= maxpop % -100
        solutions2[a]['maxpop']=maxpop
    #print(min(solutions2,key=lambda x:x['avgabs']))
    
    vaccineList = sorted(solutions2,key=lambda x:x['differ'])
    #print(vaccineList[:3])
    
    vaccineDistribution=min(solutions2,key=lambda x:x['differ'])
    #print(a)
    maxb=vaccineDistribution['finalva']+vaccineDistribution['finalvb']+vaccineDistribution['finalvc']
    maxa=vaccineDistribution['va']+vaccineDistribution['vb']+vaccineDistribution['vc']
    if(maxa>maxb):
        maxpop=maxa
    else:
        maxpop=maxb
    maxpop -= maxpop % -100
    problem = Problem()
    problem.addVariable("cr1",[*range(0,cr1range+1,1)])
    problem.addVariable("cr2",[*range(0,cr2range+1,1)])
    problem.addVariable("cr3",[*range(0,cr3range+1,1)])
    problem.addVariable("cr4",[*range(0,cr4range+1,1)])
    problem.addVariable("cr5",[*range(0,cr5range+1,1)])
    #the constraint for maximum vaccination limit
    problem.addConstraint(lambda cr1,cr2,cr3,cr4,cr5:cr1*200 + cr2*500 + cr3*1000 + cr4*2500 + cr5*4000 >= maxpop,("cr1","cr2","cr3","cr4","cr5"))
    solutions=problem.getSolutions()
    #print(solutions)
    for a in range(len(solutions)):
        solutions[a]['cost'] = solutions[a]['cr1']*100 + solutions[a]['cr2']*250 +solutions[a]['cr3']*500 + solutions[a]['cr4']*800 + solutions[a]['cr5']*1200
        #print(solutions[a])
    centreList = sorted(solutions,key=lambda x:x['cost'])
    totalCentre =min(solutions,key=lambda x:x['cost'])
    
    centres = list(totalCentre.values())
    centreNeeded = "Vaccination Centre Type Needed             : "
    for a in range(5):
        if(totalCentre['cr'+str(a+1)]!=0):
            centreNeeded +=  "Centre " + str(a+1) + " x " + str(totalCentre['cr'+str(a+1)] ) + " "
    print("Total Day Needed         : " + str(daysneeded) + " Days")
    print("Rental per day           : RM " + str(centreList[0]['cost']))
    print("Total Vaccine A per day  : " + str(vaccineList[0]['va']))
    print("Total Vaccine A last day : " + str(vaccineList[0]['finalva']))
    print("Total Vaccine B per day  : " + str(vaccineList[0]['vb']))
    print("Total Vaccine B last day : " + str(vaccineList[0]['finalvb']))
    print("Total Vaccine C per day  : " + str(vaccineList[0]['vc']))
    print("Total Vaccine C last day : " + str(vaccineList[0]['finalvc']))
    print("Maximum total vaccine distribution per day : " + str(maxpop))
    print(centreNeeded)
    print()
    return vaccineList, centreList

def displayCalculations(text,vaccineList,centreList):
    print(text)
    print("Top vaccine distribution for the smallest difference between final day and average day distribution")
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Vaccine A','Vaccine B','Vaccine C', 'Final VA','Final VB','Final VC','Total Difference'))
    length=len(vaccineList)
    if(length>5):
        length=5
    for x in range(length):
        print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(vaccineList[x]['va'],vaccineList[x]['vb'],vaccineList[x]['vc'], vaccineList[x]['finalva'],vaccineList[x]['finalvb'],vaccineList[x]['finalvc'],vaccineList[x]['differ']))
    print()
    print("Top cheapest vaccine centre usage")
    length=len(centreList)
    if(length>5):
        length=5
    for x in range(length):
        centreNeeded = "Total cost of RM " + str(centreList[x]['cost']) + " :"
        for a in range(5):
            if(centreList[x]['cr'+str(a+1)]!=0):
                centreNeeded +=  "Centre " + str(a+1) + " x " + str(centreList[x]['cr'+str(a+1)] ) + " "
        print(centreNeeded)
    print()