import click


@click.group()
def cli():
    """OrbitML Command Line Interface."""
    pass


@cli.command()
def info():
    """Show basic project info."""
    click.echo("OrbitML: Modular ML Orchestration Toolkit")


if __name__ == "__main__":
    cli()
