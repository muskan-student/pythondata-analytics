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
    st.balloons()

st.title("Pokemon Data Analytics")
st.subheader("A simple data app to analyze pokemon ")

st.sidebar.title("Menu")
choice = st.sidebar.radio('options',['View Data','Visualize Data','Column Analysis'])

if choice == 'View Data':
    st.header('View Dataset')
    st.dataframe(df)
elif choice == 'Visualize data':
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
elif choice == 'Column Analysis':
    columns = df.columns.tolist()
    scol= st.sidebar.selectbox('Select a column ',columns)
    if df[scol].dtype == "object":
        vc = df[scol].value_counts()
        most_common = vc.idxmax()
        c1,c2 = st.columns([3,1])
        #visualize
        fig = px.histogram(df, x= scol, title = f'Distribution of {scol}')
        c1.plotly_chart(fig, use_container_width=True)

        #values count
        c2.subheader('Total Data')
        c2.write(vc)
        c2.metric('Most Common',most_common,int(vc[most_common]))
        c1,c2 = st.columns(2)
        fig2 = px.pie(df, names = scol, title = f'Percentage wise of {scol}',
                      hole = 0.3 )
        c1.plotly_chart(fig2)
        fig3 = px.box(df,x= scol,title = f'{scol} by {scol}')
        c2.plotly_chart(fig3)
        fig4 = px.funnel_area(names= vc.index,
                              values = vc.values,
                              title = f'{scol} Funnel Area',
                              height = 600)
        st.plotly_chart(fig4 , use_container_width=True)


    else:
        tab1,tab2  = st.tabs(['Univariate','Bivariate'])
        with tab1:
            st.write('Univariate Analysis')
            score = df[scol].describe()
            fig1= px.histogram(df, x =scol,title = f'Distribution of {scol}')
            fig2 = px.box(df,x = scol,title = f'{scol} by {scol}')
            c1 ,c2 ,c3 = st.columns([1,3,3])
            c1.dataframe(score)
            c2.plotly_chart(fig1)
            c3.plotly_chart(fig2)
        with tab2:
            c1, c2 = st.columns(2)
            col2 =c1.selectbox('select a column ',df.select_dtypes(include = 'number').columns.tolist())
            color = c2.selectbox('select a color', df.select_dtypes(exclude = 'number').columns.tolist())
            fig3 = px.scatter(df, x= scol, y = col2, 
                              color = color,
                              title = f'{scol} vs {col2}' ,height =600)
            st.plotly_chart(fig3 ,use_container_width= True)
# to run this program ,open terminal and run the following command 

#streamlit run app.py