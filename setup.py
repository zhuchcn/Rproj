from setuptools import setup

setup(
    name="rproj",
    version='0.1',
    py_modules=['rproj'],
    install_requires=[
        'click',
        'jinja2'
    ],
    entry_points='''
        [console_scripts]
        rproj=rproj:rproj
    ''',
)