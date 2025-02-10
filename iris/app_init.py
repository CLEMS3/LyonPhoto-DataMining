# import the library to create web app
import streamlit as st 
# dataframe
import pandas as pd

# plotting
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# a function that load the dataset
# to cache data objects to avoid reloading them each time 
@st.cache_data(persist=True)
def load_data(filename="data/IrisDataset/data.all", sep=" ") -> pd.DataFrame:
    """
    Loads data to a pandas DataFrame

    Args:
        filename (str, optional): Name of the file to be loaded. Defaults to "data/IrisDataset/data.all".
        sep (str, optional): Separator of the data column. Defaults to " ".

    Returns:
        data: a DataFrame contanining loaded data
    """
    data = pd.read_table(filename, sep=sep)
    
    return data

def pairplot(data, cols_list):
    """
    Displays a pairplot of features given in cols_list from data dataframe. 
    Two implementations are given: (1) seaborn.pairplot, (2) plotly.express  

    Args:
        data (pd.DataFrame): A DataFrame containing data to display
        cols_list: A list of attributes (columns to consider)
    """
    st.subheader("Pairplot with `seaborn`")
    # Create pairplot
    fig = plt.figure()
    sns.pairplot(data[cols_list])

    # Display in Streamlit
    st.pyplot(plt.gcf())
    
    st.subheader("Paiplot with `plotly.express`")
    fig = px.scatter_matrix(data,
                            dimensions=cols_list,
                            title="Interactive Pairplot"
                        )
    st.plotly_chart(fig)

def main():
    """
    The logic of the app will be written here.
    """
    # add a title to the main page
    st.title("Clustering IRIS dataset")

    # to run the app, run the command "streamlit run app_init.py" in the terminal

    # add markdown
    st.markdown("This project is an application of clustering techniques to the IRIS dataset")

    # save the changes
    # in the app, you can click on "Always rerun" to apply saved changes automatically

    # to add a header
    # st.header("IRIS Dataset")

    # # to add an image into the main part of the window
    # st.image('img/iris-flower-types.png')
    
    # # add a header to a sidebar
    # st.sidebar.header("Raw data")
    
    # # load data and show the dataframe
    # df = load_data(filename="data/IrisDataset/data.all", sep=" ")
    # st.write(df)
    
    # # to a sidebar add a multiselect to select features to be displayed
    # cols = list(df.columns) # all columns
    # def_cols = cols[:-1] # default columns
    # selected_features = st.sidebar.multiselect("Choose attributes to consider", options=cols, default=def_cols)
    # df_selection = df[selected_features]
    
    # # add a checkbox to display the subset of the dataframe
    # if st.sidebar.checkbox("Show dataset with selected attributes"):
    #     st.markdown(f"Dataset with selected attributes")
    #     st.write(df_selection)
        
    # # add a header to a sidebar
    # st.sidebar.header("Pairplot")
    # # add a button to a sidebar
    # if st.sidebar.button("Show pairplot"):
    #     pairplot(df, selected_features)
        
if __name__ == '__main__':
    main()

