# pdf merger
Looks for pdfs prepended with numbers and merges them ordered in increasing order.  
Eg. merge in this order: 0a, 1a, 3a, 10a, 99a

By default, the name is "joined.pdf" and placed in the same directory as the python tool.
## Options:
* `-n/--name`: name of the pdf resulting from the merge
* `-p/--path`: filepath to directory of pdfs to combine
* `-d/--dest`: place the output in the same path (if path is not specified with -p/--path, then it will place it in the same directory as the python tool)
* `-v/--verbose`: print the name of the files merged
