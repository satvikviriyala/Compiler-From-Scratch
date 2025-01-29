# driver.py
import subprocess

class Driver:
    def __init__(self):
        self.options = {
            "-h", "--help",
            "-O",
            "--fold-constants",
            "--propagate-copies",
            "--eliminate-unreachable-code",
            "--eliminate-dead-stores",
            "--optimize",
            "-c",
            "-S",
            "--int-only"
        }
        
    def print_help(self):
        print("Usage: python compiler.py [options] <filename.c>")
        print("Options:")
        print("  -h, --help\t\t\tPrint this help message")
        print("  -O\t\t\t\tEnable all optimizations")
        print("  --fold-constants\t\tEnable constant folding")
        print("  --propagate-copies\t\tEnable copy propagation")
        print("  --eliminate-unreachable-code\tEnable unreachable code elimination")
        print("  --eliminate-dead-stores\tEnable dead store elimination")
        print("  -c\t\t\t\tCompile to object file (.o), but do not link")
        print("  -S\t\t\t\tCompile to assembly (.s), but do not assemble or link")
        print("  --int-only\t\t\tOnly enable support for integer types (no long, float, double, char, or void)")
    
    def run_assembler_and_linker(self, filename, assembly_code):
        assembly_filename = filename[:-2] + ".s"
        with open(assembly_filename, 'w') as f:
            for instruction in assembly_code:
                f.write(str(instruction) + '\n')

        object_filename = filename[:-2] + ".o"
        subprocess.run(["gcc", "-c", assembly_filename, "-o", object_filename])
        
        executable_filename = filename[:-2]
        subprocess.run(["gcc", object_filename, "-o", executable_filename])

        return executable_filename