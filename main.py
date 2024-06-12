import difflib

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def generate_latex_diff(file1, file2):
    code1 = read_file(file1)
    code2 = read_file(file2)
    
    # Get the diff between the two codes
    diff = difflib.ndiff(code1.splitlines(), code2.splitlines())

    # LaTeX document preamble
    latex_preamble = r'''
\documentclass{article}
\usepackage[svgnames]{xcolor}
  \definecolor{diffincl}{named}{Green}   % Brighter green for added lines
  \definecolor{diffrem}{named}{Red}      % Bright red for removed lines
  \definecolor{backcolour}{rgb}{0.95, 0.95, 0.92}

\usepackage{listings}
  \lstdefinelanguage{diff}{
    basicstyle=\ttfamily\small,
    morecomment=[f][\color{diffincl}]{+},     % Added lines
    morecomment=[f][\color{diffrem}]{-},      % Removed lines
  }

  \lstdefinestyle{mystyle}{
    language=diff,  % Setting the language to diff
    basicstyle=\footnotesize\ttfamily,
    breakatwhitespace=false,
    backgroundcolor=\color{backcolour},
    linewidth=\textwidth,   
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    commentstyle=\color{Red},
    keywordstyle=\color{Magenta},
    numberstyle=\tiny\color{Grey},
  }

\begin{document}

\begin{lstlisting}[style=mystyle]
'''

    # Generate the diff output without @@ lines
    diff_output = '\n'.join([line for line in diff if not line.startswith('@@')])

    # LaTeX document ending
    latex_end = r'''
\end{lstlisting}

\end{document}
'''

    # Combine all parts
    full_latex_document = latex_preamble + diff_output + latex_end

    return full_latex_document

# File paths for the code files
file1 = 'code1.java'
file2 = 'code2.java'

# Generate LaTeX document with diff
latex_document = generate_latex_diff(file1, file2)

# Output the LaTeX document to a .tex file
with open('code_diff.tex', 'w') as file:
    file.write(latex_document)

print("LaTeX diff document generated: code_diff.tex")

