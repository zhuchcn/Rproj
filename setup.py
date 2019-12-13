from setuptools import setup, find_packages

setup(
    name="rproj",
    version='0.1',
    py_modules=['rproj.rproj'],
    install_requires=[
        'click',
        'jinja2'
    ],
    entry_points='''
        [console_scripts]
        rproj=rproj.rproj:rproj
    ''',
    packages=["rproj"],
    package_data={'rproj': ['templates/*']},
    include_package_data=True
)