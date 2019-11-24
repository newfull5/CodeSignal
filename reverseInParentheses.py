def reverseInParentheses(inputString):
    
    if inputString[0] == '(' or inputString[-1]:
        return inputString[1:len(inputString)-1][::-1]
    
    left = ''
    right = ''
    center = ''
    answer = ''
    centence = ''

    for i in range(0, len(inputString)):
        if inputString[i] == '(':
            left += inputString[:i]
            center += inputString[i+1:]
            
    for i in range(1, len(inputString)):
        if inputString[-i] == ')':
            right += inputString[-i+1:]
            answer += center[:(-i)]
            
    centence = left + answer[::-1] + right
        
    return centence
