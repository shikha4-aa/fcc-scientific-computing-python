def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_lines = []
    second_lines = []
    dash_lines = []
    answer_lines = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        left, operator, right = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        max_len = max(len(left), len(right))
        width = max_len + 2

        first_lines.append(left.rjust(width))
        second_lines.append(operator + ' ' + right.rjust(max_len))
        dash_lines.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(left) + int(right))
            else:
                answer = str(int(left) - int(right))
            answer_lines.append(answer.rjust(width))

    arranged_problems = (
        '    '.join(first_lines) + '\n' +
        '    '.join(second_lines) + '\n' +
        '    '.join(dash_lines)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_lines)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
