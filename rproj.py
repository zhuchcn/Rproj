import os
from jinja2 import Environment, FileSystemLoader
import click


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False
)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def use_template(template_filename,
                 dest_dirname,
                 dest_filename=None,
                 context={}):
    if dest_filename is None:
        dest_filename = template_filename
    fname = os.path.join(dest_dirname, dest_filename)
    with open(fname, 'w') as f:
        template_data = render_template(template_filename, context)
        f.write(template_data)

def create_project_dir(projname):
    try:
        os.mkdir(projname)
    except FileExistsError:
        print(f"Directory {projname} already exists")

def create_package(projname):
    create_project_dir(projname)
    
    context = {
        "project_type": "package",
        "projname": projname
    }
    use_template('template.Rproj', projname, projname + '.Rproj', context)
    use_template('.Rbuildignore', projname)
    use_template('DESCRIPTION', projname, context = context)
    use_template('NAMESPACE', projname)
    use_template('.gitignore', projname)
    
    os.mkdir(os.path.join(projname, 'R'))
    os.mkdir(os.path.join(projname, 'man'))
    use_template('hello.R', os.path.join(projname, 'R'))
    use_template('hello.Rd', os.path.join(projname, 'man'))

def create_shinyapp(projname):
    create_project_dir(projname)

    context = {
        "project_type": "package",
        "projname": projname
    }
    use_template('template.Rproj', projname, projname + '.Rproj', context)
    use_template('app.R', projname, context = context)


@click.command()
@click.option('--project-type', default="default",
              type=click.Choice(["default", "package", "shiny-app"]),
              help="The project type. Can be either default or package")
@click.argument('projname')
def rproj(project_type, projname):
    '''
    Create a Rproj from command line.

    The --project-type by default will generate a .Rproj file at the current
    working directory. When --project-type is set to "package", a new folder
    will be created.
    '''
    rproj_fname = projname + '.Rproj'

    if project_type == "default":
        context = { "project_type": project_type }
        use_template('template.Rproj', os.getcwd(), rproj_fname, context)
    elif project_type == "package":
        create_package(projname)
    elif project_type == "shiny-app":
        create_shinyapp(projname)


if __name__ == "__main__":
    rproj()