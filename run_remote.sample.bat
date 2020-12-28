@echo off
setlocal

rem == ENTER SERVER PATH & YOUR ACCOUNT DATA ==
set SERVER_PATH=x: https://xxx.jp/yyy/zzz/
set USERNAME=admin_id
set PASSWORD=admin_pass

net use /del /y %SERVER_PATH% > nul 2>&1
net use %SERVER_PATH% /user:%USERNAME% %PASSWORD%
python auto-bk.py
net use x: /delete