# DreamHack Wargame

- xss-1
  : 
```python
@app.route("/vuln")
def vuln():
    param = request.args.get("param", "")
    return param
```

# vm 우분투 설치
