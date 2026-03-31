import sys

import socket_rollback
import socket_run

print("socket_run" in sys.modules)
print("socket_rollback" in sys.modules)
print(socket_run.run_socket())
print(socket_rollback.rollback_socket())
# print(vars(vars(sys.modules["__main__"])["socket_run"]).keys())
# print(vars(vars(sys.modules["__main__"])["socket_rollback"]).keys())
