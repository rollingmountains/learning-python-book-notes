import printer

printer.x = 0
printer.y = "this is caller"
printer.z = ("test", "demo")
printer.a.append(10)
printer.b["three"] = 3

import printer

print(printer.a, printer.b, printer.x, printer.y, printer.z)

import print_call_proxy

print(print_call_proxy)
