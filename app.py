# Load Test Case Dataset with Cleaned Column Names
@st.cache_data
def load_test_case_dataset():
    test_case_file = 'selected_demand_1.xlsx'
    test_case_data = pd.read_excel(test_case_file)
    
    # Clean column names by stripping whitespace and special characters
    test_case_data.columns = test_case_data.columns.str.strip().str.replace('\t', '', regex=False)
    return test_case_data

# Fetch Project Attributes
st.markdown("### 📋 Select Test Case Project ID")
project_ids = test_case_data["Demand ID"].unique()
selected_project_id = st.selectbox("**Project ID:**", project_ids)

# Retrieve the selected project
selected_project = test_case_data[test_case_data["Demand ID"] == selected_project_id]

# Handle empty selected project
if selected_project.empty:
    st.error(f"No project found with Demand ID {selected_project_id}. Please check your dataset.")
else:
    selected_project = selected_project.iloc[0]  # Get the first matching row

    # Auto-Populated Attributes (Read-only on UI)
    st.markdown("### 🛠️ Auto-Populated Project Attributes")
    col1, col2 = st.columns(2)
    user_input = []
    columns = data.columns.drop("Employment ID")

    # Display auto-populated fields as read-only
    for idx, column in enumerate(columns):
        with col1 if idx % 2 == 0 else col2:
            if column in selected_project:
                value = selected_project[column]
                st.text_input(f"**{column}**", value, disabled=True)  # Read-only field
                if column in label_encoders:
                    user_input.append(label_encoders[column].transform([value])[0])
                else:
                    user_input.append(value)
