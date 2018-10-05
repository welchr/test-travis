# Building the docs

## Setup

If you don't already have pipenv, you'll need that first: 

```bash
# If you have root permission to install packages globally
# Or if you're using Anaconda/Miniconda or Linuxbrew
pip3 install pipenv

# Otherwise, install it in your home, and add it to your PATH
pip3 install --user pipenv
echo 'export PATH=$HOME/.local/bin:$PATH' >> $HOME/.bashrc
```

Then, install the dependencies from `Pipfile.lock` by doing: 

```bash
pipenv sync
```

Then clone the docs:

```bash
git clone https://github.com/statgen/...
```

## Build

Now run the Makefile with `pipenv run make html`. This should build all docs into `_build`.

All of the documentation files are written in Markdown and located in `docs`. The only reStructuredText file is `index.rst`.

## Syntax hints

With the installed packages `recommonmark` and `sphinx-markdown-tables`, along with changes to `conf.py`, you can use both markdown or RST types of tables. 

Click the "page source" link in the bottom right to see the code for these two examples. 

This is an example of an RST table: 

```eval_rst
+------+--------+-----+
| Test | Column | Foo |
+======+========+=====+
| A    | B      | C   |
+------+--------+-----+
```

This is an example of a markdown table:

| Test | Blah | Wee |
|------|------|-----|
| A    | B    | C   |
