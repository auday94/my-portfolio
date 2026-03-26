import streamlit as st
import json

# 1. إعدادات الصفحة
st.set_page_config(page_title="معرض أعمالي الاحترافي", page_icon="🎨", layout="wide")

# 2. كود تنسيق اللغة العربية (RTL) والألوان
st.markdown("""
<style>
    * {
        direction: rtl;
        text-align: right;
    }
    .stMainContainer {
        background-color: #0e1117;
    }
</style>
""", unsafe_allow_html=True)

# 3. قراءة البيانات من ملف JSON
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        projects = json.load(f)
except FileNotFoundError:
    projects = [] # في حال لم يجد الملف لا يتوقف الموقع

# 4. العنوان الرئيسي
st.title("أهلاً بكم في معرض أعمالي 🚀")
st.subheader("مصمم جرافيك ومسوق رقمي | خبرة 5 سنوات")
st.write("هنا أعرض لكم خلاصة تجاربي في التصميم والمونتاج وإدارة الحملات الإعلانية.")
st.divider()

# 5. عرض المشاريع تلقائياً من الملف
if not projects:
    st.warning("جاري تجهيز المشاريع... تأكد من وجود ملف data.json")
else:
    for project in projects:
        with st.container():
            # تقسيم العرض لعمودين (واحد للصورة وواحد للنص)
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # عرض الصورة المذكورة في ملف الـ JSON
                st.image(project['image'], use_container_width=True)
            
            with col2:
                st.header(project['title'])
                st.write(project['description'])
                st.info(f"التصنيف: {project['type']}")
                
            st.divider()

# 6. تذييل الصفحة (Footer)
st.success("✉️ للتواصل والتعاون العملي، يمكنكم مراسلتي مباشرة.")
