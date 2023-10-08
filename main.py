import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Pythones", page_icon="🐍", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/x.jpg")
img_lottie_animation = Image.open("images/y.png")

with st.container():
    st.subheader("Hi, Saya Seno :wave:")
    st.title("Data Operation - PT BRI Insurance")
    st.write(
        "Saya telah bekerja sebagai Software Engineer, Data Scientist, dan Data Operation."
    )
    st.write("[Selengkapnya>](https://www.linkedin.com/in/seno-alrianto-aa2615166)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Apa yang saya kerjakan?")
        st.write("##")
        st.write(
            """
            Saat ini saya telah melakukan beberpa pekerjaan terkait :
            - Manajemen integrasi data agar lebih optimal menggunakan SSIS.
            - Mengembangkan sistem monitoring database server dan informasi data menggunakan SSRS, Grafana, dan Python.
            - Mengembangkan sistem informasi via chatbot telegram menggunakan Python.
            - Mengelola yang ada dalam server tim (Windows Server, MS SQL, Tableau Server, Python).
            - Memprediksi kebutuhan server berdasarkan rencana kerja.

            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@pythones_ind)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Daftar Projek")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Automation - Monitoring RAM")
        st.write(
            """
            Memantau kondisi RAM server secara realtime yang bersifat otomatis.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/1MwUbfz25v4?si=AZdBsJEe5dpU9Ejx)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Automation - Monitoring Storage")
        st.write(
            """
            Memantau kondisi Storage server secara realtime yang bersifat otomatis.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/6oq-u5F_xo8?si=KZtTuj_ijexn2XVH)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Hubungi saya")
        st.write("##")
        st.write(
            """
            Jika kamu tertarik dengan apa yang saya bisa, bisa hubungi melalui :\n
            Email : salrianto@work.brins.co.id\n
            Whatsapp : 0813-8106-7348
            """
        )