string = """\cvtag{Python}
\cvtag{C}
\cvtag{Java}
\cvtag{Arduino}
\cvtag{Lisp}
\cvtag{C++}
\cvtag{MATLAB}
\cvtag{Verilog HDL}
\cvtag{Swift}
\cvtag{Git}
\cvtag{Linux/Unix}
\cvtag{LaTeX}
\cvtag{AutoCAD}
\cvtag{SolidWorks}
\cvtag{3D Printing}"""
string = string.replace("\n", "").replace("\cvtag{", "").split("}")[:-1]
string = ", ".join(string)
print(string)