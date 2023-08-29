""" 
brackets_in_code.py

"""


class Bracket:
    """
    Bracket class.

    Stores bracket "[", "{", or "(" and its index in the input string

    """

    def __init__(self, character, index):
        self.character = character
        self.index = index

    def match_brackets(self, bracket_character):
        """
        Checks if brackets can be matched

        Args:
            bracket_character (str): Bracket character {, [, or (

        Returns:
            bool: True/False

        """

        if self.character == "[" and bracket_character == "]":
            return True

        if self.character == "{" and bracket_character == "}":
            return True

        if self.character == "(" and bracket_character == ")":
            return True

        return False


def brackets_in_code(input_str):
    """
    Compute the result of checking the brackets in code

    Args:
        input_str (str): Input string containing brackets

    Returns:
        str, int: 'Success' if matched, index of the first unmatched closing bracket

    """
    stack_list = []

    for i, character in enumerate(input_str, start=1):
        if character in ("[", "(", "{"):
            stack_list.append(Bracket(character, i))

        elif character in ("]", ")", "}"):
            if not stack_list:
                return i

            top = stack_list.pop()
            if not top.match_brackets(character):
                return i

    if stack_list:
        top = stack_list.pop()
        return top.index

    return "Success"


if __name__ == "__main__":
    INPUT_STRING = str(input())
    print(brackets_in_code(INPUT_STRING))
