# Create a Number Guessing Game (user guesses random number).
"""
Created on Mon Apr 27 16:01:00 2026

@author: Varad
"""

import streamlit as st
import random

def reset_game():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.feedback = "I'm thinking of a number between 1 and 100..."

def main():
    st.set_page_config(page_title="Number Guessing Game", page_icon="🎲")
    
    st.title("🎲 Number Guessing Game")
    st.write("Can you guess the number I'm thinking of?")

    # Initialize game state
    if 'target_number' not in st.session_state:
        reset_game()

    # Display game status
    st.info(st.session_state.feedback)
    
    # User Input
    with st.form(key="guess_form", clear_on_submit=True):
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
        submit = st.form_submit_button("Submit Guess")

    if submit and not st.session_state.game_over:
        st.session_state.attempts += 1
        
        if guess < st.session_state.target_number:
            st.session_state.feedback = f"📈 Too low! Try again. (Attempt: {st.session_state.attempts})"
            st.rerun()
        elif guess > st.session_state.target_number:
            st.session_state.feedback = f"📉 Too high! Try again. (Attempt: {st.session_state.attempts})"
            st.rerun()
        else:
            st.session_state.feedback = f"🎯 Correct! The number was {st.session_state.target_number}."
            st.session_state.game_over = True
            st.rerun()

    # Victory screen
    if st.session_state.game_over:
        st.success(st.session_state.feedback)
        st.balloons()
        st.metric("Total Attempts", st.session_state.attempts)
        
        if st.button("Play Again"):
            reset_game()
            st.rerun()

    # Sidebar stats
    with st.sidebar:
        st.header("Game Stats")
        st.write(f"Current Session Attempts: {st.session_state.attempts}")
        if st.button("Reset Game"):
            reset_game()
            st.rerun()

if __name__ == "__main__":
    main()
