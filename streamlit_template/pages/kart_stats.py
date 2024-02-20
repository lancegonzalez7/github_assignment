import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')
df_kart_lim_col = df_kart[['Body','Weight','Acceleration','On-Road Traction','Off-Road Traction','Mini-Turbo']]

st.dataframe(df_kart)

st.dataframe(df_kart_lim_col.style
             .highlight_max(color="lightgreen", axis=0, subset=['Weight','Acceleration','On-Road Traction','Off-Road Traction','Mini-Turbo'])
             .highlight_min(color="pink", axis=0, subset=['Weight','Acceleration','On-Road Traction','Off-Road Traction','Mini-Turbo']))


st.scatter_chart(df_kart, x = 'Air Speed', y= 'Air Handling', color='Body', size=500)

st.line_chart(df_kart_lim_col, x='Acceleration', y=['Weight','On-Road Traction','Off-Road Traction','Mini-Turbo'])

chosen_kart = st.selectbox('Pick a Kart',df_kart['Body'])

df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]

sf_single_kart = df_single_kart.drop(columns=['Body'])

df_ump_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)

st.bar_chart(df_ump_kart, x='category',y='strength')