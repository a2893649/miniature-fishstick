# 导入 streamlit 库，简写为 st 是行业通用习惯
import streamlit as st

# 设置网页标题
st.title("我的第一个 Streamlit 应用")

# 添加文本
st.write("你好，Streamlit！")

# 添加交互式组件（比如滑块）
age = st.slider("请选择你的年龄", 0, 100, 25)
st.write(f"你的年龄是：{age} 岁")