import ast
root = ast.parse("import os")
root2 = ast.parse("from bs4 import BeautifulSoup")
print(ast.dump(root))
print(ast.dump(root2))
