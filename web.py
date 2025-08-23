import streamlit as st
import pandas as pd
import joblib

# 尝试加载模型
try:
    model = joblib.load('A:/研究生/临床课题/专利/LDA.pkl')
except Exception as e:
    st.error(f"加载模型时出错: {e}")
    st.stop()

# 应用标题
st.title("PONV Prediction")
st.write("Please enter the patient's anesthesia information data：")

# 性别字段使用selectbox
gender = st.selectbox("gender", options=[0, 1], format_func=lambda x: "male" if x == 0 else "female")

# 其他输入字段
age = st.number_input("age", min_value=0, max_value=120, step=1)
weight = st.number_input("weight (kg)", min_value=0, step=1)
height = st.number_input("height (cm)", min_value=0, step=1)
ponv = st.radio("previous history of PONV", options=[0, 1], format_func=lambda x: "no" if x == 0 else "yes")
smoke = st.radio("smoking history", options=[0, 1], format_func=lambda x: "no" if x == 0 else "yes")
motion = st.radio("motion", options=[0, 1], format_func=lambda x: "no" if x == 0 else "yes")
opioids = st.radio("history of opioid use", options=[0, 1], format_func=lambda x: "no" if x == 0 else "yes")
duration = st.number_input("anesthesia duration (min)", min_value=0, step=1)
exam = st.number_input("exam", min_value=0, max_value=10, step=1)  # 假设检查类型为离散型数值
sbpa = st.number_input("maximum systolic blood pressure", min_value=0, step=1)
dbpa = st.number_input("maximum diastolic blood pressure", min_value=0, step=1)
sbpb = st.number_input("minimum diastolic blood pressure", min_value=0, step=1)
dbpb = st.number_input("minimum systolic blood pressure", min_value=0, step=1)

# 数据预处理
data = pd.DataFrame([[age, gender, height, weight, ponv, smoke, motion, opioids, duration, exam, sbpa, dbpa, sbpb, dbpb]], 
                    columns=['age', 'gender', 'height', 'weight', 'ponv', 'smoke', 'motion', 'opioids', 'duration', 'exam', 'sbpa', 'dbpa', 'sbpb', 'dbpb'])

# 预测
if st.button("Prediction"):
    try:
        prediction = model.predict(data)
        if prediction[0] == 1:
            st.write("Postoperative nausea and vomiting [Yes (√) / No ( )]")
        else:
            st.write("Postoperative nausea and vomiting [Yes ( ) / No (√)]")
    except Exception as e:
        st.write("预测过程中出现错误: ", e)
