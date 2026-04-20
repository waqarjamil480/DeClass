import streamlit as st
import requests
import json

# Define the Streamlit app title
st.title("My Task API : MongoDB Backend and StreamLit Frontend")

# Define the test case names
test_case_names = ["Create Task", "List All Tasks", "Get Task", "Update Task", "Delete Task"]

# Create tabs for each test case
tabs = st.tabs(test_case_names)

# Define a function to run the test cases based on user input
def run_test_case(test_case_name):
    if test_case_name == "Create Task":
        st.subheader("Create Task Test Case")
        title = st.text_input("Task Title", "My First Task",key=test_case_name+'_textinput')
        if st.button(key=test_case_name+'_button',label="Run Test Case"):
            response = requests.post('http://localhost:5001/v1/tasks', json={"title": title})
            st.json(response.json())

    elif test_case_name == "List All Tasks":
        st.subheader("List All Tasks Test Case")
        if st.button(key=test_case_name+'_button',label="Run Test Case"):
            response = requests.get('http://localhost:5001/v1/tasks')
            st.json(response.json())

    elif test_case_name == "Get Task":
        st.subheader("Get Task Test Case")
        task_id = st.text_input("Task ID", "1",key=test_case_name+'_textinput')
        if st.button(key=test_case_name+'_button',label="Run Test Case"):
            response = requests.get(f'http://localhost:5001/v1/tasks/{task_id}')
            st.json(response.json())

    elif test_case_name == "Update Task":
        st.subheader("Update Task Test Case")
        task_id = st.text_input("Task ID", "1",key=test_case_name+'_textinput_taskid')
        title = st.text_input("New Task Title", "My Updated Task",key=test_case_name+'_textinput_title')
        is_completed = st.checkbox("Is Completed", value=False)
        if st.button(key=test_case_name+'_button',label="Run Test Case"):
            response = requests.put(f'http://localhost:5001/v1/tasks/{task_id}', json={"title": title, "is_completed": is_completed})
            st.write(f"Status Code: {response.status_code}")
            if response.status_code == 204:
                st.success("Task updated successfully!")
            else:
                try:
                    st.json(response.json())
                except:
                    st.error(f"Error: {response.text}")

    elif test_case_name == "Delete Task":
        st.subheader("Delete Task Test Case")
        task_id = st.text_input("Task ID", "1",key=test_case_name+'_textinput')
        if st.button(key=test_case_name+'_button',label="Run Test Case"):
            response = requests.delete(f'http://localhost:5001/v1/tasks/{task_id}')
            st.write(f"Status Code: {response.status_code}")
            if response.status_code == 204:
                st.success("Task deleted successfully!")
            else:
                try:
                    st.json(response.json())
                except:
                    st.error(f"Error: {response.text}")

# Loop through tabs and assign a test case to each tab
for i, tab in enumerate(tabs):
    with tab:
        run_test_case(test_case_names[i])