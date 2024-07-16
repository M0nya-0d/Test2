#Job.py
while True:
  with open("script.py") as f:
    code = compile(f.read(), "script.py", 'exec')
    exec(code)
