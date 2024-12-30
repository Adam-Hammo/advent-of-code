from typing import Generator


def compute(program: list[int]) -> Generator[int, int, None]:
    def get_reference(p: int, offset: int, parameter_modes: int) -> int:
        parameter_mode = (parameter_modes // 10 ** (offset - 1)) % 10
        if parameter_mode == 0:
            return program[p + offset]
        elif parameter_mode == 1:
            return p + offset
        else:
            raise NotImplementedError(
                f"Parameter mode {parameter_mode} reached but not implemented"
            )

    p = 0
    try:
        while (instruction := program[p]) != 99:
            opcode, parameter_modes = instruction % 100, instruction // 100
            ref = lambda i: get_reference(p, i, parameter_modes)

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
            else:
                raise NotImplementedError(
                    f"Opcode {opcode} reached but not implemented"
                )
    except IndexError:
        raise Exception(f"Segfault")
