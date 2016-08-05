import csv
import os

import click
from lib.Team import Team
from lib.TeamMember import TeamMember

VERSION_NUMBER = '0.1'
APPLICATION_NAME = os.path.basename((os.path.splitext(__file__)[0]))
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
WORK_DIR = os.path.dirname(__file__)
CONFIG_FILE_PATH = './config.cfg'
DATE_FORMAT = '%d-%m-%yT%H:%M:%S'


def docstring_parameter(*par):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*par)
        return obj

    return dec


@click.command(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--teams', default=3, help="Number of teams to make. Default is 3.")
@click.version_option(VERSION_NUMBER)
@docstring_parameter(VERSION_NUMBER, APPLICATION_NAME)
def main(input_file, teams):
    """\b
    \033[1m{1} v{0} \033[0m\n
    This application splits a csv file of team members into three equal teams for AWs and AQs for the Marvel CoC game.

    This application takes one file as input. The file must be a csv in this format (with no header):

    \tplayer,rating,boss killer?

    For example:

    \tjdell64,102034,True
    \tMonkey123,242034,True
    \tsomePlayer2,42034,False

    The first field is the player name. Useful for you to know who it is. The second field is the player's rating. Grab that from the game.
    The last field is whether you feel that player can kill a boss or not. Write True or False for that field.
    """
    # print "Hello World. Input file: %s, Count is: %s" % (input_file, teams)
    reader = csv.reader(file(input_file))
    team = Team()
    for row in reader:
        bkstring = row[2].title()
        bkbool = True if bkstring == "True" else False

        team.append(TeamMember(row[0], int(row[1]), bkbool))

    groups = team.split(teams)

    for idx, team in enumerate(groups):
        print "Team %s:" % idx
        print team.to_string()
        print "Total: %s" % team.get_team_total()
        print "Average: %s" % team.get_team_average()
        print "Players who can kill bosses: %s" % len(team.get_bkillers().members)
        print "\n"

    print "Saving to groups.csv"

    with open('groups.txt', 'wb') as outfile:
        for idx, group in enumerate(groups):
            outfile.write(("TEAM %s" % idx) + os.linesep)
            for member in group.members:
                # print member.to_string()
                outfile.write(member.to_string() + os.linesep)
            outfile.write("-------------" + os.linesep)
            outfile.write("GROUP SUMMARY" + os.linesep)
            outfile.write(("Total rating: %s" % group.get_team_total()) + os.linesep)
            outfile.write(("Member Average: %s" % group.get_team_average()) + os.linesep)
            outfile.write(("Total Bosskillers: %s" % len(group.get_bkillers().members)) + os.linesep)
            outfile.write(os.linesep)


if __name__ == "__main__":
    main()
