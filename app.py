import streamlit as st

import utils
import os
import sys
import time


st.set_page_config(
    page_title="QA App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Question Answering Using BERT")

# context = '''The Kargil War, also known as the Kargil conflict, was an armed conflict fought between India and Pakistan from May to July 1999 in the Kargil district of Jammu and Kashmir and elsewhere along the Line of Control (LoC). In India, the conflict is also referred to as Operation Vijay, which was the name of the Indian military operation to clear out the Kargil sector. The Indian Air Force's role in acting jointly with Indian Army ground troops during the war was aimed at flushing out regular and irregular troops of the Pakistan Army from vacated Indian positions along the LoC.This particular operation was given the codename Operation Safed Sagar'''

# question = 'what is Operation Vijay'

context = st.text_area("Enter the Context")
question = st.text_area("Enter the Question")
# st.button("Predict")
if st.button("Predict") and context and question:
    start = time.time()
    answer = utils.QA_prediction(question, context)
    end = time.time()
    st.header("Answer :\n "+ answer['answer'])
else:
    st.write("Enter the Context and Question")
footer='''

<style> your css code put here</style>

<div class='footer'>

<p>Made with ❤️ by Medhaja<a style='display:block;text-align:center;' 

https://medhaja.com</a></p>

</div>'''

st.markdown(footer, unsafe_allow_html=True)