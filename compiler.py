# compiler.py
import sys
from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer
from tacky_generator import TackyGenerator
from assembly_generator import AssemblyGenerator
from code_emitter import CodeEmitter
from driver import Driver

def main():
    driver = Driver()
    args = sys.argv[1:]

    if not args:
        print("Usage: python compiler.py [options] <filename.c>")
        sys.exit(1)

    if "--help" in args:
        driver.print_help()
        sys.exit(0)
    
    filename = args[-1]

    if not filename.endswith(".c"):
        print("Error: Input file must have a .c extension")
        sys.exit(1)

    try:
        with open(filename, 'r') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        sys.exit(1)

    # Lexing
    lexer = Lexer(source_code)
    tokens = lexer.lex()
    
    # Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # Semantic Analysis
    semantic_analyzer = SemanticAnalyzer(ast)
    transformed_ast = semantic_analyzer.analyze()

    # TACKY Generation
    tacky_gen = TackyGenerator(transformed_ast)
    tacky_code = tacky_gen.generate()

    # Assembly Generation
    assembly_gen = AssemblyGenerator(tacky_code)
    assembly_code = assembly_gen.generate()

    # Code Emission
    emitter = CodeEmitter(assembly_code)
    
    if "-S" in args:
        output_filename = filename[:-2] + ".s"
        emitter.emit_assembly(output_filename)
        print(f"Assembly code written to {output_filename}")
    else:
        output_filename = driver.run_assembler_and_linker(filename, assembly_code)
        print(f"Executable written to {output_filename}")

if __name__ == "__main__":
    main()