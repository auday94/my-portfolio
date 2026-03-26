import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="معرض أعمالي", page_icon="🎨", layout="centered")
# كود سحري لضبط اتجاه الموقع للغة العربية
st.markdown("""
<style>
    * {
        direction: rtl;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# 2. العنوان الرئيسي والنبذة
st.title("أهلاً بكم في معرض أعمالي 🎨")
st.subheader("مصمم جرافيك محترف | خبرة 5 سنوات")

st.write("""
أنا متخصص في إخراج تصاميم بصرية جذابة واحترافية. 
أدمج بين الفن والتقنية لإنشاء هويات بصرية، وتصاميم سوشيال ميديا مدروسة تسويقياً، 
باستخدام أدوات مثل Photoshop، Illustrator، InDesign، بالإضافة لمونتاج الفيديو الاحترافي على Premiere Pro.
""")

st.divider() # خط فاصل أنيق

# 3. قسم معرض الأعمال (مقسم لعمودين)
st.header("أحدث المشاريع")
col1, col2 = st.columns(2)

with col1:
    st.info("📱 تصاميم السوشيال ميديا")
    st.write("حملات إعلانية متكاملة مصممة خصيصاً لجذب الانتباه وزيادة التفاعل.")
    # هذا هو السطر الجديد لعرض الصورة:
    st.image("design1.jpg", caption="تصميم سوشيال ميديا", use_container_width=True)

with col2:
    st.info("🎬 مونتاج وتحرير الفيديو")
    st.write("مقاطع ريلز وفيديوهات ترويجية قصيرة وجذابة.")
    # st.video("promo_video.mp4") # رح نفعل هاد السطر لاحقاً لعرض فيديوهاتك

st.divider()

# 4. قسم التواصل
st.success("✉️ هل لديك مشروع رائع في ذهنك؟ دعنا نتحدث!")
st.write("**البريد الإلكتروني:** contact@example.com")
