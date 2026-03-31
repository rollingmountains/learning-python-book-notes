import sys
import sysconfig

# print(sys.builtin_module_names)
# for m in sys.builtin_module_names:
#     print(m)
# print(sum(1 for m in sys.builtin_module_names if m[0] != "_"))
print(sys.path)


# import os
# import sys
# import sysconfig

# print(sys.__file__)

stdlib = sysconfig.get_paths()["stdlib"]
# print(os.listdir(stdlib))

# print(sys.modules.keys())

# print(dir(builtins))

# print(a, b, c)
# # print(sys.modules["sys"] is sys)
# # print(sys.modules["os"] is os)
# print(type(sys.modules))
# print(sys.modules.keys())

# for module in sys.stdlib_module_names:
#     if not module.startswith("_"):
#         print(module)
#         print(module)
#         print(module)
#         print(module)
