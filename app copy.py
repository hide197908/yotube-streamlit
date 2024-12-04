import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st
import time

st.title('米国株価可視化アプリ')
st.sidebar.write("""
# GAFA株価
こちらは株価可視化ツールです。以下のオプションで日付を選んでください
""")
st.sidebar.write("""
##表示日数選択
""")

days=st.sidebar.slider('日数',1,50,20)

st.write(f"""
### 過去 **{days}日間**のGAFAの株価
""")



@st.cache_data
def get_data(days,tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr=yf.Ticker(tickers[company])
        hist=tkr.history(period=f'{days}d')
        #hist.index = hist.index.strftime('%d %B %Y')
        hist=hist[['Close']]
        hist.columns =[company]
        hist =hist.T
        hist.index.name='NAME'
        df = pd.concat([df,hist])
        
    return df


st.sidebar.write("""
## 株価の範囲指定
""")
ymin,ymax=st.sidebar.slider(
    '範囲を指定してください',
    0.0,3500.0,(0.0,3500.0)
)

tickers={
    'apple': 'AAPL',
    'google': 'GOOGL',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}

df=get_data(days,tickers)
st.write(df)



companies=st.multiselect(
    '会社名を選択してください',
    list(df.index),
    ['google','amazon','facebook','apple']
)

if not companies :
    st.error('少なくとも1社は選んでください')
else:
    data=df.loc[companies]
    st.write("### 株価 (USD)",data.sort_index())
