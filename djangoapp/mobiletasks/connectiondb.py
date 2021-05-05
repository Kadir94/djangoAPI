import asyncio
import sqlite3
from fetch_data import get_info

conn = sqlite3.connect('../../mobile.db')
result = asyncio.get_event_loop().run_until_complete(get_info())
c = conn.cursor()
# Create table - STATIONS
c.execute('''CREATE TABLE STATIONS
             ([generated_id] INTEGER PRIMARY KEY ,[Station_id] TEXT, [Station_Name] TEXT, [Latitude] FLOAT, [Longnitude] FLOAT)''')
for r in result:
    c.execute("INSERT INTO STATIONS VALUES (NULL, :Station_id, :Station_Name, :Latitude, :Longnitude)", r)

conn.commit()
