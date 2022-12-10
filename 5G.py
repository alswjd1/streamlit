import requests
import xmltodict
import time
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title='권역별 5G 전송속도',
    page_icon='📱'
)
data=pd.read_csv('5G전송속도.csv',encoding='cp949', thousands=',')
data=data.astype({'다운로드(Mbps)':'float','업로드(Mbps)':'float'})

menu=st.sidebar.selectbox('지역',data['구분(지역)'].drop_duplicates())

plt.rc('font',family='Malgun Gothic')


temp=data[data['구분(지역)']==menu]
# plt.plot(temp['createDt'], temp['natDefCnt'], label=value)

print(temp)

temp = temp['다운로드(Mbps)']
plt.bar(['SKT','KT','LG'], temp, color='pink', width=0.5)
plt.title('권역별 5G 전송속도')
plt.ylabel('다운로드(Mbps)')
plt.xlabel('통신사')
plt.show()


st.pyplot(plt)
#st.table(df2)