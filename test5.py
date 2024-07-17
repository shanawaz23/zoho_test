import streamlit as st
import sqlite3

def my_connection(db_file):
    conn=None
    
    try:
        conn=sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return conn
    
def create_table(conn):
    sql_table="""
                  CREATE TABLE IF NOT EXIST emails(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT NOT NULL UNIQUE);
                  """
    try:
        c=conn.cursor()
        c.execute(sql_table)

    except sqlite3.Error as e:
        print(e)

def insert_email(conn,email):
    sql = "INSERT INTO emails (emails) VALUSE (?)"
    cur=conn.cursor()
    cur.execute(sql,(email))
    conn.commit()
    
    return cur.lastrowid

def main():
    st.title('EMAIL REGISTRATION')

    conn = my_connection('email_database.db')
    
    if conn is not None:
        create_table(conn)

        email=st.text_input('Enter your mail')

        if st.button('Register'):
            if email:
                insert_email(conn,email)
                st.seccess(f'You have successfully registered:{email}')
            else:
                st.warning('please enter valid mail')

        conn.close()
    else:
        st.error('there is error in database')

if __name__ =="__main__":
    main()