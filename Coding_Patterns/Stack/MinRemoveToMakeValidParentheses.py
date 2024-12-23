def min_remove_parentheses(s):
    stack = []
    s_list = list(s)
    
    for i, val in enumerate(s):
        # if stack is not empty and top element of stack is an opening parenthesis
        # and the current element is a closing parenthesis
        if len(stack) > 0 and stack[-1][0] == '(' and val == ')':
            # pop the opening parenthesis as it makes a valid pair 
            # with the current closing parenthesis
            stack.pop()

        # if the current value is an opening or a closing parenthesis
        elif val == '(' or val == ')':
            # push onto stack 
            stack.append([val, i])

    # Remove the invalid parentheses
    for p in stack:
        s_list[p[1]] = ""
    
    # convert the list to string
    result = ''.join(s_list)
   
    return result

#Time-Complexity = O(n)
#Space-Complexity = O(n)
