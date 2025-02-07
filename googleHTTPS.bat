@echo off
setlocal
set "query=%*"
set "query=%query: =+%"
start "" "%query%"
endlocal
