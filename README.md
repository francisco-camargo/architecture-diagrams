Architecture Diagrams
=====================

# Windows Installation

Install `graphviz`, [link](https://graphviz.org/download/). Downloaded zip file, unzipped file and moved contents into `C:\Program Files (x86)\Graphviz-10.0.1-win64\bin`.

I tried adding path to Windows environment variables but did not help any. Instead, in code I added the lines

```python
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz-10.0.1-win64/bin'
```

# Visualization in VSCode

Can render `.gv` files using a `graphviz` VSCode extension, eg. Graphviz Interactive Preview.

# Examples

Find a `graphviz` example in `src/graphviz_example/graphviz.example.py`.

Find a `diagrams` examples in `src/diagrams_example/`

Run any of these scripts and output files will be saved in the corresponding example folder.
