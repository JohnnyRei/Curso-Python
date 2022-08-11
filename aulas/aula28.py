"""
* Operador ternário em Python.
"""


from logging import logProcesses


logger_user = True

"""
if logger_user:
    msg = ("O usuário está logado")
else:
    msg = ("O usuário precisa precisa estar logar")

print(msg)
"""

if logger_user:
    # ! Operador ternário.
    msg = "O usuário está logado." if logger_user else "O usuário precisa precisa estar logar"
print(msg)
