import sys
from antlr4 import *
from qasm3Lexer import qasm3Lexer
from qasm3Parser import qasm3Parser
from qasm3Listener import qasm3Listener

from antlr4.tree.Trees import Trees
import re

def main(argv):
    input = FileStream(argv[1])
    lexer = qasm3Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = qasm3Parser(stream)
    tree = parser.program()
    lisp_tree = Trees.toStringTree(tree, None, parser)
    import pdb; pdb.set_trace()

if __name__ == '__main__':
    main(sys.argv)
