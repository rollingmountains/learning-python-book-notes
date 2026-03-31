import os
import timeit

defnum, defrep = 1000, 5


# orchestrator sets up stage and actual execution platform of the play
def runner(
    statements, pythons=None
):  # contract with the play troupe on the format of the play
    for number, repeat, stmt, name in statements:
        number = number or defnum
        repeat = repeat or defrep
        if not pythons:
            result = min(timeit.repeat(number=number, repeat=repeat, stmt=stmt))
            print(f"{result} --> {name}")
        else:
            for python in pythons:
                # structure the command prompt
                # actual command
                # python -m timeit -n 1000 -r 50 "Expression"
                cmd = f'{python} -m timeit -n {number} -r {repeat} "{stmt}"'

                output = os.popen(cmd).read()
                print(
                    python,
                    name,
                    output,
                )


# make this moduel a script
if __name__ == "__main__":
    # execute the orchestrator
    import sys

    namespace = sys.modules[__name__]
    print(namespace.__dict__)
