import sys


class SExpression:
    # This is used to Pre-Calculated expressions for dynamic programming optimization
    pre_calculated = {}

    def calc(self, str_input):
        while ")" in str_input:
            # First is to check if already been calculated
            if str_input in self.pre_calculated:
                return self.pre_calculated[str_input]

            # Starting with the first expression to close (ie. first index of ")")
            right_bound = str_input.index(")")
            left_bound = str_input[:right_bound].rindex("(")

            # Since we're getting the first expression to close, it is guaranteed not to have nested functions inside
            value = self._evaluate_single(str_input[left_bound + 1:right_bound])

            # If it is evaluated final function
            if left_bound == 0:
                return value

            # Otherwise update str_input, then replacing expression with calculated value
            else:
                str_input = str_input[:left_bound] + str(value) + str_input[right_bound+1:]

        return int(str_input)

    # Evaluating the simple expression with no nested values
    def _evaluate_single(self, str_input):
        # To check if already been calculated
        if str_input in self.pre_calculated:
            return self.pre_calculated[str_input]

        pieces = str_input.split()

        if pieces[0] == "add":
            answer = int(pieces[1]) + int(pieces[2])

        elif pieces[0] == "multiply":
            answer = int(pieces[1]) * int(pieces[2])

        else:
            answer = int(str_input)

        # Adding it to pre calculated dict
        self.pre_calculated[str_input] = answer
        return answer


def main():
    try:
        print(SExpression().calc(sys.argv[1]))
    except Exception as error:
        print("Error:", error)
        print("Please enter a valid value or (FUNCTION EXPR EXPR)...")


if __name__ == '__main__':
    main()
