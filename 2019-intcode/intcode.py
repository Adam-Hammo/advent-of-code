from collections import defaultdict
from typing import Generator


def parse_program(program: str) -> defaultdict[int, int]:
    return defaultdict(int, {i: int(p) for i, p in enumerate(program.split(","))})


def compute(program: list[int]) -> Generator[int, int, None]:
    def get_reference(
        p: int, offset: int, relative_base: int, parameter_modes: int
    ) -> int:
        parameter_mode = (parameter_modes // 10 ** (offset - 1)) % 10
        if parameter_mode == 0:
            return program[p + offset]
        elif parameter_mode == 1:
            return p + offset
        elif parameter_mode == 2:
            return relative_base + get_reference(p, offset, 0, 0)
        else:
            raise NotImplementedError(
                f"Parameter mode {parameter_mode} reached but not implemented"
            )

    p, relative_base = 0, 0
    try:
        while (instruction := program[p]) != 99:
            opcode, parameter_modes = instruction % 100, instruction // 100
            ref = lambda i: get_reference(p, i, relative_base, parameter_modes)

            if opcode == 1:
                program[ref(3)] = program[ref(1)] + program[ref(2)]
                p += 4
            elif opcode == 2:
                program[ref(3)] = program[ref(1)] * program[ref(2)]
                p += 4
            elif opcode == 3:
                program[ref(1)] = yield
                p += 2
            elif opcode == 4:
                yield program[ref(1)]
                p += 2
            elif opcode == 5:
                p = program[ref(2)] if program[ref(1)] else p + 3
            elif opcode == 6:
                p = program[ref(2)] if not program[ref(1)] else p + 3
            elif opcode == 7:
                program[ref(3)] = int(program[ref(1)] < program[ref(2)])
                p += 4
            elif opcode == 8:
                program[ref(3)] = int(program[ref(1)] == program[ref(2)])
                p += 4
            elif opcode == 9:
                relative_base += program[ref(1)]
                p += 2
            else:
                raise NotImplementedError(
                    f"Opcode {opcode} reached but not implemented"
                )
    except IndexError:
        raise Exception(f"Segfault")
