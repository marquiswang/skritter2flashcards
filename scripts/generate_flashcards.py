#!/usr/bin/python3

import csv
import sys

header = r"""\NeedsTeXFormat{LaTeX2e}[1996/12/01]
\ProvidesFile{business.tex}
\documentclass[avery5371]{flashcards}
\usepackage{CJKutf8}
\usepackage{multicol}
\usepackage{anyfontsize}

\cardfrontstyle[\fontsize{50}{60}]{plain}
\cardbackstyle[\large]{plain}

% Definitions of Pinyin
\makeatletter
\def\py@yunpriv#1{%
  \if a#1 10\else
  \if o#1 9\else
  \if e#1 8\else
  \if i#1 7\else
  \if u#1 6\else
  \if v#1 5\else
  \if A#1 4\else
  \if O#1 3\else
  \if E#1 2\fi\fi\fi\fi\fi\fi\fi\fi\fi0
}

\def\py@init{%
  \edef\py@befirst{}%
  \edef\py@char{}\edef\py@tuneletter{}%
  \def\py@last{}%
  \def\py@tune{5}%
}

% Usage:
% \pinyin{Hao3hao3\ xue2xi2} （好好学习）
\def\pinyin#1{%
  \edef\py@postscan{#1}%
  \py@init
  % scan
  \loop
  \edef\py@char{\expandafter\@car\py@postscan\@nil}%
  \edef\py@postscan{\expandafter\@cdr\py@postscan\@nil}%
  \ifnum 0 < 0\py@char
    \edef\py@tune{\py@char}%
    \py@first \py@tuneat\py@tuneletter\py@tune \py@last\kern -4sp\kern 4sp{}\py@init
  \else
    \ifnum\py@yunpriv\py@char > \py@yunpriv\py@tuneletter
      \edef\py@tuneletter{\py@char}\edef\py@first{\py@befirst}\def\py@last{}%
    \else
      \edef\py@last{\py@last\if v\py@char\"u\else\py@char\fi}%
    \fi
    \edef\py@befirst{\py@befirst\if v\py@char\"u\else\py@char\fi}%
  \fi
  \ifx\py@postscan\@empty\else
  \repeat
}

\let\py@macron \=
\let\py@acute \'
\let\py@hacek \v
\let\py@grave \`

%% \py@tuneat{Letter}{tune}
\def\py@tuneat#1#2{%
  \if v#1%
    \py@tune@v #2%
  \else
  \if i#1%
    \py@tune@i #2%
  \else
    \ifcase#2%
      \or\py@macron #1\or\py@acute #1\or\py@hacek #1\or\py@grave #1\else #1%
    \fi
  \fi\fi
}

\def\py@tune@v#1{{%
    \dimen@ii 1ex%
    \fontdimen5\font 1.1ex%
    \rlap{\"u}%
    \fontdimen5\font .6ex%
    \ifcase#1%
      \or\py@macron u\or\py@acute u\or\py@hacek u\or\py@grave u\else u%
    \fi
    \fontdimen5\font\dimen@ii
  }}

\def\py@tune@i#1{%
  \ifcase#1
    \or\py@macron \i\or\py@acute \i\or\py@hacek \i\or\py@grave \i\else i%
  \fi
}
\makeatletter
%end pinyin

\begin{document}
\begin{CJK*}{UTF8}{bkai}
"""

flashcard_header=r"""\begin{flashcard}[]{"""

flashcard_2=r"""}

\begin{minipage}[t][1.5in][c]{1.25in}
\begin{center}
\pinyin{"""

flashcard_3 = r"""}
\end{center}
\end{minipage}
\hspace{0.25in}
\begin{minipage}[t][1.5in][c]{1.25in}
\begin{center}"""

flashcard_4 = r"""\end{center}
\end{minipage}
\end{flashcard}"""

footer = r"""\clearpage\end{CJK*}
\end{document}

\endinput"""

input_file = sys.argv[1]

with open("flashcards.tex", "w") as output:
    output.write(header)

    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for row in reader:
            word = row[0]
            pinyin = row[1]
            definition = row[2]
            type = row[3]
            if type == '[simplified]':
                print("Skipping " + word)
                continue

            output.write(flashcard_header)
            output.write(word)
            output.write(flashcard_2)
            output.write(pinyin)
            output.write(flashcard_3)
            output.write(definition)
            output.write(flashcard_4)

    output.write(footer)