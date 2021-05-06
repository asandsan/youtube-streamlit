import streamlit as st
import time

st.title('streamlit 超入門')

# st.write('Display Image')

st.write('Display Progresbar')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
'Done!!'

left_column,right_column = st.beta_columns(2)
botton = left_column.button('右カラムに文字を表示')
if botton:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')

expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')


# if st.checkbox('Show Image'):
#     img = Image.open('test.jpeg')
#     st.image(img,caption='test',use_column_width=True)


# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、',option,'です。'

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味は、',text,''


# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディショ
# left_column,right_column = st.beta_columns(2)ン',condition,''



# st.write('Dataframe')

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# df
# st.line_chart(df)

# st.dataframe(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] +[35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)


