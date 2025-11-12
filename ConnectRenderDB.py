#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import psycopg2
import pandas as pd

def main():
    st.title("Render PostgreSQL DB Output")

    # ⚡ Hardcoded DB Connection Info
    host="dpg-d3t5f4mmcj7s73fgm5s0-a.oregon-postgres.render.com"
    port=5432
    dbname="slothdb3"
    user="slothdb3_user"
    password="uWqtzvpmgNXMs9dWLZuEKDu4mH3RlxAR"

    if st.button("Fetch Tables"):
        try:
            # Connect to Render PostgreSQL
            conn = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password
            )

            query = """
            SELECT * from messages order by created_at desc;
            """

            df = pd.read_sql(query, conn)
            st.write("✅ Tables in your database:")
            st.dataframe(df)

            conn.close()
        except Exception as e:
            st.error(f"❌ Error connecting to DB:\n{e}")

if __name__ == "__main__":
    main()




