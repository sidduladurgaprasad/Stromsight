import streamlit as st
from multiapp import MultiApp
from apps import home, cyclone_app, preventive_measures  # import your app modules here

# Initialize MultiApp
app = MultiApp()
st.markdown(f'''
   <style>
   .stApp {{
             background-image: url("https://wallpapercave.com/wp/wp3644301.jpg");
             background-attachment: fixed;
             background-size: cover;
             }}

   /* Add CSS for the navigation bar */
   .sidebar-content {{
        background-image: url("https://th.bing.com/th/id/OIG1.OzHhRpdwr_bLGbl1XA7G?pid=ImgGn");
        background-size: cover;
   }}

   .navigation-bar-title {{
        font-size: 24px;
        font-weight: bold;
        color: #007bff; /* Title color */
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 10px;
   }}
   </style>
   ''', unsafe_allow_html=True)

# Define a function to create a navigation bar
def navigation_bar():
    st.sidebar.markdown('<div class="navigation-bar"><div class="navigation-bar-title">STORMSIGHT</div></div>', unsafe_allow_html=True)
    app_selection = st.sidebar.radio('Go to', ('Home', 'Intensity Estimation', 'Preventive Measures'), key='navigation')
    return app_selection

# Get the selected app from the navigation bar
selected_app = navigation_bar()

# Add the selected app to MultiApp
if selected_app == 'Home':
    app.add_app(home.app)
elif selected_app == 'Preventive Measures':
    app.add_app(preventive_measures.app)
elif selected_app == 'Intensity Estimation':
    app.add_app(cyclone_app.app)

# Run the selected app
app.run()
