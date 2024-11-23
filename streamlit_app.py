import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
from pandas.api.types import is_numeric_dtype

def check_csv_file(input):
    # ファイルを読み込み
    input_data= input.getvalue()
    # BOMチェック
    if input_data.startswith(b'\xef\xbb\xbf'):
        st.error("❌ ファイルがBOM付きのUTF-8で保存されています。CSVファイルを保存するエンコードをチェックしてください。")
        return
    else:
        st.write("⭕️ BOMがないことのチェックOK")    

    df = pd.read_csv(input, header=None)

    shape = df.shape
    st.write(f"行 : {shape[0]}, 列: {shape[1]}")
    if shape != (5983, 3):
        st.error("❌ ファイルの行数/列数がおかしい (期待値 -> 行 : 5983, 列: 3)")
    else:
        st.write("⭕️ ファイルの行数/列数のチェックOK")    

    # 一列目が数値型かをチェック
    is_1st_column_numeric = is_numeric_dtype(df.iloc[:, 0])
    if is_1st_column_numeric:
        st.write("⭕️ 一列目が数値型かをチェックOK")
    else:
        st.error("❌ 一列目が数値型ではない")

    # 二列目が数値型かをチェック
    is_2nd_column_numeric = is_numeric_dtype(df.iloc[:, 1])
    if is_2nd_column_numeric:
        st.write("⭕️ 二列目が数値型かをチェックOK")
    else:
        st.error("❌ 二列目が数値型ではない")

    # 三列目が数値型かをチェック
    is_3rd_column_numeric = is_numeric_dtype(df.iloc[:, 2])
    if is_3rd_column_numeric:
        st.write("⭕️ 三列目が数値型かをチェックOK")
    else:
        st.error("❌ 三列目が数値型ではない")

    # 一列目が行番号と等しいかどうかチェック
    is_index_1st_column_equal = (df.iloc[:, 0] == df.index).all()
    if is_index_1st_column_equal:
        st.write("⭕️ 一列目が行番号と等しいかどうかチェックOK")
    else:
        st.error("❌ 一列目が行番号と等しくない")

    # 二列目に無効な値（NaNや空白）があるかチェック
    has_2nd_column_invalid_values = df.iloc[:, 1].isna().any()
    if has_2nd_column_invalid_values:
        st.error("❌ 二列目に無効な値（NaNや空白）がある")
    else:
        st.write("⭕️ 二列目に無効な値（NaNや空白）があるかチェックOK")

    # 三列目に無効な値（NaNや空白）があるかチェック
    has_3rd_column_invalid_values = df.iloc[:, 2].isna().any()
    if has_3rd_column_invalid_values:
        st.error("❌三列目に無効な値（NaNや空白）がある")
    else:
        st.write("⭕️三列目に無効な値（NaNや空白）があるかチェックOK")

    st.dataframe(df)


st.set_page_config(
    page_title="Streamlit : MDXQ2024 PBL05 提出ファイル フォーマット 確認アプリ",
)

st.markdown(f"# MDXQ2024 PBL05 提出ファイル フォーマット確認 アプリ")

STR_UPLOAD_CSV = "CSVファイルをアップロード"

input = st.file_uploader("Choose a CSV file")
if input is not None:
    check_csv_file(input)

