import streamlit as st 

st.sidebar.title('This is a sidebar')
st.sidebar.write('You can place element here like sliders, buttons, and text')

sidebar_input = st.sidebar.text_input("Enter something")

#Tabs layout

tab1, tab2, tab3 = st.tabs(['TAB 1', 'TAB 2', 'TAB 3'])

with tab1:
    st.write('this is the TAB 1')

with tab2:
    st.write('this is the TAB 2')

with tab3:
    st.write('this is the TAB 3')

col1, col2, = st.columns(2)

with col1:
    st.header('COLUMNA 1')
    st.write('content for column 1')

with col2:
    st.header('COLUMNA 2')
    st.write('content for column 2')


placeholder = st.empty()
placeholder.write("This is a emply placeholder, usful for dinamyc contecnt")

if st.button('Update Placeholder'):
    placeholder.write("Placeholder UPDATED")

with st.expander("Expand for more details"):
    st.write("Las cosas mas tribiales se vuelven fundamentales")