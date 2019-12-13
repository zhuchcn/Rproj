# Create Rproj file from command line

## Installation

```
$ pip install git+git://github.com/zhuchcn/Rproj.git
```

## Usage

Create a .Rproj file in current directory.

```
$ rproj my_project
```

Create a R package skeleton.

```
$ rproj --project-type package my_package
```

Create a Shiny App skeleton.

```
$ rproj --project-type shiny-app my_app
```