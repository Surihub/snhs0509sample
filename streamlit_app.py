import streamlit as st

st.title("🎈 숩숩이의 첫 번째 앱!")
st.info(
    "안녕하세요! 반갑습니다. 저는 ~~입니다."
)
st.write(
    "안녕하세요! 반갑습니다. 저는 ~~입니다."
)

# LaTeX 수식 출력
st.latex(r"E = mc^2")
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")

st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHcwYWpkY3YzYjFiNjdodzZwa2tweG9zN3hzYm8xYmVydnkzZDB6cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uQgXjl505BdYAv8H0X/giphy.gif")

st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성

# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용

    # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")

# st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)


name = st.text_input("이름을 입력해주세요:)")

if name == "고구마":
    st.success(name+"님 반갑습니다!")
else:
    st.error("고구마님이 아니네요...")

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.info("선택한 성별:"+gender)
