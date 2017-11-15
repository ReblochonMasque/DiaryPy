from distutils.core import setup
setup(
  name = 'diarypy',
  packages = ['diarypy'],
  install_requires=[
    'os',
    'sys',
    'errno',
    'csv',
    'datetime',
    'Image',
  ],
  version = '0.3.1',
  description = 'Diary to create notebooks and store intermediate results and figures',
  author = 'Miquel Perello Nieto',
  author_email = 'perello.nieto@gmail.com',
  url = 'https://github.com/perellonieto/DiaryPy',
  download_url = 'https://github.com/perellonieto/DiaryPy/archive/0.3.tar.gz',
  keywords = ['diary', 'notebook', 'logging', 'figures', 'experiments'],
  classifiers = [],
)