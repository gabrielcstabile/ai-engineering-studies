import streamlit as st

def hello_world() -> str:
    return "Hello World."

def main() -> None:
    st.write(hello_world())
    
if __name__ == "__main__":
    main()

