# 🥸 Nerdyseq

Programmatically find the $nth$ term for *any* sequence.

## ⌨️ Getting Started

- Clone the repository: `git clone https://github.com/codonade/nerdyseq.git`
- Open VS Code: `cd nerdyseq && code .`
  - If you want to reuse an already open VS Code instance, you can append `-r`
- Install any recommended workspace extensions.
- Open the command pallette with `Ctrl + Shift + P` (or `Cmd + Shift + P` if you're
on MacOS) and select `Python: Create Environment > Venv`
  - Ensure to select a Python version above `3.12.4`
  - In the dependencies installation prompt, select [`requirements.txt`](requirements.txt)
- Run `Python: Select Interpreter` and choose the `.venv` one.
- Restart VS Code. You can do that easily with the `Developer: Reload Window` command,
or manually if you prefer.
- Create a new terminal instance through `Terminal: Create New Terminal` or
`Ctrl + Shift + \``
- Type in `python3 main.py` and you should be good to go!

## 🤔 The Reason Why

I've created this program after spending nearly two hours trying to find the $nth$
term for a sequence present in my 10th grade mathematics book. It's in no means
perfect, and it starts hallucinating quickly when provided with complex sequences,
but building it was fun, and I've learned a lot through out the process.
