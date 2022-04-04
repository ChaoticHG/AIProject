from math import ceil

import streamlit as st
import matplotlib as plt
import pandas as pd

def app():
    def writeDetails(totalPopulationA,totalPopulationB,totalPopulationC,dailyLimit,vacList,centreList):
        daysneeded = ceil((totalPopulationA+totalPopulationB+totalPopulationC)/dailyLimit)
        centreNeeded = "Vaccination Centre Type Needed             : "
        for a in range(5):
            if(centreList.iloc[0,a]!=0):
                centreNeeded +=  "Centre " + str(a+1) + " x " + str( centreList.iloc[0,a] ) + " "
        st.write("Total Day Needed         : " + str(daysneeded) + " Days")
        st.write("Rental per day           : RM " + str(centreList.iloc[0,5]))
        st.write("Total Vaccine A per day  : " + str(vacList.iloc[0,0]))
        st.write("Total Vaccine A last day : " + str(vacList.iloc[0,3]))
        st.write("Total Vaccine B per day  : " + str(vacList.iloc[0,1]))
        st.write("Total Vaccine B last day : " + str(vacList.iloc[0,4]))
        st.write("Total Vaccine C per day  : " + str(vacList.iloc[0,2]))
        st.write("Total Vaccine C last day : " + str(vacList.iloc[0,5]))
        st.write("Maximum total vaccine distribution per day : " + str(vacList.iloc[0,7]))
        st.write(centreNeeded)

    dict1 = {'va' : 'Daily Vaccine A Distribution',
            'vb' : 'Daily Vaccine B Distribution',
            'vc' : 'Daily Vaccine C Distribution',
            'finalva' : 'Last Day Vaccine A Distribution',
            'finalvb' : 'Last Day Vaccine B Distribution',
            'finalvc' : 'Last Day Vaccine C Distribution',
            'differ'  : 'Total Difference',
            'maxpop'  : 'Minimum Size Needed',
                    }


    st.title("Question 2")

    st1vac= pd.read_csv('st1vac.csv', header=0)
    st1centre= pd.read_csv('st1centre.csv', header=0)
    st1vac = st1vac[['va','vb','vc','finalva','finalvb','finalvc','differ','maxpop']]
    st1vac.rename(columns=dict1,inplace=True)
    st1centre = st1centre[['cr1','cr2','cr3','cr4','cr5','cost']]

    st2vac= pd.read_csv('st2vac.csv', header=0)
    st2centre= pd.read_csv('st2centre.csv', header=0)
    st2vac = st2vac[['va','vb','vc','finalva','finalvb','finalvc','differ','maxpop']]
    st2vac.rename(columns=dict1,inplace=True)
    st2centre = st2centre[['cr1','cr2','cr3','cr4','cr5','cost']]

    st3vac= pd.read_csv('st3vac.csv', header=0)
    st3centre= pd.read_csv('st3centre.csv', header=0)
    st3vac = st3vac[['va','vb','vc','finalva','finalvb','finalvc','differ','maxpop']]
    st3vac.rename(columns=dict1,inplace=True)
    st3centre = st3centre[['cr1','cr2','cr3','cr4','cr5','cost']]

    st4vac= pd.read_csv('st4vac.csv', header=0)
    st4centre= pd.read_csv('st4centre.csv', header=0)
    st4vac = st4vac[['va','vb','vc','finalva','finalvb','finalvc','differ','maxpop']]
    st4vac.rename(columns=dict1,inplace=True)
    st4centre = st4centre[['cr1','cr2','cr3','cr4','cr5','cost']]

    st5vac= pd.read_csv('st5vac.csv', header=0)
    st5centre= pd.read_csv('st5centre.csv', header=0)
    st5vac = st5vac[['va','vb','vc','finalva','finalvb','finalvc','differ','maxpop']]
    st5vac.rename(columns=dict1,inplace=True)
    st5centre = st5centre[['cr1','cr2','cr3','cr4','cr5','cost']]

    vacDistOption = st.multiselect("States: ",
                        ['ST1', 'ST2', 'ST3','ST4','ST5'])
    show=st.checkbox("Show/Hide All Possible Combinations",value=False)

    if 'ST1' in vacDistOption:
        st.write("ST1")
        writeDetails(15000,434890,115900,5000,st1vac,st1centre)
        #st.write(st1vac.iloc[0,4])
        #st.write(st1vac.iloc[0,2])
        if show:
            st.dataframe(data=st1vac)
            st.dataframe(data=st1centre)

    if 'ST2' in vacDistOption:
        st.write("ST2")
        writeDetails(35234,378860,100450,10000,st2vac,st2centre)
        if show:
            st.dataframe(data=st2vac)
            st.dataframe(data=st2centre)

    if 'ST3' in vacDistOption:
        st.write("ST3")
        writeDetails(22318,643320,223400,7500,st3vac,st3centre)
        if show:
            st.dataframe(data=st3vac)
            st.dataframe(data=st3centre)

    if 'ST4' in vacDistOption:
        st.write("ST4")
        writeDetails(23893,859900,269300,8500,st4vac,st4centre)
        if show:
            st.dataframe(data=st4vac)
            st.dataframe(data=st4centre)

    if 'ST5' in vacDistOption:
        st.write("ST5")
        writeDetails(19284,450500,221100,9500,st5vac,st5centre)
        if show:
            st.dataframe(data=st5vac)
            st.dataframe(data=st5centre)

