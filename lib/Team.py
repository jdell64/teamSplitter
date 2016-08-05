import operator

import TeamMember


class Team:
    def __init__(self, members=None):
        if members is None:
            self.members = []
        else:
            self.members = members

    def append(self, member):
        self.members.append(member)

    def remove(self, member):
        self.members.remove(member)

    def sort(self):
        return Team(sorted(self.members, key=operator.attrgetter('rating'), reverse=True))

    def get_bkillers(self):
        ret_members = Team()
        for member in self.members:
            if member.bkiller:
                ret_members.append(member)
        return ret_members

    def get_team_average(self):
        return self.get_team_total() / (len(self.members))

    def get_team_total(self):
        sum = 0
        for member in self.members:
            sum += member.rating
        return sum

    def split(self, numberOfTeams):

        # create copy of the team
        t = self.sort()
        # create a list of teams
        new_teams = []
        for i in xrange(numberOfTeams):
            new_teams.append(Team())
        going_up = True
        do_double = False
        # print new_teams

        # first do the boss killers
        current_run = 0
        b_killers = t.get_bkillers().members
        # print "GETTING BKILLERS"
        for member in b_killers:
            # print "Member: %s" % member.to_string()
            t.remove(member)
            current_team = current_run % numberOfTeams
            # print "is going to team %s\n" % current_team
            new_teams[current_team].append(member)

            if current_team == 0 and not going_up:
                # if 0 is reached and I'm going down, start going up
                going_up = True
                do_double = True

            elif current_team == (numberOfTeams - 1) and going_up:
                # if the highest mod is reached and still going up, go down
                going_up = False
                do_double = True

            if going_up:
                if do_double:
                    do_double = False
                else:
                    current_run += 1
            else:
                if do_double:
                    do_double = False
                else:
                    current_run -= 1

        # do everyone else

        non_bkillers = t.members
        for member in non_bkillers:
            current_team = current_run % numberOfTeams
            # print "is going to team %s\n" % current_team
            new_teams[current_team].append(member)

            if current_team == 0 and not going_up:
                # if 0 is reached and I'm going down, start going up
                going_up = True
                do_double = True

            elif current_team == (numberOfTeams - 1) and going_up:
                # if the highest mod is reached and still going up, go down
                going_up = False
                do_double = True

            if going_up:
                if do_double:
                    do_double = False
                else:
                    current_run += 1
            else:
                if do_double:
                    do_double = False
                else:
                    current_run -= 1

        return new_teams

    def to_string(self):
        ret_string = ""
        for member in self.members:
            ret_string += member.to_string() + "\n"
        return ret_string

    def size(self):
        return len(self.members)