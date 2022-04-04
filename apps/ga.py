import math
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import altair as alt
def app():
    def dispIndividual(displayData):
        st.write('Money on-hand       : RM 7000')
        st.write('Vacation duration   : 5 days')
        st.write('Hotel star rating   : '+ str(math.floor( displayData.iloc[0])) + ' per night')
        st.write('Tourist spots       : '+ str(math.floor( displayData.iloc[1])) + ' spots')
        st.write('One tourist spot    : '+ str(math.floor( displayData.iloc[2])) )
        st.write('Food price          : '+ str(math.floor( displayData.iloc[3])) + ' per meal ')
        st.write('Transportation fees : '+ str(math.floor( displayData.iloc[4])) + ' per trip ')
        st.write('Transport frequency : '+ str(math.floor( displayData.iloc[5])) + ' trip per day ')
        st.write('No of Loops/ No of Generations Needed :' + str(math.floor( displayData.iloc[6])) )
        st.write('Time Taken :' + str( displayData.iloc[7]) )
    st.title("Question 1")
    #this is the sidebar menu
    with st.sidebar:
        st.info("Money on-hand : RM 7000  \n Vacation duration : 5 days  \n Hotel star rating : <RM300 per night  \n Tourist spots       : 13 spots  \n One tourist spot    : <RM400  \n  Food price          : <RM30 per meal  \n  Transportation fees : <RM65 per trip   \n  Transport frequency : max 8 trip per day  \n  Max total           : RM 9750")
        selectionRadio = st.radio(
            "Choose a modification method",
            ("Pairing Selection", "Tournament Selection","Random Selection")
        )
        number=st.number_input("Select Run Time",min_value=1,max_value=5,step=1)
        displayReport=st.checkbox("Display comparison of all 3 methods")

    totalLoop1,totalLoop2,totalLoop3,totalTime1,totalTime2,totalTime3=[0]*6
    data= pd.read_csv('q1data.csv', header=None)
    data.columns=['Hotel Star','Total Tour Spot','Tour Budget','Food Budget','Transport Budget','Transport Frequency','Total Loop/No of Generations','Time Taken']
    fitnessData= pd.read_csv('q1gen.csv', header=None)
    fitnessData.columns=['Generation','Overall Fitness']
    #st.dataframe(data=data)
    #st.dataframe(data=fitnessData)
    #below generates dataframe from the q1gen.csv into multiple dataframe based on each runtime of each methods
    p0=fitnessData.loc[fitnessData['Generation']=='p0gen',['Overall Fitness']]
    p0.reset_index(inplace = True, drop = True)
    p0.columns=['Pairing Selection 1']
    p1=fitnessData.loc[fitnessData['Generation']=='p1gen',['Overall Fitness']]
    p1.reset_index(inplace = True, drop = True)
    p1.columns=['Pairing Selection 2']
    p2=fitnessData.loc[fitnessData['Generation']=='p2gen',['Overall Fitness']]
    p2.reset_index(inplace = True, drop = True)
    p2.columns=['Pairing Selection 3']
    p3=fitnessData.loc[fitnessData['Generation']=='p3gen',['Overall Fitness']]
    p3.reset_index(inplace = True, drop = True)
    p3.columns=['Pairing Selection 4']
    p4=fitnessData.loc[fitnessData['Generation']=='p4gen',['Overall Fitness']]
    p4.reset_index(inplace = True, drop = True)
    p4.columns=['Pairing Selection 5']
    m0=fitnessData.loc[fitnessData['Generation']=='m0gen',['Overall Fitness']]
    m0.reset_index(inplace = True, drop = True)
    m0.columns=['Tournament Selection 1']
    m1=fitnessData.loc[fitnessData['Generation']=='m1gen',['Overall Fitness']]
    m1.reset_index(inplace = True, drop = True)
    m1.columns=['Tournament Selection 2']
    m2=fitnessData.loc[fitnessData['Generation']=='m2gen',['Overall Fitness']]
    m2.reset_index(inplace = True, drop = True)
    m2.columns=['Tournament Selection 3']
    m3=fitnessData.loc[fitnessData['Generation']=='m3gen',['Overall Fitness']]
    m3.reset_index(inplace = True, drop = True)
    m3.columns=['Tournament Selection 4']
    m4=fitnessData.loc[fitnessData['Generation']=='m4gen',['Overall Fitness']]
    m4.reset_index(inplace = True, drop = True)
    m4.columns=['Tournament Selection 5']
    r0=fitnessData.loc[fitnessData['Generation']=='r0gen',['Overall Fitness']]
    r0.reset_index(inplace = True, drop = True)
    r0.columns=['Random Selection 1']
    r1=fitnessData.loc[fitnessData['Generation']=='r1gen',['Overall Fitness']]
    r1.reset_index(inplace = True, drop = True)
    r1.columns=['Random Selection 2']
    r2=fitnessData.loc[fitnessData['Generation']=='r2gen',['Overall Fitness']]
    r2.reset_index(inplace = True, drop = True)
    r2.columns=['Random Selection 3']
    r3=fitnessData.loc[fitnessData['Generation']=='r3gen',['Overall Fitness']]
    r3.reset_index(inplace = True, drop = True)
    r3.columns=['Random Selection 4']
    r4=fitnessData.loc[fitnessData['Generation']=='r4gen',['Overall Fitness']]
    r4.reset_index(inplace = True, drop = True)
    r4.columns=['Random Selection 5']
    #the segment belows combines different dataframe according to respective methods for comparison
    combinep=pd.concat([p0,p1,p2,p3,p4],axis=1)
    combinep = combinep.reset_index().rename(columns={'index': 'Loop Times/No of Generation'})
    combinep.set_index(['Loop Times/No of Generation'], inplace = True)
    combinep=combinep.reset_index().melt('Loop Times/No of Generation')

    combinem=pd.concat([m0,m1,m2,m3,m4],axis=1)
    combinem = combinem.reset_index().rename(columns={'index': 'Loop Times/No of Generation'})
    combinem.set_index(['Loop Times/No of Generation'], inplace = True)
    combinem=combinem.reset_index().melt('Loop Times/No of Generation')

    combiner=pd.concat([r0,r1,r2,r3,r4],axis=1)
    combiner = combiner.reset_index().rename(columns={'index': 'Loop Times/No of Generation'})
    combiner.set_index(['Loop Times/No of Generation'], inplace = True)
    combiner=combiner.reset_index().melt('Loop Times/No of Generation')
    #this segment calculates the data needed to compare different methods based on no of generation and time taken
    for x in range(5):
        #x,y
        totalLoop1 = totalLoop1+data.iloc[x*3  ,6]
        totalLoop2 = totalLoop2+data.iloc[x*3+1,6]
        totalLoop3 = totalLoop3+data.iloc[x*3+2,6]
        totalTime1 = totalTime1+data.iloc[x*3  ,7]
        totalTime2 = totalTime2+data.iloc[x*3+1,7]
        totalTime3 = totalTime3+data.iloc[x*3+2,7]


    #st.dataframe(data=combine)
    #st.line_chart(data=combine,height=0)
    if displayReport:
        st.write("Comparison of average fitness for each run time for pairing selection")
        chartp=alt.Chart(combinep).mark_line().encode(
        alt.Y('value',scale=alt.Scale(zero=False)),
        x='Loop Times/No of Generation',
        #y='value',
        color='variable'
        )
        st.altair_chart(chartp, use_container_width=True)

        st.write("Comparison of average fitness for each run time for tournament selection")
        chartm=alt.Chart(combinem).mark_line().encode(
        alt.Y('value',scale=alt.Scale(zero=False)),
        x='Loop Times/No of Generation',
        #y='value',
        color='variable'
        )
        st.altair_chart(chartm, use_container_width=True)
        
        st.write("Comparison of average fitness for each run time for random selection")
        chartr=alt.Chart(combiner).mark_line().encode(
        alt.Y('value',scale=alt.Scale(zero=False)),
        x='Loop Times/No of Generation',
        #y='value',
        color='variable'
        )
        st.altair_chart(chartr, use_container_width=True)

        st.write("Comparison of average Loop Needed/No of Generation for each methods")
        barData1 = {"Pairing Selection":totalLoop1/5, "Tournament Selection":totalLoop2/5,"Random Selection":totalLoop3/5}
        methods = list(barData1.keys())
        noLoop = list(barData1.values())
        fig1 = plt.figure(figsize = (10, 5))
        plt.bar(methods, noLoop, width = 0.4)
        plt.xlabel("Type of Methods")
        plt.ylabel("Average number of Loops/No of Generations Needed")
        plt.title("Average Loops/No of Generations Needed for Different Methods ")
        st.pyplot(fig1)
        st.write("Comparison of average Time taken for each methods")
        barData2 = {"Pairing Selection":totalTime1/5, "Tournament Selection":totalTime2/5,"Random Selection":totalTime3/5}
        methods = list(barData2.keys())
        totalTime = list(barData2.values())
        fig2 = plt.figure(figsize = (10, 5))
        plt.bar(methods, totalTime, width = 0.4)
        plt.xlabel("Type of Methods")
        plt.ylabel("Average Time Needed")
        plt.title("Average Time Needed for Different Methods ")
        st.pyplot(fig2)
        st.subheader("Performance Assessment")
        st.write("As we can see the average fitness value of each generation for both pairing selection and random selection gradually increases over generation. While for tournament selection it decreases sharply after first generation. This is mainly because tournament selection selects the fittest chromosome to be mated for next generation but for pairing and random the chromosomes are chosen randomly.")
        st.write("On average the number of generations needed to achieve best fit that uses up all money on-hand the lowest is tournament selection while pairing selection and random selection have nearly identical average number of generations")
        st.write("For the average time needed for different methods to complete each run to generate optimal solution for vacation plan, pairing selection has the lowest average time needed followed by random selection that are close to the pairing selection. But for tournament selection it has the highest run time due to it require going through random selection of 3 chromosome before selection fittest chromosome for pairing with another chromosome chosen in the same manner. This resulted in significant time consumed in the selection phases.")
        st.write("As conclusion we can see from the charts tournament selection have the lowest number of generation needed to get optimal solution but longest time needed . While the other two pairing selection and random selection has the identical performance.")
    elif(selectionRadio=="Pairing Selection"):
        match number:
            case 1:
                displayData=data.iloc[0]
                dispIndividual(displayData)
            case 2:
                displayData=data.iloc[3]
                dispIndividual(displayData)
            case 3:
                displayData=data.iloc[6]
                dispIndividual(displayData)
            case 4:
                displayData=data.iloc[9]
                dispIndividual(displayData)
            case 5:
                displayData=data.iloc[12]
                dispIndividual(displayData)
    elif(selectionRadio=='Tournament Selection'):
        match number:
            case 1:
                displayData=data.iloc[1]
                dispIndividual(displayData)
            case 2:
                displayData=data.iloc[4]
                dispIndividual(displayData)
            case 3:
                displayData=data.iloc[7]
                dispIndividual(displayData)
            case 4:
                displayData=data.iloc[10]
                dispIndividual(displayData)
            case 5:
                displayData=data.iloc[13]
                dispIndividual(displayData)
    elif(selectionRadio=='Random Selection'):
        match number:
            case 1:
                displayData=data.iloc[2]
                dispIndividual(displayData)
            case 2:
                displayData=data.iloc[5]
                dispIndividual(displayData)
            case 3:
                displayData=data.iloc[8]
                dispIndividual(displayData)
            case 4:
                displayData=data.iloc[11]
                dispIndividual(displayData)
            case 5:
                displayData=data.iloc[14]
                dispIndividual(displayData)