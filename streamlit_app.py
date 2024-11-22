import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer


st.set_page_config(
    page_title="Streamlit : マナビDXQuest2024 PBL05 提出ファイル チェック アプリ",
    layout="wide"
)

st.markdown(f"# マナビDXQuest2024 PBL05 提出ファイル チェック アプリ")

STR_UPLOAD_CSV = "CSVファイルをアップロード"

df = None
input = st.file_uploader("Choose a CSV file")
if input is not None:
    title_str = input.name
    df = pd.read_csv(input)
    st.dataframe(df)
