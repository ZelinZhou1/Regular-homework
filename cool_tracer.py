#!/usr/bin/env python
# coding: utf-8

from sys import monitoring

def on_start(code, offset):
    print(f"entering {code.co_name}")

def on_return(code, offset, retval):
    print(f"leaving {code.co_name}, return value: {retval}")

ID = 0
monitoring.use_tool_id(ID, "cool")
monitoring.register_callback(ID, monitoring.events.PY_START, on_start)
monitoring.register_callback(ID, monitoring.events.PY_RETURN, on_return)

def foo():
    return 30
def bar():
    return foo() + 10

monitoring.set_events(ID, monitoring.events.PY_START|monitoring.events.PY_RETURN)
bar()
monitoring.set_events(ID, 0)
monitoring.free_tool_id(ID)