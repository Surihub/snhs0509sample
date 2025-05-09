import streamlit as st
import openai

st.set_page_config(page_title="숩숩이의 첫 번째 앱", layout="wide", page_icon="😥")

st.title("🎈 숩숩이의 첫 번째 앱!")

# -------------------------------
# 🗂️ 탭 구성
# -------------------------------
tabs = st.tabs([
    "소개", 
    "메시지 & 수식", 
    "이미지 & 코드", 
    "레이아웃", 
    "사이드바 & 입력폼", 
    "GPT 호출", 
    "음악추천"
])

# -------------------------------
# 📌 소개 탭
# -------------------------------
with tabs[0]:
    st.header("👋 소개")
    st.info("안녕하세요! 반갑습니다. 저는 ~~입니다.")
    st.write("안녕하세요! 반갑습니다. 저는 ~~입니다.")

# -------------------------------
# 📌 메시지 & 수식 탭
# -------------------------------
with tabs[1]:
    st.header("📢 메시지 & 수식")
    st.latex(r"E = mc^2")

    st.info("ℹ️ 정보 메시지입니다.")
    st.warning("⚠️ 경고 메시지입니다.")
    st.success("✅ 성공 메시지입니다.")
    st.error("❌ 오류 메시지입니다.")

# -------------------------------
# 📌 이미지 & 코드 탭
# -------------------------------
with tabs[2]:
    st.header("🖼️ 이미지 & 💻 코드")
    st.image(
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHcwYWpkY3YzYjFiNjdodzZwa2tweG9zN3hzYm8xYmVydnkzZDB6cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uQgXjl505BdYAv8H0X/giphy.gif"
    )

    st.code(
        """
import streamlit as st
st.title('Hello World')
""",
        language="python"
    )

    st.link_button("Streamlit Cheat Sheet", "https://docs.streamlit.io/develop/quick-reference/cheat-sheet")

# -------------------------------
# 📌 레이아웃 탭 (열, 탭, 확장)
# -------------------------------
with tabs[3]:
    st.header("📐 레이아웃 구성")

    # 열
    col1, col2 = st.columns(2)
    with col1:
        st.write("왼쪽 열입니다.")
    with col2:
        st.write("오른쪽 열입니다.")

    # 탭
    inner_tab1, inner_tab2 = st.tabs(["탭 1", "탭 2"])
    with inner_tab1:
        st.write("탭 1에 해당하는 내용입니다.")
    with inner_tab2:
        st.write("탭 2에 해당하는 내용입니다.")

    # 확장
    with st.expander("ℹ️ 자세한 설명 보기"):
        st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")

# -------------------------------
# 📌 사이드바 & 입력폼 탭
# -------------------------------
with tabs[4]:
    st.header("📝 입력폼 & 사이드바")

    st.sidebar.title("📌 사이드바 메뉴")
    option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
    st.write("선택한 옵션:", option)

    name = st.text_input("이름을 입력해주세요:)")
    if name == "고구마":
        st.success(f"{name}님 반갑습니다!")
    elif name:
        st.error("고구마님이 아니네요...")

    gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
    st.info(f"선택한 성별: {gender}")

# -------------------------------
# 📌 GPT 호출 탭
# -------------------------------
with tabs[5]:
    st.header("🤖 GPT 호출")
    user_api_key = st.secrets["openai"]["api_key"]

    if user_api_key:
        from openai import OpenAI

        client = OpenAI(api_key=user_api_key)
        prompt = st.text_input("프롬프트를 입력해주세요.")

        if prompt:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)

with tabs[6]:
    import streamlit as st
    import webbrowser
    from openai import OpenAI



    st.title("🎵 GPT 기반 음악 추천기")

    # 추천 기준 선택
    criterion = st.radio(
        "🎯 추천 기준을 선택하세요",
        ["MBTI 기반", "기분에 따라", "장르 기반", "요즘 인기곡"]
    )

    # MBTI 입력
    mbti_type, mbti_desc = "", ""
    if criterion == "MBTI 기반":
        mbti_type = st.selectbox("🧬 MBTI를 선택하세요", [
            "INTJ", "INTP", "ENTJ", "ENTP",
            "INFJ", "INFP", "ENFJ", "ENFP",
            "ISTJ", "ISFJ", "ESTJ", "ESFJ",
            "ISTP", "ISFP", "ESTP", "ESFP"
        ])
        mbti_desc = st.text_area("📄 성격을 한 줄로 설명해 주세요", placeholder="예: 조용하지만 상상력이 풍부하고 감성이 섬세해요.")

    # 프롬프트 생성
    def make_prompt(criterion, mbti_type="", mbti_desc=""):
        if criterion == "MBTI 기반":
            return f"""
    MBTI가 {mbti_type}이고, 성격은 "{mbti_desc}"인 사람에게 어울리는 음악을 아래 형식으로 한 곡 추천해줘.

    제목: (노래 제목)
    아티스트: (가수 이름)
    추천 이유: (짧고 강렬하게)
    분위기 요약: (감성적이고 창의적인 표현으로)
    """
        elif criterion == "기분에 따라":
            return """
    감정을 위로하거나 고양시키는 음악을 아래 형식으로 한 곡 추천해줘.

    제목: (노래 제목)
    아티스트: (가수 이름)
    추천 이유: (짧고 강렬하게)
    분위기 요약: (감성적이고 창의적인 표현으로)
    """
        elif criterion == "장르 기반":
            return """
    다양한 장르 중 추천할 만한 음악을 아래 형식으로 한 곡 소개해줘.

    제목: (노래 제목)
    아티스트: (가수 이름)
    추천 이유: (짧고 강렬하게)
    분위기 요약: (감성적이고 창의적인 표현으로)
    """
        elif criterion == "요즘 인기곡":
            return """
    요즘 유행하거나 인기 있는 음악을 아래 형식으로 한 곡 추천해줘.

    제목: (노래 제목)
    아티스트: (가수 이름)
    추천 이유: (짧고 강렬하게)
    분위기 요약: (감성적이고 창의적인 표현으로)
    """

    # 추천 요청
    if st.button("🎁 음악 추천받기"):

        with st.spinner("GPT가 노래를 고르고 있어요..."):
            prompt = make_prompt(criterion, mbti_type, mbti_desc)

            try:
                client = OpenAI(api_key=st.secrets["openai"]["api_key"])
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}]
                )
                response = completion.choices[0].message.content.strip()

                # 내용 파싱
                lines = response.splitlines()
                title, artist, reason, mood = "", "", "", ""
                for line in lines:
                    if line.startswith("제목:"):
                        title = line.replace("제목:", "").strip()
                    elif line.startswith("아티스트:"):
                        artist = line.replace("아티스트:", "").strip()
                    elif line.startswith("추천 이유:"):
                        reason = line.replace("추천 이유:", "").strip()
                    elif line.startswith("분위기 요약:"):
                        mood = line.replace("분위기 요약:", "").strip()

                # 링크 생성
                search_query = f"{title} {artist} 노래"
                search_url = f"https://www.google.com/search?q={search_query}"

                # 출력
                st.markdown(f"# 🎵 {title} - {artist}")
                st.markdown(f"### ✅ 추천 이유\n{reason}")
                st.markdown(f"### 🎧 분위기 요약\n{mood}")
                st.markdown(
                    f'<a href="{search_url}" target="_blank"><button style="background-color:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">🔗 노래 검색하러 가기</button></a>',
                    unsafe_allow_html=True
                )

                if st.button("🔁 다시 추천받기"):
                    st.rerun()

            except Exception as e:
                st.error(f"GPT 호출 오류: {e}")


# import streamlit as st

# st.title("🎈 숩숩이의 첫 번째 앱!")
# st.info(
#     "안녕하세요! 반갑습니다. 저는 ~~입니다."
# )
# st.write(
#     "안녕하세요! 반갑습니다. 저는 ~~입니다."
# )

# # LaTeX 수식 출력
# st.latex(r"E = mc^2")
# st.info("ℹ️ 정보 메시지입니다.")
# st.warning("⚠️ 경고 메시지입니다.")
# st.success("✅ 성공 메시지입니다.")
# st.error("❌ 오류 메시지입니다.")

# st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHcwYWpkY3YzYjFiNjdodzZwa2tweG9zN3hzYm8xYmVydnkzZDB6cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/uQgXjl505BdYAv8H0X/giphy.gif")

# st.code("""
# import streamlit as st
# st.title('Hello World')
# """, language="python")

# st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

# # st.columns(n): 화면을 n개의 수직 열로 나눕니다
# col1, col2 = st.columns(2)  # 2개의 열 생성

# with col1:
#     st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
# with col2:
#     st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성

# # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
# tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

# with tab1:
#     st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
# with tab2:
#     st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용

#     # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
# with st.expander("ℹ️ 자세한 설명 보기"):
#     st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")

# # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
# st.sidebar.title("📌 사이드바 메뉴")
# option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
# st.write("선택한 옵션:", option)


# name = st.text_input("이름을 입력해주세요:)")

# if name == "고구마":
#     st.success(name+"님 반갑습니다!")
# else:
#     st.error("고구마님이 아니네요...")

# # 여러 옵션 중 하나 선택
# gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
# st.info("선택한 성별:"+gender)


# import openai

# user_api_key = st.text_input("키를 입력해주세요.")

# if user_api_key:
#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)

