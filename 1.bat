@echo off  
set INTERVAL=10
timeout %INTERVAL%
:Again  
echo Called000000000000000
python 1.py
timeout %INTERVAL%
goto Again  