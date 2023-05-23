def validBraces(string):
    print(string)
    list_of_string=list(string)  
    print(list_of_string)
    # possible chars () [] {}
    # good: ({[{()}]}) or (){}[] or () or [] or {} or {}({})[]
    # bad: ([)] or ((()]) 
    left_rounded = string.count("(")
    right_rounded = string.count(")")
    left_square = string.count("[")
    right_square = string.count("]")
    left_curly = string.count("{")
    right_curly = string.count("}")
    if left_rounded != right_rounded or left_square != right_square or left_curly != right_curly:
        print("opening # != closing #")
        same_number = False
    else:
        print("opening # == closing #")
        same_number = True
    for char in string:
        if char == "(":
            left = string.find("(")
            right = string.find(")")
            if right < left:
                print("found ) before (")
                return False
            if (right-left) % 2 != 0 and (right-left)>0 and same_number:
                print("verified (), looks good")
                return True
            else:
                print("verified (), looks bad")
                return False
        if char == "[":
            left = string.find("[")
            right = string.find("]")
            if right < left:
                print("found ] before [")
                return False
            if (right-left) % 2 != 0 and (right-left)>0 and same_number:
                print("verified [], looks good")
                return True
            else:
                print("verified [], looks bad")
                return False
        if char == "{":
            left = string.find("{")
            print("found opening { at: %s" % left)
            right = string.find("}")
            print("found closing } at: %s" % right)
            if right < left:
                return False
            if (right-left) % 2 != 0 and (right-left)>0 and same_number:
                return True
            else:
                return False
    
validBraces("(({{[[]]}}))")
