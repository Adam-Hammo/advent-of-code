from typing import Optional

def execute(program: list[int], _input: Optional[int] = None) -> list[int]:
    p = 0
    output: list[int] = []
    try:
        while (opcode:=program[p]) != 99:
            if opcode==1: 
                program[program[p+3]] = program[program[p+1]] + program[program[p+2]]
                p += 4
            elif opcode==2: 
                program[program[p+3]] = program[program[p+1]] * program[program[p+2]]
                p += 4
            elif opcode==3: 
                if _input is None:
                    raise Exception("Input opcode reached but no input specified.")
                program[program[p+1]] = _input
                p += 2
            elif opcode==4:
                output.append(program[p+1])
                p += 2
            else:
                raise NotImplementedError(f"Opcode {opcode} reached but not implemented")
    except IndexError as e:
        raise Exception(f"Segfault. Tried accessing {e}, program has size {len(e)}")

    return output