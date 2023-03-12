<div class="markdown prose w-full break-words dark:prose-invert light">
  <h1>Sungodra Portfolio</h1>
  <p>
    This repository manages the writing scripts for Sungodra's portfolio, utilizing open source software. The workspace is mostly designed for macOS, but is intended to be OS agnostic.
  </p>
  <p>
    Included is a local <code>vimrc</code> file that is used as an integrated development environment (IDE) for writing. To accomplish the traditional formatting of screenplays, several pieces of software are utilized:
  </p>
  <ul>
    <li>
      <p>
        <code>nvim</code>: <code>nvim</code> is an improved version of the Vim text editor with better performance, and added features. To install <code>nvim</code>, you can use the Homebrew package manager by running the command <code>brew install nvim</code>.
      </p>
    </li>
    <li>
      <p>
        <code>fountain.vim</code>: <code>fountain.vim</code> is a plugin for Vim and nvim that provides syntax highlighting and formatting for Fountain, a plain text markup language for screenwriting. You can install <code>fountain.vim</code> by adding the following line to your Vim or nvim plugin manager:
      </p>
      <pre>
        <code class="bg-black mb-4 rounded-md !whitespace-pre hljs language-python">Plug <span class="hljs-string">'rstacruz/fountain.vim'</span></code>
      </pre>
    </li>
    <li>
      <p>
        <code>pandoc</code>: <code>pandoc</code> is a command-line tool for converting between different document formats, including Fountain to PDF conversion. To install <code>pandoc</code> using Homebrew, run the command <code>brew install pandoc</code>.
      </p>
    </li>
    <li>
      <p>
        <code>mactex: pdflatex</code>: MacTeX is a distribution of the TeX/LaTeX typesetting system for macOS, which includes the <code>pdflatex</code> engine for generating PDF files. To install MacTeX, download and run the installer from the following website: <a href="https://tug.org/mactex/mactex-download.html" target="_new">https://tug.org/mactex/mactex-download.html</a>.
      </p>
    </li>
    <li>
      <p>
        <code>(homebrew):</code> no link needed.
      </p>
    </li>
  </ul>
  <p>
    By utilizing these tools, Sungodra can use the Vim text editor as an IDE for screenwriting in Fountain format and generate PDF files using the <code>pdflatex</code> engine.
  </p>
</div>
