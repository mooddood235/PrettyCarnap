def main():
    in_path = input("Input path: ")
    out_path = input("Output path: ")

    f_in = open(in_path, 'r')
    lines = f_in.readlines()
    f_in.close()

    pretty_lines = ['\\begin{fitch}\n'] + MakePretty(lines, 1, []) + ['\\end{fitch}\n']

    f_out = open(out_path, 'w')
    f_out.writelines(pretty_lines)
    f_out.close()


def MakePretty(lines, line_num, transfered):
    if not lines:
        return []

    line = lines[0]
    line_depth = Depth(line)
    if 'Show' in line:
        close_line_index = FirstLineWithSameDepthIndex(line_depth, lines)
        conclusion = line.split(':')[1].strip()
        white_space = ''.join(' ' for _ in range(line_depth))
        lines[close_line_index] = '{}{} {}'.format(white_space, conclusion, lines[close_line_index])
        transfered.append((line_num, line_num + close_line_index))
        return MakePretty(lines[1:], line_num + 1, transfered)
    else:
        tokens = line.split(':')
        statement = tokens[0].strip()
        rule = tokens[1].strip()

        pretty_statement = statement \
            .replace('v', '\\vee ') \
            .replace('^', '\\wedge ') \
            .replace('->', '\\rightarrow ') \
            .replace('~', '\\neg ') \
            .replace('P', 'A') \
            .replace('Q', 'B') \
            .replace('R', 'C') \
            .replace('S', 'D') \
            .replace('T', 'E') \
            .replace('U', 'F') \
            .replace('p', '\\phi') \
            .replace('q', '\\psi')

        pretty_rule = FixRuleNumbers(rule, transfered)
        pretty_rule = pretty_rule \
            .replace(':AS', 'AS') \
            .replace(':PR', 'PR') \
            .replace(':MTP', '$\\vee E$ ') \
            .replace(':ADD', '$\\vee I$ ') \
            .replace(':S', '$\\wedge E$ ') \
            .replace(':ADJ', '$\\wedge I$ ') \
            .replace(':MP', 'MP ') \
            .replace(':CD', '$\\implies \\!\\!\\!\\! I$ ' ) \
            .replace(':DNE', '$\\neg E$ ') \
            .replace(':ID', '$\\neg I$' ) \
            .replace(':D-AC', 'AC ') \
            .replace(':DD', 'DD ')

        fas, fhs = GetFasAndFhs(line_depth, rule, lines)

        return ['{}{} {} & {} \\\\\n'.format(fas, fhs, pretty_statement, pretty_rule)] \
               + MakePretty(lines[1:], line_num + 1, transfered)


def GetFasAndFhs(line_depth, rule, lines):
    fas = ''
    fhs = ''

    if 'AS' in rule:
        fhs = '\\fh'
        for i in range(line_depth - 1):
            fas += '\\fa'
    elif 'PR' in rule and len(lines) > 1 and ':PR' not in lines[1]:
        fhs = '\\fj'
        for i in range(line_depth - 1):
            fas += '\\fa'
    else:
        for i in range(line_depth):
            fas += '\\fa'
    return fas, fhs


def FixRuleNumbers(rule, transfered):
    rule = rule.removeprefix(':').replace(' ', '')
    tokens = rule.split(',')

    index_of_first_digit = IndexOfFirstDigit(tokens[0])
    rule_name = tokens[0]
    numbers = ['']

    if index_of_first_digit:
        rule_name = tokens[0][:IndexOfFirstDigit(tokens[0])]
        numbers = [tokens[0][IndexOfFirstDigit(tokens[0]):]] + tokens[1:]

        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])

            for (frm, to) in transfered:
                if numbers[i] == frm:
                    numbers[i] = to
                    break
            n = numbers[i]
            for (frm, to) in transfered:
                if n >= frm:
                    numbers[i] -= 1

    pretty_rule = ':{} {}'.format(rule_name, numbers[0])
    for n in numbers[1:]:
        pretty_rule += ',{}'.format(n)

    return pretty_rule


def IndexOfFirstDigit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return i
    return None


def FirstLineWithSameDepthIndex(depth, lines):
    for i in range(1, len(lines)):
        if Depth(lines[i]) == depth:
            return i


def Depth(line):
    n = 0
    while line[0] == ' ':
        n += 1
        line = line[1:]
    return n


if __name__ == '__main__':
    main()
