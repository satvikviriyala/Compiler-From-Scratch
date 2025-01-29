# emitter.py
class CodeEmitter:
    def __init__(self, assembly_code):
        self.assembly_code = assembly_code

    def emit_assembly(self, output_filename):
        with open(output_filename, 'w') as f:
            for instruction in self.assembly_code:
                f.write(str(instruction) + '\n')