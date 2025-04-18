
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ذاكرة التدقيق الذكية", layout="centered")

st.title("🧠 ذاكرة التدقيق الذكية")
st.markdown("أدخل ملاحظة تدقيق للحصول على ملاحظات مشابهة وتوصيات مرجعية.")

# تحميل البيانات
df = pd.read_csv("audit_observations_sample.csv")

# إدخال المستخدم
query = st.text_area("✏️ أدخل ملاحظة التدقيق هنا:")

if st.button("🔍 تحليل واقتراح"):
    if query.strip() == "":
        st.warning("يرجى إدخال الملاحظة.")
    else:
        # البحث البسيط بالتطابق الجزئي
        results = df[df['observation'].str.contains(query, case=False, na=False)]

        if results.empty:
            st.info("لم يتم العثور على ملاحظات مشابهة.")
        else:
            st.success(f"تم العثور على {len(results)} ملاحظة مشابهة:")
            st.dataframe(results)
