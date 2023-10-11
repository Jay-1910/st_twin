import streamlit as st
import webbrowser
import pandas as pd
import numpy as np

st.title("Digital Twin Platform")

data = {'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'Value': np.random.randint(1, 100, size=10)}
df = pd.DataFrame(data)


st.write(f'<iframe src="http://localhost:8080/" width="600" height="600"></iframe>', unsafe_allow_html=True)

st.line_chart(df.set_index('Date')['Value'],use_container_width=True, width=600)
