# Compiler-From-Scratch
# C Compiler Project

This project implements a compiler for a subset of the C programming language, following the book "Writing a C Compiler" by Nora Sandler.

## Features

The compiler supports the following features:

-   **Data Types:**
    -   `int`
    -   `long`
    -   `double`
    -   `char`
    -   `signed` and `unsigned` modifiers
    -   `void`
    -   pointers
    -   arrays
    -   structures
-   **Operators:**
    -   Arithmetic: `+`, `-`, `*`, `/`, `%`
    -   Relational: `>`, `<`, `>=`, `<=`, `==`, `!=`
    -   Logical: `!`, `&&`, `||`
    -   Bitwise: `~`, `&`, `|`, `^`
    -   Assignment: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`
    -   Increment/Decrement: `++`, `--` (prefix and postfix)
    -   Address: `&`
    -   Dereference: `*`
    -   Member access: `.`, `->`
    -   Subscript: `[]`
    -   sizeof
    -   Type cast
    -   Comma
-   **Statements:**
    -   `if`
    -   `while`
    -   `do`
    -   `for`
    -   `break`
    -   `continue`
    -   `return`
-   **Functions:**
    -   Function declarations and definitions
    -   Function calls (including standard library functions)
-   **Variables:**
    -   Local and global variables
    -   Static variables
    -   Initialization
-   **Other:**
    -   Integer, floating-point, character, and string literals
    -   Comments

## Limitations

-   The following features are **not** implemented:
    -   `typedef`
    -   `goto`
    -   `switch` statements
    -   `union` types
    -   `float` and `long double` types
    -   `long long` type
    -   `struct` and `union` types as function parameters or return values
    -   `const`, `volatile`, and other type qualifiers
    -   `register`, `auto`, `_Thread_local` storage-class specifiers
    -   Bit-fields
    -   Variable-length arrays
    -   Designated initializers
    -   `#include` and preprocessor directives
    -   Variable number of arguments in function calls (e.g., `printf`)
    -   Function pointers
    -   Hexadecimal floating-point constants
    -   Multicharacter constants
    -   Wide character types and string literals
    -   Complex types
    -   Atomic types
    -   Generic selections

## Compilation Stages

The compiler follows these stages:

1. **Lexing:** Converts the source code into a stream of tokens.
2. **Parsing:** Builds an abstract syntax tree (AST) from the tokens.
3. **Semantic Analysis:**
    -   Identifier resolution
    -   Type checking
    -   Loop labeling
4. **TACKY Generation:** Translates the AST into TACKY intermediate representation.
5. **Assembly Generation:**
    -   Converts TACKY to x86-64 assembly code.
    -   Performs register allocation.
    -   Fixes up instructions.
6. **Code Emission:** Writes the assembly code to an output file.

## Usage

### Prerequisites

-   Python 3.8+
-   GCC (or Clang)
-   GNU Assembler (as)
-   GNU Linker (ld)

### Building

```bash
python compiler.py input.c
