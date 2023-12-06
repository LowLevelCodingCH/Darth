import sys
argv = sys.argv


list; memstack = []

fname = argv[1]
retfile = argv[2]

with open(fname, "r") as file:
    
    iteration = 0

    file_read = file.read()
    print(file_read)

    lines = file_read.split("\n")
    if(lines[0] == "void main():"):

        memstack.append("Function::Void::main")
# Array Syntax: <FUNCTION>::<RETURN_TYPE>::<NAME> or <DATA>
# <DATA>: any string or integer etc. mostly coming after a function or keyword as argument or plain data
# <FUNCTION>: Print, Return, Function (for the "main" function)
# <RETURN_TYPE>: Void, CharacterArray, Character, Any, SystemInteger32BitSigned, SystemInteger32BitUnsigned, Array, FloatingPointNumber32Bit, SystemLong64BitSigned, SystemLong64BitUnsigned
# <NAME>: any name, "ANY", or "main"
# [CLASS_TYPE]: type of arrays, like {INFORMATION} for <DATA> and {DECLARE} for <FUNCTION>::<RETURN_TYPE>::<NAME>
        for line in lines:

            file_line = lines[iteration]

            if file_line.startswith("    Std::Print >> "):

                memstack.append("Print::CharacterArray::ANY")

                file_line_str_print = file_line[18:]

                memstack.append(file_line_str_print)
                if len(memstack) >= 32768:
                    exit()

            elif file_line.startswith("    Return "):

                memstack.append("Return::SystemInt32Bit::ANY")

                file_line_int_return = file_line[11:]

                memstack.append(file_line_int_return)
                if len(memstack) > 32768:
                    exit()
            
            elif file_line.startswith("    import "):

                with open(file_line[11:], "r") as read_file_import:
                    memstack.append(read_file_import.read())

            iteration += 1
    
    if len(memstack) > 32768:
        exit()
with open(retfile, "w") as returnfileobj:
    arrleng = str(memstack).replace("\"", "")
    arrlen = arrleng.replace("\"", "")
    returnfileobj.write(arrlen)
if argv[3] == "-dbg":
        arrlenga = str(memstack).replace("\"", "")
        arrlena = arrlenga.replace("\"", "")
        print(f"""
-------------MEMSK-------------
Memory stack: {memstack}
Memory size: {len(memstack)}
Ram: {len(memstack)}/32678 spaces used
Disk: {len(arrlena)}B used
Disk data: {arrlena}
Return file: {retfile}

-------------DEBUG-------------
Code file: \n\"\"\"\n{file_read}\n\"\"\"
Code name: {fname}
Code size: {len(file_read)}
"""
)