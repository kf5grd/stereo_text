#!/usr/bin/env python3
from stereo_text import stereo_panel, stereo_sirt
import click
import sys

@click.group()
def cli():
    """
    Generate autostereograms with text.

    Be sure to read over the readme to get a good
    idea of what input is expected.
    """
    pass

@cli.command()
@click.option('--hpad', '-p', default=1, help='Horizontal padding')
@click.option('--vpad', '-P', default=1, help='Vertical padding')
@click.option('--dbl', '-d', is_flag=True, help='Double space words')
@click.argument('input', type=click.File('r'))
def panel(hpad, vpad, dbl, input):
    """
    Generates 2 panels, each with a slightly different
    variation of the same text that, when looked at with
    parallel vision, shows specified words in 3D.
    """
    text = input.read()
    panel = stereo_panel(text, hpad, vpad, dbl)
    click.echo(panel)

@cli.command()
@click.option('--pattern-length', '-l', default=15, help='Pattern length',
              type=click.IntRange(5,34, clamp=True))
@click.argument('input', type=click.File('r'))
def sirt(input, pattern_length):
    """
    Generates a single block of seemingly random text that, when
    looked at with parallel vision, shows a 3D image based
    on the provided depth map.
    
    SIRT = Single Image Random Text
    """
    sirt = stereo_sirt(input.read(), pattern_length)
    click.echo(sirt)

if __name__ == '__main__':
    cli()
