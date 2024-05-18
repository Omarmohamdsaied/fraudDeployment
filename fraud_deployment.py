import pickle
import simplejson
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie




def load_lottiefile(filepath:str):
   with open(filepath,'r') as f:
      return simplejson.load(f)

lottie_coding=load_lottiefile(r"C:\Users\dell\fraudDeployment\lottie.json")
st_lottie(lottie_coding,speed=0.05,quality='high',height=300,width=700)

st.title('Fraud Detection Web APP')
st.info('Application for detecting the fraud')
#C:\Users\dell\fraudDeployment\lottie2.json

lottie2_coding=load_lottiefile(r"C:\Users\dell\fraudDeployment\lottie2.json")

st_lottie(lottie2_coding,speed=0.05,quality='high',height=300,width=700)

avgDict={'entertainment': 64.1282076003686,
 'food_dining': 51.14719567610285,
 'gas_transport': 63.43144276895249,
 'grocery_net': 53.77320441516215,
 'grocery_pos': 116.90031958968333,
 'health_fitness': 54.13658366909623,
 'home': 58.174049382716056,
 'kids_pets': 57.5266695296664,
 'misc_net': 80.84104417917796,
 'misc_pos': 62.49729978267216,
 'personal_care': 47.964401001294284,
 'shopping_net': 88.61572104865337,
 'shopping_pos': 79.13913734191257,
 'travel': 111.662196257213}

category_encode={'entertainment': 8,
 'food_dining': 11,
 'gas_transport': 9,
 'grocery_net': 0,
 'grocery_pos': 10,
 'health_fitness': 2,
 'home': 7,
 'kids_pets': 1,
 'misc_net': 4,
 'misc_pos': 5,
 'personal_care': 6,
 'shopping_net': 12,
 'shopping_pos': 13,
 'travel': 3}


data=pickle.load(open(r'C:\Users\dell\fraudDeployment\Fraud_Detection.sav','rb'))
scaledata=pickle.load(open(r'C:\Users\dell\fraudDeployment\saving stdScaler.sav','rb'))



#Time=st.text_input('Time')
category=st.selectbox('Transaction Category',['entertainment',
 'food_dining',
 'gas_transport',
 'grocery_net',
 'grocery_pos',
 'health_fitness',
 'home',
 'kids_pets',
 'misc_net',
 'misc_pos',
 'personal_care',
 'shopping_net',
 'shopping_pos',
 'travel'])

Amount=float(st.text_input('Transaction Amount'))
Hour=st.slider('Trasaction occured Hour',0,23)

Trasaction_Diff=abs(Amount-avgDict[category])

df=pd.DataFrame({'0':[category_encode[category]],'1':[Amount],
                 '2':[Hour],
                 '3':[avgDict[category]],
                 '4':[Trasaction_Diff]}
                ,index=[0])

df=scaledata.transform(df)


bt=st.button('Predict')

if bt:
    result=data.predict(df)
    if result==0:
     st.success('The Transaction is Not Fraud')
     st.balloons()
    else:
       st.error('Be Careful !! it is a FRAUD Transaction ')