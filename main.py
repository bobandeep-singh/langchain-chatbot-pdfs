import streamlit as st

# set page configuration


def main(name):
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("CHat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs and click on process")
        st.button("Process")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')
