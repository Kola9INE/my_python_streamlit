import streamlit as st
import pandas as pd, numpy as np
import statistics as stats
import Home as hm
import altair as at

def not_available():
    st.snow()
    st.info(f"""## {'🚧'} {'⛔'} Ooops! SORRY, THIS FEATURE IS STILL IN PROGRESS... {'⚠️'}{'🧑‍🔧'} """)
    st.stop()
    return

try:
    # If user filtered by country
    if st.session_state['my_nation'] != []:

        st.set_page_config(
            page_title = 'Quickview',
            page_icon = "📓",
            layout = 'wide'
        )

        st.write('FILTERED DATASET')
        st.dataframe(st.session_state['my_filter'])

        # Creating metric values
        ROWS = hm.data.shape[0]
        COLUMNS = hm.data.shape[1]
        rows = st.session_state['my_filter'].shape[0]
        columns = st.session_state['my_filter'].shape[1]
        TOTAL = round(np.sum(hm.data['price'])/1000000000, 2)
        total = round(np.sum(st.session_state['my_filter']['price'])/1000000, 2)
        mean = round(stats.mean(st.session_state['my_filter']['price']), 2)
        MEAN = round(stats.mean(hm.data['price']), 2)
        MODE = stats.mode(hm.data['price'])
        mode = stats.mode(st.session_state['my_filter']['price'])
        MAX_price = np.round(hm.data['price'].max()/1000000, 2)
        max_price = st.session_state['my_filter']['price'].max()
        FEATURED_PROD = hm.data['produce'].nunique()
        featured_prod = st.session_state['my_filter']['produce'].nunique()
        FEATURED_MARKET = hm.data['market'].nunique()
        featured_market = st.session_state['my_filter']['market'].nunique()
        FEATURED_STATE = hm.data['state'].nunique()
        featured_state = st.session_state['my_filter']['state'].nunique()
        FEATURED_YEAR = hm.data['year'].nunique()
        featured_year = st.session_state['my_filter']['year'].nunique()

        with st.expander('SEE SUMMARY METRICS', expanded = False):
            # Creating info metric:
            # 1. For Columns
            col1, col2 = st.columns(2)
            col1.metric("TOTAL ROWS IN ORIGINAL DATA", ROWS)
            col2.metric("TOTAL ROWS IN FILTERED DATA", rows)
            # 2. For Rows
            col1, col2 = st.columns(2)
            col1.metric("TOTAL COLUMNS IN ORIGINAL DATA", COLUMNS)
            col2.metric("TOTAL COLUMNS IN FILTERED DATA", columns)
                    

            # Creating total metric
            col1, col2 = st.columns(2)
            col1.metric("TOTAL PRICE OF ORIGINAL DATA (Billions)", TOTAL)
            col2.metric('TOTAL PRICE OF FILTERED DATA (Millions)', total)

            # Creating mean metric
            col1, col2 = st.columns(2)
            col1.metric('MEAN PRICE OF ORIGINAL DATA', MEAN)
            col2.metric('MEAN PRICE OF FILTERED DATA', mean)

            # Creating mode metric
            col1. col2 = st.columns(2)
            col1.metric('MOST OCCURING PRICE IN ORIGINAL DATA', MODE)
            col2.metric('MOST OCCURING PRICE IN FILTERED DATA', mode)

            # Creating max price metric
            col1, col2 = st.columns(2)
            col1.metric('MAX PRICE IN ORIGINAL DATASET (MILLIONS)', MAX_price)
            col2.metric('MAX PRICE IN FILTERED DATASET', max_price)

            # Creating metric for number of featured products
            col1, col2 = st.columns(2)
            col1.metric('NUMBER OF PRODUCE FEATURED IN ORIGINAL DATA', FEATURED_PROD)
            col2.metric('NUMBER OF PRODUCE FEATURED IN FILTERED DATA', featured_prod)

            # Creating metric for amount of featured markets
            col1, col2 = st.columns(2)
            col1.metric('AMOUNT OF MARKETS FEATURED IN ORIGINAL DATA', FEATURED_MARKET)
            col2.metric('AMOUNT OF MARKETS FEATURED IN FILTERED DATA', featured_market)

            # Creating metric for amount of featured states
            col1, col2 = st.columns(2)
            col1.metric('AMOUNT OF STATES FEATURED IN ORIGINAL DATA', FEATURED_STATE)
            col2.metric('AMOUNT OF STATES FEATURED IN FILTERED DATA', featured_state)

            # Creating metric for amount of featured years
            col1, col2 = st.columns(2)
            col1.metric('AMOUNT OF YEARS FEATURED IN ORIGINAL DATA', FEATURED_YEAR)
            col2.metric('AMOUNT OF YEARS FEATURED IN FILTERED DATA', featured_year)

        '___'

        # Visualizing the top ten produce by price in Africa
        col1, col2 = st.columns(2)
        col1.markdown('TOP TEN PRODUCE BY PRICE IN AFRICA')
        bar1 = hm.data.groupby(['produce'])['price'].sum().nlargest(n=10).sort_values(ascending = False)
        col1.bar_chart(bar1)

        # Visualizing the top the produce by price in st.session_state['my_nation']
        col2.markdown('TOP TEN PRODUCE BY PRICE IN FILTERED DATA')
        F_Bar1 = st.session_state['my_filter'].groupby(['produce'])['price'].sum().nlargest(n=10).sort_values(ascending = False)
        col2.bar_chart(F_Bar1)

        # Visualizing the top ten produce as table in st.expander container
        with st.expander('COMPARE TABLES'):
            col1, col2 = st.columns(2)
            col1.write('Top ten produce by price in Africa')
            col1.dataframe(bar1)
            col2.write(f'Top ten produce by price in {st.session_state['my_nation']}')
            col2.dataframe(F_Bar1)

        # Visualizing the least ten produce by price in Africa
        col1, col2 = st.columns(2)
        col1.markdown('BOTTOM TEN PRODUCE BY PRICE IN AFRICA')
        bar2 = hm.data.groupby(['produce'])['price'].sum().nsmallest(n=10).sort_values(ascending = False)
        col1.bar_chart(bar2)

        # Visualizing the least ten produce by price in st.session_state['my_nation']
        col2.markdown('BOTTOM TEN PRODUCE BY PRICE IN FILTERED DATA')
        F_Bar2 = st.session_state['my_filter'].groupby(['produce'])['price'].sum().nsmallest(n=10).sort_values(ascending = False)
        col2.bar_chart(F_Bar2)

        # Visualizing the bottom ten produce as table in st.expander container
        with st.expander('COMPARE TABLES'):
            col1, col2 = st.columns(2)
            col1.write('Bottom ten produce by price in Africa')
            col1.dataframe(bar2)
            col2.write('Bottom ten produce by price in filtered data')
            col2.dataframe(F_Bar2)

        "___"
        # Visualizing price performance by years in st.session_state['my_filter'] in st.expander container
        with st.expander('SEE HOW PRICE PERFORMED ACROSS THE YEARS', expanded = False):
            ln_data = st.session_state['my_filter'].groupby(['year'])['price'].sum()
            col1, col2, col3 = st.columns(3)
            col1.dataframe(ln_data)
            col2.bar_chart(ln_data)

            # Showing highest year and lowest year by price
            ln_df = pd.DataFrame(ln_data)
            ln_df = ln_df.sort_values('price', ascending = False)

            col3.write("HIGHEST PERFORMING YEAR BY PRICE")
            col3.write(ln_df[ln_df['price'] == ln_df.price.max()])
            col3.write('LOWEST PERFORMING YEAR BY PRICE')
            col3.write(ln_df[ln_df['price'] == ln_df.price.min()])
        
        # Visualizing price performance by state in st.session_state['my_filter'] in st.expander container
        with st.expander(f'SEE HOW PRICE PERFORMED ACROSS THE STATES IN {st.session_state['my_nation']}', expanded= False):
            states_data = st.session_state['my_filter'].groupby(['state'])['price'].sum()
            col1, col2, col3 = st.columns(3)
            col1.dataframe(states_data)
            col2.bar_chart(states_data)

            # Showing highest and lowest state by price
            state_df = pd.DataFrame(states_data)
            state_df = state_df.sort_values('price', ascending = False)

            col3.write('HIGHEST PERFORMING STATE BY PRICE')
            col3.write(state_df[state_df['price'] == state_df.price.max()])
            col3.write('LOWEST PERFORMING STATE BY PRICE')
            col3.write(state_df[state_df['price'] == state_df.price.min()])

        # Visualizing price performance by market in st.session_state['my_filter'] in st.expander container
        with st.expander(f'SEE HOW PRICE PERFORMED ACROSS THE MARKETS IN {st.session_state['my_nation']}', expanded= False):
            mkt_data = st.session_state['my_filter'].groupby(['market'])['price'].sum()
            col1, col2, col3 = st.columns(3)
            col1.dataframe(mkt_data)
            col2.bar_chart(mkt_data)

            # Showing highest and lowest market by price
            mkt_df = pd.DataFrame(mkt_data)
            mkt_df = mkt_df.sort_values('price', ascending = False)

            col3.write('HIGHEST PERFORMING MARKET BY PRICE')
            col3.write(mkt_df[mkt_df['price'] == mkt_df.price.max()])
            col3.write('LOWEST PERFORMING MARKET BY PRICE')
            col3.write(mkt_df[mkt_df['price'] == mkt_df.price.min()])

        # Visualizing price performance by market_type in st.session_state['my_filter'] in st.expander container
        with st.expander(f'SEE HOW PRICE PERFORMED ACROSS THE MARKET_TYPE IN {st.session_state['my_nation']}', expanded= False):
            mktyp_data = st.session_state['my_filter'].groupby(['market_type'])['price'].sum()
            col1, col2, col3 = st.columns(3)
            col1.dataframe(mktyp_data)
            col2.bar_chart(mktyp_data)

            # Showing highest and lowest market_type by price
            mktyp_df = pd.DataFrame(mktyp_data)
            mktyp_df = mktyp_df.sort_values('price', ascending = False)

            col3.write('HIGHEST PERFORMING MARKET_TYPE BY PRICE')
            col3.write(mktyp_df[mktyp_df['price'] == mktyp_df.price.max()])
            col3.write('LOWEST PERFORMING MARKET_TYPE BY PRICE')
            col3.write(mktyp_df[mktyp_df['price'] == mktyp_df.price.min()])

        "___"
        # Visualizing price progression across the last three recorded years in tab containers
        '''## SEE PRICE PROGRESSION IN RECENT THREE YEARS'''
            
        my_filtered_year = pd.Series(st.session_state['my_filter']['year'].unique())
        last_3_years = my_filtered_year.sort_values().tail(3)

        tab1, tab2, tab3 = st.tabs([f'Price progress in the months of {last_3_years.iloc[0]}', f'Price progress in the months of {last_3_years.iloc[1]}', f'Price progress in the months of {last_3_years.iloc[2]}'])
        # In tab1
        with tab1:
            st.header(f'Price progression in {last_3_years.iloc[0]}')
            alt_chart = st.session_state['my_filter'][st.session_state['my_filter']['year']== last_3_years.iloc[0]]
            chart = (
            at.Chart(alt_chart)
            .mark_area(opacity = 0.3)
            .encode(
                x = "date",
                y = at.Y("price", stack=None)
                )
            )
            st.altair_chart (chart, use_container_width=True)

        # In tab2
        with tab2:
            st.header(f'Price progression in {last_3_years.iloc[1]}')
            alt_chart = st.session_state['my_filter'][st.session_state['my_filter']['year']== last_3_years.iloc[1]]
            chart = (
            at.Chart(alt_chart)
            .mark_area(opacity = 0.3)
            .encode(
                x = "date",
                y = at.Y("price", stack=None)
                 )
            )
            st.altair_chart (chart, use_container_width=True)
            
        # In tab3
        with tab3:
            st.header(f'Price progression in {last_3_years.iloc[2]}')
            alt_chart = st.session_state['my_filter'][st.session_state['my_filter']['year']== last_3_years.iloc[2]]
            chart = (
            at.Chart(alt_chart)
            .mark_area(opacity = 0.3)
            .encode(
                x = "date",
                y = at.Y("price", stack=None)
                )
            )
            st.altair_chart (chart, use_container_width=True)

        st.stop()

    if st.session_state['my_state'] != []:
        not_available()

    if st.session_state['my_year'] != []:
        not_available()

    if st.session_state['my_market'] != []:
        not_available()

    if st.session_state['my_produce'] != []:
        not_available()
  
except:
    not_available()