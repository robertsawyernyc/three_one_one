import sys
from flask.cli import FlaskGroup
from api.src import create_app
from api.src.adapters.run_adapters import RequestAndBuild
import click

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('build_incidents')
@click.argument('ll')
@click.argument('complaint')
def build_incidents(ll, complaint):
    # example "40.7,-74", "query": "rodent"
    runner = RequestAndBuild()
    runner.run(ll, complaint)
    print(ll, complaint)


if __name__ == "__main__":
    cli()