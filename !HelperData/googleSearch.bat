@echo off
setlocal
set "query=%*"
set "query=%query: =+%"
start "" "https://www.google.com/search?q=%query%"
endlocal
