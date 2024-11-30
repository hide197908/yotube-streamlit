import streamlit as st
from PIL import Image

st.title('Streamlit入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration=st.empty()
bar=st.progress(0)

import time

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}%')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column = st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここに右からむ')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3=st.expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')
#text= st.text_input('あなたの趣味を教えてください')

#condition=st.slider('あなたの今の調子は',0,100,50)

#text= st.sidebar.text_input('あなたの趣味を教えてください')
#'あなたの好きな趣味は、',option,'です'

#condition=st.sidebar.slider('あなたの今の調子は',0,100,50)
#'コンディション',condition,'です'
#'あなたの好きな趣味',text
#'コンディション：',condition


#option = st.selectbox(
##    'あなたが好きな数値を教えてください',
#    list(range(1,11))
#)

#'あなたの好きな数字は、',option,'です'

#if st.checkbox('Show Image'):
#    img=Image.open('IMG_5716.jpg')
#    st.image(img,caption='SLOT image',use_container_width=True)


#df = pd.DataFrame(
#np.random.rand(100,2)/[50,50]+[35.69,139.70],
##columns=['lat','lon']
#)
#表
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0))
#チャート
#st.bar_chart(df)
#地図
#st.map(df)