#!/usr/bin/env python3

import cgi
import json
import subprocess

# 读取用户输入
form = cgi.FieldStorage()
user_input = form.getvalue('input', '')

# 在外部执行 Python 脚本并获取输出
try:
    output = subprocess.check_output(['python3', 'external_script.py', user_input], stderr=subprocess.STDOUT, text=True)
except subprocess.CalledProcessError as e:
    output = e.output

# 返回结果给前端页面
response = {'result': f"You entered: {user_input}", 'output': output}
print("Content-Type: application/json")
print()
print(json.dumps(response))
