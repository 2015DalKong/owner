import streamlit as st

view = [100,150,30]
view1 = [20,40,60]

st.write("# Youtube view")
st.write('## raw')
view
view1
st.write('## bar chart')
st.bar_chart(view)
st.bar_chart(view1)

import pandas as pd
sview = pd.Series(view)
sview

sample_csv = pd.read_csv('sample.csv', encoding='cp949')
sample_csv
