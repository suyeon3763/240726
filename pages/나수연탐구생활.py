import streamlit as st

# Function to reset the quiz
def reset_quiz():
    st.session_state.step = 1
    st.session_state.name_correct = False
    st.session_state.food_correct = False
    st.session_state.subject_correct = False

# Initialize session state variables
if 'step' not in st.session_state:
    reset_quiz()

# Questions and answers
questions = {
    1: {
        'question': "제작자의 이름은 무엇인가요?",
        'answer': "나수연"
    },
    2: {
        'question': "제작자가 가르치는 과목은 무엇인가요?",
        'answer': "윤리"
    },
    3: {
        'question': "제작자가 가장 좋아하는 음식은 무엇인가요?",
        'answer': "초밥"
    }
}

st.title('나는 어떤 사람일까요?')

# Reset button
if st.button('퀴즈 리셋'):
    reset_quiz()

# Display the current question based on the step
if st.session_state.step == 1:
    st.write(questions[1]['question'])
    answer = st.text_input("정답을 입력하세요:", key='name')
    if st.button("맞지?", key='submit1'):
        if answer.strip().lower() == questions[1]['answer'].lower():
            st.session_state.name_correct = True
            st.session_state.step = 2
        else:
            st.warning("정답이 아닙니다. 다시 시도하세요.")
            reset_quiz()

elif st.session_state.step == 2:
    st.write(questions[2]['question'])
    answer = st.text_input("정답을 입력하세요:", key='food')
    if st.button("맞지?", key='submit2'):
        if answer.strip().lower() == questions[2]['answer'].lower():
            st.session_state.food_correct = True
            st.session_state.step = 3
        else:
            st.warning("정답이 아닙니다. 다시 시도하세요.")
            reset_quiz()

elif st.session_state.step == 3:
    st.write(questions[3]['question'])
    answer = st.text_input("정답을 입력하세요:", key='subject')
    if st.button("맞지?", key='submit3'):
        if answer.strip().lower() == questions[3]['answer'].lower():
            st.session_state.subject_correct = True
            st.success("축하합니다! 모든 문제를 맞혔습니다.")
            st.balloons()
            reset_quiz()
        else:
            st.warning("정답이 아닙니다. 다시 시도하세요.")
            reset_quiz()
