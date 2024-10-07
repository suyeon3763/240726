import streamlit as st

# Existential Quiz 함수 정의
def existential_quiz():
    questions = [
        "1. 인생에서 불안과 두려움을 피할 수 없다고 생각하십니까?",
        "2. 인간의 자유가 가장 중요한 속성이라고 믿으십니까?",
        "3. '신에 대한 믿음'이 존재의 문제를 해결한다고 생각하십니까?",
        "4. '죽음'이 삶에서 가장 중요한 문제라고 생각하십니까?",
        "5. 인간은 자신의 본질보다 먼저 선택하고 행동해야 한다고 생각하십니까?",
        "6. 인간은 진리를 절대적으로 알 수 없다고 생각하십니까?",
        "7. 개인적인 신앙이 진리를 추구하는 데 중요하다고 생각하십니까?",
        "8. 인간의 본질은 스스로 만들어가는 것이라고 생각하십니까?",
        "9. 개인적 선택이 사회적 책임보다 더 중요하다고 생각하십니까?",
        "10. 삶의 본질이 신과 연결되어 있다고 생각하십니까?"
    ]
    
    scoring = {"매우 그렇다": 3, "그렇다": 2, "보통이다": 1, "그렇지 않다": 0, "전혀 그렇지 않다": 0}
    responses = {
        "1": {"매우 그렇다": "키르케고르", "그렇다": "하이데거", "보통이다": "사르트르"},
        "2": {"매우 그렇다": "사르트르", "그렇다": "야스퍼스", "보통이다": "하이데거"},
        "3": {"매우 그렇다": "키르케고르", "그렇다": "야스퍼스", "보통이다": "하이데거"},
        "4": {"매우 그렇다": "하이데거", "그렇다": "키르케고르", "보통이다": "야스퍼스"},
        "5": {"매우 그렇다": "사르트르", "그렇다": "하이데거", "보통이다": "야스퍼스"},
        "6": {"매우 그렇다": "야스퍼스", "그렇다": "하이데거", "보통이다": "사르트르"},
        "7": {"매우 그렇다": "키르케고르", "그렇다": "야스퍼스", "보통이다": "하이데거"},
        "8": {"매우 그렇다": "사르트르", "그렇다": "하이데거", "보통이다": "야스퍼스"},
        "9": {"매우 그렇다": "사르트르", "그렇다": "야스퍼스", "보통이다": "하이데거"},
        "10": {"매우 그렇다": "키르케고르", "그렇다": "야스퍼스", "보통이다": "하이데거"}
    }

    # Session State에 점수 저장
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.philosophers_score = {"키르케고르": 0, "하이데거": 0, "야스퍼스": 0, "사르트르": 0}

    current_question = st.session_state.current_question

    # 질문이 남아있을 때
    if current_question < len(questions):
        question = questions[current_question]
        answer = st.radio(question, ["매우 그렇다", "그렇다", "보통이다", "그렇지 않다", "전혀 그렇지 않다"])

        if st.button("다음"):
            st.session_state.answers.append(answer)

            # 점수 계산
            philosopher = responses[str(current_question + 1)][answer]
            st.session_state.philosophers_score[philosopher] += scoring[answer]

            # 다음 질문으로 이동
            st.session_state.current_question += 1
            st.experimental_rerun()

    # 모든 질문이 끝났을 때
    else:
        st.write("모든 질문에 답변하셨습니다. 결과를 확인하세요.")

        # 결과 도출
        highest_score = max(st.session_state.philosophers_score, key=st.session_state.philosophers_score.get)
        st.write(f"당신과 가장 가까운 실존주의 철학자는: **{highest_score}** 입니다.")
        st.write("점수:", st.session_state.philosophers_score)

        # 다시 시작할 수 있도록 초기화 버튼 제공
        if st.button("다시 시작하기"):
            st.session_state.current_question = 0
            st.session_state.answers = []
            st.session_state.philosophers_score = {"키르케고르": 0, "하이데거": 0, "야스퍼스": 0, "사르트르": 0}
            st.experimental_rerun()

# Streamlit 앱 실행
st.title("실존주의 철학자 테스트")
st.write("10개의 질문에 답하고 당신과 가장 가까운 실존주의 철학자를 찾아보세요!")

existential_quiz()

