from .api import NBAStatsAPI


class NBAObject():
    nba_api = NBAStatsAPI()


class Scoreboard(NBAObject):
    endpoint = 'scoreboard'

    def __init__(self, date, day_offset, league_id):
        params = {
            'gameDate': date,
            'DayOffset': day_offset,
            'LeagueID': league_id
        }

        self.result = self.nba_api.request(self.endpoint, params)

        self.results = self.parse_results()

    def parse_results(self):
        results = {}

        result_sets = self.result['resultSets']
        for result in result_sets:
            results[result['name']] = []

            for row in result['rowSet']:
                game = {}

                for key, value in enumerate(row):
                    game[result['headers'][key].lower()] = value

                results[result['name']].append(game)

        return results

    @property
    def game_header(self):
        return self.results['GameHeader']

    @property
    def line_score(self):
        return self.results['LineScore']

    @property
    def series_standing(self):
        return self.results['SeriesStandings']

    @property
    def last_meeting(self):
        return self.results['LastMeeting']

    @property
    def east_conf_standing_by_day(self):
        return self.results['EastConfStandingsByDay']

    @property
    def west_conf_standing_by_day(self):
        return self.results['WestConfStandingsByDay']

    @property
    def available(self):
        return self.results['Available']

    @property
    def team_leaders(self):
        return self.results['TeamLeaders']

    @property
    def tickets_links(self):
        return self.results['TicketsLinks']

    @property
    def win_probability(self):
        return self.results['WinProbability']

    @property
    def home_team_id(self):
        return self.game_header['home_team_id']

    @property
    def visitor_team_id(self):
        return self.game_header['visitor_team_id']

    @property
    def teams_scores(self):
        teams = {}
        for line in self.line_score:
            teams[line['team_id']] = {
                'name': line['team_abbreviation'],
                'pts': line['pts']
            }

        return teams

    @property
    def team_score(self, team_id):
        return self.teams_scores[team_id]

    @property
    def final_scores(self):
        scores = []
        for game in self.game_header:
            visitor_team = self.teams_scores[game['visitor_team_id']]
            home_team = self.teams_scores[game['home_team_id']]

            scores.append('%s @ %s: %s - %s' % (visitor_team['name'],
                                                home_team['name'],
                                                visitor_team['pts'],
                                                home_team['pts']))
        return scores
