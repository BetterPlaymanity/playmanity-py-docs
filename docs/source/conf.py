# Configuration file for the playmanity documentation builder.

# -- Project information

project = 'Playmanity.py'
copyright = '2023, BetterPlaymanity'
author = 'TheLite'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'asyncio',
    'requests'
]

interplaymanity_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'playmanity': ('https://playmanity.com', None),
}
interplaymanity_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for EPUB output
epub_show_urls = 'footnote'
