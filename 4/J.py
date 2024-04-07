import re


class FootballStats:
    def __init__(self):
        self.team_goals = {}
        self.team_games = {}
        self.player_goals = {}
        self.player_goals_by_minute = {}
        self.player_games = {}  # Количество игр, в которых участвовал игрок
        self.player_teams = {}  # Команды игроков
        self.score_opens_team = {}
        self.score_opens_player = {}

    def process_match(self, match_info, goals_info):
        team1, team2, score1, score2 = match_info
        # Обработка голов команд
        self.team_goals[team1] = self.team_goals.get(team1, 0) + score1
        self.team_goals[team2] = self.team_goals.get(team2, 0) + score2
        self.team_games[team1] = self.team_games.get(team1, 0) + 1
        self.team_games[team2] = self.team_games.get(team2, 0) + 1

        # Фиксация участия игроков в матче
        for player in self.player_teams.get(team1, []) + self.player_teams.get(team2, []):
            self.player_games[player] = self.player_games.get(player, 0) + 1

        if goals_info:
            first_goal_info = sorted(goals_info, key=lambda x: x[1])[0]
            # зачислить к первой команде
            if first_goal_info[0] in [g[0] for g in goals_info[:score1]]:
                self.score_opens_team[team1] = self.score_opens_team.get(team1, 0) + 1
                self.score_opens_player[first_goal_info[0]] = self.score_opens_player.get(first_goal_info[0], 0) + 1
            # зачислить ко 2 команде
            else:
                self.score_opens_team[team2] = self.score_opens_team.get(team2, 0) + 1
                self.score_opens_player[first_goal_info[0]] = self.score_opens_player.get(first_goal_info[0], 0) + 1


            last_minut_gole = goals_info[0][1]


        flag_second_comand = False
        for player, minute in goals_info:
            # Регистрация голов игрока
            if last_minut_gole < minute:
                flag_second_comand = True
            self.player_goals[player] = self.player_goals.get(player, 0) + 1
            if player not in self.player_goals_by_minute:
                self.player_goals_by_minute[player] = {}
            self.player_goals_by_minute[player][minute] = self.player_goals_by_minute[player].get(minute, 0) + 1
            # Добавление игрока в команду, если это новый игрок
            if player not in self.player_teams.get(team1, []) and not flag_second_comand:
                self.player_teams[team1] = self.player_teams.get(team1, []) + [player]
            if player not in self.player_teams.get(team2, []) and flag_second_comand:
                self.player_teams[team2] = self.player_teams.get(team2, []) + [player]
            self.player_games[player] = self.player_games.get(player, 0) + 1

    def query(self, query):
        if query.startswith("Total goals for"):
            team = query[len("Total goals for "):].strip('"')
            return self.team_goals.get(team, 0)
        elif query.startswith("Mean goals per game for"):
            team = query[len("Mean goals per game for "):].strip('"')
            return round(self.team_goals[team] / self.team_games[team], 3)
        elif query.startswith("Total goals by"):
            player = query[len("Total goals by "):].strip('"')
            return self.player_goals.get(player, 0)
        elif query.startswith("Mean goals per game by"):
            player = query[len("Mean goals per game by "):].strip('"')
            return round(self.player_goals.get(player, 0) / self.player_games[player],
                         3) if player in self.player_games else 0
        elif query.startswith("Score opens by"):
            entity = query[len("Score opens by "):].strip('"')

            if entity in self.score_opens_team:
                return self.score_opens_team.get(entity, 0)
            elif entity in self.score_opens_player:
                return self.score_opens_player.get(entity, 0)
            else:
                return 0

# Создаем экземпляр класса для обработки статистики
stats = FootballStats()
queries = []
flag_new_match = False

with open('input.txt', 'r') as file:
    lines = file.readlines()

for get in lines:
    get = get.rstrip()

    if ':' in get:
        flag_new_match = True
        pattern = r'"(.*?)" - "(.*?)" (\d+):(\d+)'
        match = re.match(pattern, get)

        match = (match.group(1),
                 match.group(2),
                 int(match.group(3)),
                 int(match.group(4))
                 )

        process = []
    elif flag_new_match:
        # Если это перечисление голов
        if "'" in get:
            spli_get = get.split(' ')
            process.append((' '.join(spli_get[:-1]), int(spli_get[-1][:-1])))


        # конец перечисления, начало запросов
        else:
            flag_new_match = False
            stats.process_match(match , process)
            print(stats.query(get))
    else:
        print(stats.query(get))


