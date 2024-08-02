import streamlit as st 
import pandas as pd
import plotly.express as px 

# ui configuration
st.set_page_config(
    page_title ="Pokemon App",
    page_icon =" 😊",
    layout = 'wide'
)
# load data
@st.cache_data
def load_data():
    return pd.read_csv ('pokemon.csv', index_col="#")
#ui integration
with st.spinner ('loading dataset...'):
    df = load_data()
    #st.balloons()

st.title("Pokemon Data Analytics")
st.subheader("A simple data app to analyze pokemon ")

st.sidebar.title("Menu")
choice = st.sidebar.radio('options',['View Data','Visualize Data'])

if choice == 'View Data':
    st.header('View Dataset')
    st.dataframe(df)
else:
    st.header('Visualization')
    '''scol= st.sidebar.radio('select a column ', df.columns)
    st.write(f"### Visualizing {scol}")
    if df[scol].dtype =="object":
        total_unique_values = df[scol].nunique()
        st.write(f"total unique values : {total_unique_values}")
    elif df[scol].dtype =='int64':
        st.write(f'Min value :{df [scol].min()}')
        st.write(f'Max value :{df [scol].max()}')
        st.write(f'Mean value :{df [scol].mean()}')'''
    cat_cols= df.select_dtypes(include ='object').columns.tolist()
    num_cols = df.select_dtypes(exclude = 'object').columns.tolist()
    # st.write(cat_cols)
    # st.write(num_cols)
    cat_cols.remove('Name')
    num_cols.remove('Generation')
    cat_cols.append('Generation')
    num_cols.remove('Legendary')
    cat_cols.append('Legendary')

    snum_col =st.sidebar.selectbox('Select a numeric column',num_cols)
    scat_col = st.sidebar.selectbox('select a catgorical columns',cat_cols)

    c1,c2 = st.columns(2)
    #visualize numerical column 
    fig1 = px.histogram(df,
        x = snum_col,
        title = f'Distribution of {snum_col}'
    )
     #visualize categorical column 
    fig2 = px.pie(df,
            names= scat_col,
            title= f'Disribution of {scat_col}',
            hole= 0.3
    )            
    c1.plotly_chart(fig1)
    c2.plotly_chart(fig2)
# to run this program ,open terminal and run the following command 

#streamlit run app.py