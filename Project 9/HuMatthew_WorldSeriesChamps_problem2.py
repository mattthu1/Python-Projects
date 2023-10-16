import urllib.request

def download_data(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8').splitlines()
        return data
    except:
        print("Sorry, that is not valid.")
        return None

url = input("Enter a URL: ")
data = download_data(url)

if data:
    print(data[:10])


#2b 

def clean_data(data):
    # Remove empty entries
    cleaned_data = [entry for entry in data if entry]

    # Get unique list of teams
    unique_teams = list(set(cleaned_data))

    # Count number of times each team has won
    team_counts = [cleaned_data.count(team) for team in unique_teams]

    return unique_teams, team_counts

#2c

def download_data(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8').split('\n')
        data = [d.strip() for d in data if d.strip()]
        return data
    except:
        print("Sorry, that is not valid.")
        return None

def get_world_series_stats(url):
    data = download_data(url)
    if not data:
        return

    # Get unique list of teams and number of wins
    team_wins = {}
    for d in data:
        if d in team_wins:
            team_wins[d] += 1
        else:
            team_wins[d] = 1
    unique_teams = list(team_wins.keys())
    unique_teams.sort()
    num_unique_teams = len(unique_teams)

    # Get total number of years
    num_years = len(data)

    # Get team with most wins
    most_wins_team = max(team_wins, key=team_wins.get)
    most_wins = team_wins[most_wins_team]

    # Get teams with only one win
    one_win_teams = [team for team, wins in team_wins.items() if wins == 1]

    # Get average number of wins for teams with at least one win
    num_teams_with_wins = len([wins for wins in team_wins.values() if wins > 0])
    total_wins = sum([wins for wins in team_wins.values() if wins > 0])
    avg_wins = total_wins / num_teams_with_wins

    # Print out statistics
    print(f"{num_unique_teams} teams have won the World Series at least once.")
    print(f"The data contains {num_years} years worth of World Series.")
    print(f"{most_wins_team} has won the most World Series, with a total of {most_wins} wins.")
    print(f"{', '.join(one_win_teams)} have only won one World Series each.")
    print(f"Among the teams who have won at least one World Series, the average number of wins was {avg_wins:.2f}.")

url = input("Enter a URL: ")
get_world_series_stats(url)
