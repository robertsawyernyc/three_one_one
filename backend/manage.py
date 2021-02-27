import sys
from flask.cli import FlaskGroup
from api.src import create_app
from api.src.adapters.run_adapters import RequestAndBuild
import click

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('build_incidents')
@click.argument('begin_date')
@click.argument('end_date')
@click.argument('limit')
def build_incidents(begin_date, end_date, limit):
    runner = RequestAndBuild()
    runner.run(begin_date, end_date, limit)
    print(begin_date, end_date, limit)


if __name__ == "__main__":
    cli()

# this file requires 3 arguements to run:
# python3 manage.py build_incidents '2019-03-24' '2019-03-24' 2