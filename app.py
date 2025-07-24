from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Function to load Gemini Model
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(f"{prompt}\n{question}")
    return response.text
    
#Funtion to retrieve query from db
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit() 
    conn.close()
    for row in rows:
        print(row)
    return rows 

prompt=["""You are an expert in converting English instructions into SQL queries. The SQL database table is named STUDENT and has the following columns: NAME, CLASS, SECTION, and MARKS.\n

Always provide the correct SQL query based on the instruction.\n

Do not add triple quotes (''') at the beginning or end of the SQL code.\n
    
Only return the SQL query, nothing else—no explanation, no formatting, no extra text.\n

For example, if the instruction is: "How many entries are present in the column?",
the output should be:
SELECT COUNT(*) FROM STUDENT;"""]  

st.set_page_config(page_title="I can Retrieve any SQL Query")
st.header("Gemini App to Retrieve SQL Data")
question=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)