import streamlit as st, altair as alt
from urllib.error import URLError
import pandas as pd, numpy as np
from datetime import datetime
import time as t

def tell_time():
    time = datetime.now().strftime("%H:%M:%S")
    timeset = time.split(':')
    if timeset[0] < '12' and timeset[0] >= '00':
        return '🌇 Good morning!'
    elif timeset[0] >= "12" and timeset[0] < "16":
        return "🌞 Good afternoon!"
    elif timeset[0]>='16':
        return "🌆 Good evening!"
    
# Function to configure st.session_states
def reset_for(name:str):
    # Configuring st.session_state for st.session_state['my_nation']
    if name == 'my_nation':
        try:
            st.session_state['my_state'] = []
            st.session_state['my_market'] = []
            st.session_state['my_year'] = []
            st.session_state['my_produce'] = []
            return
        except:
            pass
            st.stop()

    if name == 'my_state':
        # Configuring st.session_state for st.session_state['my_state']
        try:
            st.session_state['my_nation'] = []
            st.session_state['my_market'] = []
            st.session_state['my_year'] = []
            st.session_state['my_produce'] = []
            return
        except:
            pass
            st.stop()

    if name == 'my_market':
        # Configuring st.session_state for st.session_state['my_market']
        try:
            st.session_state['my_state'] = []
            st.session_state['my_nation'] = []
            st.session_state['my_year'] = []
            st.session_state['my_produce'] = []
            return
        except:
            pass
            st.stop()

    if name == 'my_year':
        # Configuring st.session_state for st.session_state['my_year']
        try:
            st.session_state['my_state'] = []
            st.session_state['my_market'] = []
            st.session_state['my_nation'] = []
            st.session_state['my_produce'] = []
            return
        except:
            pass
            st.stop()

    if name == 'my_produce':
        # Configuring st.session_state for st.session_state['my_produce']
        try:
            st.session_state['my_state'] = []
            st.session_state['my_market'] = []
            st.session_state['my_year'] = []
            st.session_state['my_nation'] = []
            return
        except:
            pass
            st.stop()


@st.cache_data
def get_data():
    # Loading data from my drive.
    path = "datasets/cleaned_food_prices.parquet"
    df = pd.read_parquet(path)
    
    # Transforming columns
    df['year'] = df['year'].astype('str')
    df['id'] = df['id'].astype('str')
    df['month'] = df['month'].astype('str')

    # Returning dataset.
    return df

# To set my page details.
st.set_page_config(
    page_title = "Home Page",
    page_icon = "🏠",
    layout = 'wide'
    )
st.sidebar.success("Clik INFO after filtering data at the HOME")

try:
    ''' # African Food Prices Quickview.'''
    st.markdown(f'''
                * {tell_time()}
                * Use filter to narrow your findings.
                * The table can only be filtered by **country**, **state**, **market_type**, **produce** and **year**.
                * Quickview for your filtered data is available at the "Info" bar on your screen to the left.
                ''')
    data = get_data()
    st.header('African food prices data')
    st.dataframe(data)

    # Sending unique values to variables to develop a multiselect container.
    NATION = data['country'].unique()
    STATE = data['state'].unique()
    YEAR = data['year'].unique()
    MARKET_TYPE = data['market_type'].unique()
    PRODUCE = data['produce'].unique()

    # Creating session state to hold filtered data.
    if 'my_filter' not in st.session_state:
        st.session_state['my_filter'] = []

    # Creating columns to hold multiselect container
    col1, col2, col3 = st.columns(3)

    # Creating filter for countries.
    nation = col1.multiselect("Track prices by country here: ",
                              NATION,
                              key = 'my_nation')
    state = col2.multiselect('Track prices by state here: ',
                             STATE,
                             key = 'my_state')
    year = col3.multiselect('Track prices by year here: ',
                            YEAR,
                            key = 'my_year')
    
    # Creating columns to hold multiselect containers for produce and market filter
    col1, col2 = st.columns(2)

    # Creating filters for produce and market
    market = col1.multiselect('Track prices by market here: ',
                              MARKET_TYPE,
                              key = 'my_market')
    produce = col2.multiselect('Track prices by produce here: ',
                               PRODUCE,
                               key = 'my_produce')


    # Creating button.
    done = st.button("Filter",
                     help = "Click here to filter your dataset.")
    '___'

    # Action to do on clicking the 'filter' button.
    if done:
            col1, col2 = st.columns(2)
            col1.write('Original Data')
            col1.dataframe(data)

    # Filtering from the countries filter.
            if nation:
                with st.balloons():
                    t.sleep(3)

                filtered = data[data['country'].isin(nation)]
                col2.write('Filtered Dataset')
                col2.dataframe(filtered)
                st.session_state['my_filter'] = filtered
                st.info(f'This data is filtered by country {nation}', icon  = '🌍')
                reset_for('my_nation')
                st.stop()
                
                          
    # Filtering from the state filter.
            if state:
                with st.balloons():
                    t.sleep(3)

                filtered = data[data['state'].isin(state)]
                col2.write('Filtered Dataset')
                col2.dataframe(filtered)
                st.session_state['my_filter'] = filtered
                st.info(f'This data is filtered by {state}', icon  = '🌍')
                reset_for('my_state')
                st.stop()
                

    # Filtering from the year filter.
            if year:
                with st.snow():
                    t.sleep(5)

                filtered = data[data['year'].isin(year)]
                col2.write('Filtered Dataset')
                col2.dataframe(filtered)
                st.session_state['my_filter'] = filtered
                st.info(f'This data is filtered by years {year}', icon = "🗓️")
                reset_for('my_year')
                st.stop()

    # Filtering from the market filter.
            if market:
                with st.balloons():
                    t.sleep(3)

                filtered = data[data['market_type'].isin(market)]
                col2.write('Filtered Dataset')
                col2.dataframe(filtered)
                st.session_state['my_filter'] = filtered
                st.info(f'This data is filtered by {market}', icon = '🛒')
                reset_for('my_market')
                st.stop()
            
    # Filtering from the produce filter.
            if produce:
                with st.balloons():
                    t.sleep(3)

                filtered = data[data['produce'].isin(produce)]
                col2.write('Filtered Dataset')
                col2.dataframe(filtered)
                st.session_state['my_filter'] = filtered
                st.info(f'This data is filtered by {produce}', icon = '🛍️')
                reset_for('my_produce')
                st.stop()

    # The button updates the value in the st.session_state['my_filter'] with the filtered table.

except URLError as err:
    st.error("""We could not load site due to:
              %s
             """
             % err.reason)