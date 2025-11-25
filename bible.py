import requests
import click
import json

from pathlib import Path

bible_path = 'kjv.json'


def load_bible():
    with open(bible_path, "r", encoding="utf-8") as f:
        return json.load(f)


bible_reader = load_bible()


@click.command()
def cbible():
    click.echo("------------------------------------------------------------------------------------------------")
    name = input("\nWhat is your name?\n")
    click.echo(f"\nHello {name} \nWELCOME TO C-BIBLE\n"
               f"\nYou can use the 'find' command to find a scripture following this format\n"
               f"'python bible.py find job,3:16'\n"
               f"'python bible.py find job,3:16-20'\n"
               f"\nOr the request command to input your bible request\n"
               f"'python bible.py request\n"
               f"\nThe Lord bless you as you go through His word.!!!\n")
    click.echo("------------------------------------------------------------------------------------------------")


@click.group()
def bible():
    pass


@click.command()
def request():
    rst = []
    m_rst = []
    bk = click.prompt("What book are you searching for?", type=str).strip().capitalize()
    chp = click.prompt("What chapter are you searching for?", type=str).strip()
    vs = click.prompt("What verse are you searching for?", type=str).strip()

    if "-" in vs:
        vs_l = vs.split('-')
        vs_1st = vs_l[0]
        vs_2nd = vs_l[1]

        a = int(vs_1st)
        b = int(vs_2nd) + 1

        for n in range(a, b, +1):
            for x in bible_reader:
                if x["book"] == bk and x["chapter"] == chp and x["verse"] == str(n):
                    m_rst.append(
                        f"{x['book']} {x['chapter']}:{x['verse']}\n"
                        f"  → {x['text']}"
                    )
        if not m_rst:
                click.secho("Verse not found. Check spelling and try again.", fg="red")
        else:
            click.secho("\nResult:\n", fg="green")
            for r in m_rst:
                click.echo(r)
    else:
        for x in bible_reader:
            if x["book"] == bk and x["chapter"] == chp and x["verse"] == vs:
                rst.append(
                    f"{x['book']} {x['chapter']}:{x['verse']}\n"
                    f"→ {x['text']}\n"
                )
        if not rst:
                click.secho("Verse not found. Check spelling and try again.", fg="red")
        else:
            click.secho("\nResult:\n", fg="green")
            click.echo(rst[0])


@click.command()
@click.argument('text')
def find(text):
    rst = []
    m_rst = []

    new_text = text.strip().split(',')
    bk = new_text[0].strip().capitalize()
    new_ch_text = new_text[1].strip().split(':')
    chp = new_ch_text[0].strip()
    vs = new_ch_text[1].strip()

    if "-" in vs:
        vs_l = vs.split('-')
        vs_1st = vs_l[0]
        vs_2nd = vs_l[1]

        a = int(vs_1st)
        b = int(vs_2nd) + 1

        for n in range(a, b, +1):
            for x in bible_reader:
                if x["book"] == bk and x["chapter"] == chp and x["verse"] == str(n):
                    m_rst.append(
                        f"{x['book']} {x['chapter']}:{x['verse']}\n"
                        f"  → {x['text']}"
                    )
        if not m_rst:
                click.secho("Verse not found. Check spelling and try again.", fg="red")
        else:
            click.secho("\nResult:\n", fg="green")
            for r in m_rst:
                click.echo(r)
    else:
        for x in bible_reader:
            if x["book"] == bk and x["chapter"] == chp and x["verse"] == vs:
                rst.append(
                    f"{x['book']} {x['chapter']}:{x['verse']}\n"
                    f"→ {x['text']}\n"
                )
        if not rst:
                click.secho("Verse not found. Check spelling and try again.", fg="red")
        else:
            click.secho("\nResult:\n", fg="green")
            click.echo(rst[0])


bible.add_command(cbible)
bible.add_command(request)
bible.add_command(find)

if __name__ == '__main__':
    bible()
