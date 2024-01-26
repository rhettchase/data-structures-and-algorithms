def multi_bracket_validation(input_string):
    # Dictionary to match opening and closing brackets
    brackets = {")": "(", "}": "{", "]": "["}

    # Stack to keep track of opening brackets
    stack = []

    # Iterating through each character in the input string
    for char in input_string:
        # If the character is a closing bracket (looks at the keys)
        if char in brackets:
            # Pop an element from the stack if it's not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'

            # Check if the popped element matches the corresponding opening bracket
            if brackets[char] != top_element:
                return False
        # If the character is an opening bracket, push it onto the stack
        elif char in brackets.values():
            stack.append(char)

    # If the stack is empty, all brackets were balanced
    return not stack

# # Example test cases
# print(multi_bracket_validation("[]"))         # True
# print(multi_bracket_validation("]["))         # False
# print(multi_bracket_validation("{}"))         # True
# print(multi_bracket_validation("}{"))         # False
# print(multi_bracket_validation("()"))         # True
# print(multi_bracket_validation(")("))         # False
# print(multi_bracket_validation("{}(){}"))     # True
# print(multi_bracket_validation("{([])}"))     # True
# print(multi_bracket_validation("[}"))         # False

