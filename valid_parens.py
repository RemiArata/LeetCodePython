def valid_parens(s: str) -> bool:
    
    parens = {")": "(", "]": "[", "}": "{"}
    strng = []

    for itm in s:
        if itm in "({[":
            strng.append(itm)
        elif (strng == []) and (itm in "]})"):
            return False
        else:
            if strng[-1] == parens[itm]:
                strng.pop()
            else:
                break
    return not strng
    


s = "()"
print(valid_parens(s))

s = "()[]{}"
print(valid_parens(s))

s = "(]"
print(valid_parens(s))

s = "([)]"
print(valid_parens(s))