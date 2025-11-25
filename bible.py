import requests
import click
import json

from pathlib import Path

bible_path = 'bible-master/KJV_bible.json'


def load_version(version):
    version_bible_path = f'bible-master/{version}_bible.json'
    with open(version_bible_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_bible():
    with open(bible_path, "r", encoding="utf-8") as f:
        return json.load(f)


bible_reader = load_bible()

rst = []

@click.command()
def cbible():
    click.echo("------------------------------------------------------------------------------------------------")
    name = input("\nWhat is your name?\n")
    click.echo(f"\nHello {name} \nWELCOME TO C-BIBLE\n"
               f"\nYou can use the 'read' command to find a scripture following this format\n"
               f"'python bible.py read job 3 16'\n"
               f"\nOr the request command to input your bible request\n"
               f"'python bible.py request\n"
               f"\nThe Lord bless you as you go through His word.!!!\n")
    click.echo("------------------------------------------------------------------------------------------------")


@click.group()
def bible():
    pass


@click.command()
def request():
    bk = click.prompt("What book are you searching for?", type=str).strip().capitalize()
    chp = click.prompt("What chapter are you searching for?", type=str).strip()
    vs = click.prompt("What verse are you searching for?", type=str).strip()

    if vs:
        if "-" in vs:
            vs_l = vs.split('-')
            vs_1st = vs_l[0]
            vs_2nd = vs_l[1]

            a = int(vs_1st)
            b = int(vs_2nd) + 1

            for n in range(a, b, +1):
                for x in bible_reader:
                    if x["book"] == bk and x["chapter"] == chp and x["verse"] == str(n):
                        rst.append(
                            f"{x['book']} {x['chapter']}:{x['verse']}\n"
                            f"  → {x['text']}"
                        )
            if not rst:
                click.secho("Verse not found. Check spelling and try again.", fg="red")
            else:
                click.secho("\nResult:\n", fg="green")
                for r in rst:
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

    else:
        for x in bible_reader:
            if x["book"] == bk and x["chapter"] == chp:
                rst.append(
                    f"{x['book']} {x['chapter']}:{x['verse']}\n"
                    f"→ {x['text']}\n"
                )
        click.secho("\nResult:\n", fg="green")
        for text in rst:
            click.echo(text)


@click.command()
@click.option('-v', '--version', help="Find specific bible version")
@click.argument('u_bk', )
@click.argument('u_chp',)
@click.argument('u_vs', required=False)
def find(u_bk, u_chp, u_vs, version):

    version_reader = load_version(version) if version else bible_reader

    bk = u_bk.strip().capitalize()
    chp = u_chp.strip()
    vs = u_vs.strip() if u_vs else None

    if vs:
        if "-" in vs:
            start, end = vs.split('-')
            a = int(start)
            b = int(end) +1

            for n in range(a, b, +1):
                verse = str(n)
                text = version_reader[bk][chp][verse]
                rst.append(
                    f"{bk} {chp}: {verse}\n"
                    f"  → {text}\n"
                )
            if not rst:
                click.secho("Verse not found. Check spelling and try again.", fg="red")
            else:
                click.secho("\nResult:\n", fg="green")
                for r in rst:
                    click.echo(r)
        else:
            rst.append(
                f"{bk} {chp}: {vs}\n"
                f"  → {version_reader[bk][chp][vs]}"
            )
            if not rst:
                click.secho("Verse not found. Check spelling and try again.", fg="red")
            else:
                click.secho("\nResult:\n", fg="green")
                click.echo(rst[0])
    else:
        chapters = version_reader[bk][chp]
        for vrs, txt in chapters.items():
            rst.append(
                f"{bk} {chp}: {vrs}\n"
                f"  → {txt}\n"
            )
        click.secho("\nResult:\n", fg="green")
        for text in rst:
            click.echo(text)


bible.add_command(cbible)
bible.add_command(request)
bible.add_command(find)

if __name__ == '__main__':
    bible()
