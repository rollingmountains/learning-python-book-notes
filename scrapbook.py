# transform code into byte code
import dis
print(dis.dis('string'))

# byte code with duck typing in action
# run the code using 'uv run python -m dis scrapbook.py' command for bytecode output


class Animal:
    def make_sound(self, sound):
        print(f'{sound}')


cow = Animal()
cow.make_sound = lambda sound: print(f'{sound}')
cow.make_sound('woof')
