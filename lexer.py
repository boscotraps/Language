def lex_num(line): #done
    num = ""
    # iterate through the line
    for c in line:
        # if the character is not a digit
        if not c.isdigit():
            break
        # add the digit to num
        num += c
        
    return 'num', int(num), len(num)

def lex_str(line): #done
    delimiter = line[0]
    string = ""
    # iterate through the line
    for c in line:
         #adds each character to the string
         string += c
    return 'str', string, len(string)

def lex_id(line): #done
    # keywords
    keys = ['print', 'while', 'if', 'elif', 'else']
    # id is a name assigned by the user (variable name)
    id = ""
    # iterate through the line
    for c in line:
        # if the character is not a digit, letter, or underscore
        if not (c.isdigit() and c.isalpha and c == "_"):
            break
        id += c
    if id in keys:
        # keyword
        return 'key', id, len(id)
    else:
        # variable name
        return 'ID', id, len(id)

def lex(line): #done
    count = 0
    while count < len(line):
        lexeme = line[count]
        if lexeme.isdigit():
            #variables: type, token, consmued
            #consumed is thee length of the token
            #sets those variables to the return values of the function lexNum
            # line[count:] is the substring of line from count to the end
            typ, tok, consumed = lex_num(line[count:])
            count += consumed
        elif lexeme == '"' or lexeme == "'":
            typ, tok, consumed = lex_str(line[count:])
            lexeme_count += consumed
        elif lexeme.isalpha():
            typ, tok, consumed = lex_str(line[count:])
            count += consumed
        else:
            count += 1
code = input()
lex(code)