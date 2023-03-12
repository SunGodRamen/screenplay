Sungodra Portfolio
This repository manages the writing scripts for Sungodra's portfolio, utilizing open source software. The workspace is mostly designed for macOS, but is intended to be OS agnostic.

Included is a local vimrc file that is used as an integrated development environment (IDE) for writing. To accomplish the traditional formatting of screenplays, several pieces of software are utilized:

nvim: nvim is an improved version of the Vim text editor with better performance, and added features. To install nvim, you can use the Homebrew package manager by running the command brew install nvim.

fountain.vim: fountain.vim is a plugin for Vim and nvim that provides syntax highlighting and formatting for Fountain, a plain text markup language for screenwriting. You can install fountain.vim by adding the following line to your Vim or nvim plugin manager:

python
Copy code
Plug 'rstacruz/fountain.vim'
pandoc: pandoc is a command-line tool for converting between different document formats, including Fountain to PDF conversion. To install pandoc using Homebrew, run the command brew install pandoc.

mactex: pdflatex: MacTeX is a distribution of the TeX/LaTeX typesetting system for macOS, which includes the pdflatex engine for generating PDF files. To install MacTeX, download and run the installer from the following website: https://tug.org/mactex/mactex-download.html.

(homebrew): no link needed.

By utilizing these tools, Sungodra can use the Vim text editor as an IDE for screenwriting in Fountain format and generate PDF files using the pdflatex engine.
