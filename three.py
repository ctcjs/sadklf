import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='🍊南宁美食地图🍊')
data={
    '月份':['01月','02月','03月'],
    '1号门店':[200,150,180],
    '2号门店':[120,160,123],
    '3号门店':[110,100,60],}
df=pd.DataFrame(data)
index=pd.Series(['a','s','c'],name="编号")
df.index=index
st.table(df)
