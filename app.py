import streamlit as st
from multiapp import MultiApp
from apps import csp, ga, analysis # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Question 1", ga.app)
app.add_app("Question 2", csp.app)
app.add_app("Question 3", analysis.app)
# The main app
app.run()