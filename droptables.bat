@echo off
FOR /f "tokens=2 delims=|" %%G IN ('psql --host localhost --username postgres --command="\dt" YOUR_TABLE_NAME') DO (
   psql --host localhost --username postgres --command="DROP table if exists %%G cascade" sfkb
   echo table %%G dropped
)