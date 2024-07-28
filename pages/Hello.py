import streamlit as st
import login

login.generarLogin()
if 'usuario' in st.session_state:
    st.header('Página :blue[1]')
    
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.p
#python get-pip.py

#python install matplotlib

#python -m pip install \
#  --upgrade \
#  --pre \
#  --index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/simple \
#  --extra-index-url https://pypi.org/simple \
#  matplotlib
#import matplotlib.pyplot as plt

x=(1,2,3,4,5,6,7)

#histograma = plt.hist(x)
print(1)
#fig, ax = plt.subplots()
#ax.hist(x, bins=20)
#plt.show()
#st.pyplot(fig)
#st.bar_chart(x)
print(2)
st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
