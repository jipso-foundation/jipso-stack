import os
import sys

# -- Path setup --------------------------------------------------------------

# Thêm đường dẫn root của project
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'JIPSO'
author = 'JIPSO Foundation'
release = '0.1.35'

# -- General configuration ---------------------------------------------------

extensions = [
  'sphinx.ext.autodoc',       # Tự động generate API từ docstring
  'sphinx.ext.napoleon',      # Hỗ trợ Google style & NumPy style docstring
  'sphinx_autodoc_typehints', # Render type hint nếu có
  'sphinx.ext.autosummary',
  'myst_parser',              # Cho phép đọc file .md
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_title = 'jipso-stack'
html_theme = 'furo'
html_static_path = ['_static']
html_logo = 'https://cdn.jipso.org/logo/jipso_framework.svg'
html_favicon = 'https://cdn.jipso.org/logo/jipso_char_square.svg'

# -- Autodoc settings --------------------------------------------------------

autodoc_default_options = {
  'members': True,             # Xuất tất cả method/attribute public
  'undoc-members': True,       # Xuất cả những hàm không có docstring
  'private-members': False,    # Có thể bật True nếu muốn doc cả _private
  'special-members': '__init__',  # Show __init__ để thấy constructor
  'show-inheritance': True,
}

autoclass_content = 'class'    # Docstring class nằm trên class thay vì __init__

autosummary_generate = True

# Napoleon settings (cho Google/NumPy style)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
