import pandas as pdimport streamlit as stimport plotly.express as pximport numpy as npdef get_data():    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&interval=60min&slice=year10month12&datatype=csv&apikey=0L9YO5H4PCYBKRP3'    return pd.read_csv(url)df = get_data()df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')df['year'] = df['timestamp'].dt.yeardf['month'] = df['timestamp'].dt.monthdf['day'] = df['timestamp'].dt.dayst.title("Web Apps with Flask and Streamlit")df_plot= df[df['year'] == 1999]st.markdown("Select plot parameter:")year_options = st.selectbox(     'Select which year',np.unique(df['year']) )df_plot= df[df['year'] == year_options]fig = px.line(df_plot, x="month", y="close", title='Chart of stock closing prices in '+str(year_options))st.plotly_chart(fig , use_container_width=True)