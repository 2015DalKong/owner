import streamlit as st
import random
import datetime

st.title(':sparkles:로또 생성기:sparkles:')


def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto

# st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
# st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button('로또를 생성해 주세요!')

if button:
    for i in range(1, 6):
        st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
    st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")





# import streamlit as st

# view = [100,150,30]
# view1 = [20,40,60]

# st.write("# Youtube view")
# st.write('## raw23')
# view
# view1
# st.write('## bar chart')
# st.bar_chart(view)
# st.bar_chart(view1)

# import pandas as pd
# sview = pd.Series(view)
# sview


# # csv_url = 'https://raw.githubusercontent.com/2015DalKong/repo/master/sample.csv'
# # 으로
# # /owner/edit/main/sample.csv

# sample_csv = pd.read_csv('sample.csv')
# sample_csv
