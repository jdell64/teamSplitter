import random
import string
from pprint import pprint

from lib.Team import Team
from lib.TeamMember import TeamMember

my_team = Team()

for i in xrange(30):
    un = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randrange(5, 10))) + \
         ''.join(random.choice(string.digits) for _ in range(random.randrange(4)))
    rate = random.randrange(30000, 120000)
    bk = random.choice([True, False, False, False, False])
    tm = TeamMember(un, rate, bk)
    my_team.append(tm)

print my_team.to_string()

# print my_team.get_bkillers().to_string()
# print my_team.get_bkillers().sort().to_string()

war_groups = my_team.split(3)
# print war_groups

for idx, team in enumerate(war_groups):
    print "Team %s:" % idx
    # print team.to_string()
    print "Total: %s" % team.get_team_total()
    print "Average: %s" % team.get_team_average()
    print "Players who can kill bosses: %s" % len(team.get_bkillers().members)
    print "Total in team: %s" % team.size()
    print "\n"

print my_team.size()
