
PREAMBLE = '\\begin{tabular}[%s]{%s}'
POSTAMBLE = '\\end{tabular}'
HLINE = '\\hline'

def gen_table(array, columns=None, rows=None,
              format='default', pos='ht!'):
    result = []
    if format == 'default':
        format = ['l']
        for col in range(array.shape[1]):
            format.append('c')
        format = '|'.join(format)
    result.append(PREAMBLE % (pos, format))
    if not columns:
        columns = [str(i) for i in range(array.shape[1])]
    columns.insert(0, '')
    if not rows:
        rows = [str(i) for i in range(array.shape[0])]

    result.append('   ' + ' & '.join(columns) + ' \\\\')
    result.append('    ' + HLINE)
    for i, row in enumerate(rows):
        result.append('    ' + HLINE)
        str_row = ' & '.join([row] + [str(cell) for cell in array[i]])
        result.append('    ' + str_row + ' \\\\')
    result.append(POSTAMBLE)

    return '\n'.join(result)
