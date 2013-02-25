from .. import yaplat as yp
import numpy as np



def test1():
    a = np.array([[5,6,7],[4,5,6]])
    expected = """\\begin{tabular}[ht!]{l|c|c|c}
    & 0 & 1 & 2 \\\\
    \\hline
    \\hline
    0 & 5 & 6 & 7 \\\\
    \\hline
    1 & 4 & 5 & 6 \\\\
\end{tabular}"""
    result = yp.gen_table(a)
    print result
    print expected
    assert expected == result

def test2():
    a = np.array([[5,6,7],[4,5,6]])
    cols = ['col1','col2','col3']
    rows = ['row1','row2']
    expected = """\\begin{tabular}[ht!]{l|c|c|c}
    & col1 & col2 & col3 \\\\
    \\hline
    \\hline
    row1 & 5 & 6 & 7 \\\\
    \\hline
    row2 & 4 & 5 & 6 \\\\
\end{tabular}"""
    result = yp.gen_table(a, columns=cols, rows=rows)
    print result
    print expected
    assert expected == result
