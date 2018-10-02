import requests
import json
import arrow

API_KEY = 'GB8bkrf49HTDWvn6lQ2MERZ1qFA5oJUC';


def main():
	year = str(2018)

	season_type = determine_season_type()

	week = determine_NFL_week(season_type)

	ScheduleAPI = 'https://profootballapi.com/schedule?' + 'api_key=' + API_KEY + '&year=' + year + '&week=' + week + '&season_type=REG' 

	GameAPI = 'https://profootballapi.com/game?' + 'api_key=' + API_KEY + '&game_id=2018093009'

	print(ScheduleAPI)
	print(GameAPI)

	response1 = requests.post(ScheduleAPI)


	schedule = response1.json()

	response2 = requests.post(GameAPI)

	print(response2.status_code)

	game = response2.json()

	print(game)

	completed_games = []
	live_upcoming_games = []
	for entry in schedule:
		data = {'GameID = ': entry['id'], 'Home_team =': location_to_name(entry['home']), 'Home_score': entry['home_score'], 'Away_team =': location_to_name(entry['away']), 'Away_score': entry['away_score']}
		if entry['final'] == 1:
			completed_games.append(data)
		else:
			data.update({'Time =': ((arrow.get(entry['time'])).to('US/Eastern')).format('HH:MM MM-DD-YYYY')})
			live_upcoming_games.append(data)

	print("Completed Games: ")
	print(completed_games)
	print("Live/Upcoming Games: ")
	print(live_upcoming_games)

def determine_season_type():
	now = arrow.now('US/Eastern')
	start_reg = arrow.get(2018, 9, 2)
	start_post = arrow.get(2018, 12, 31)
	if(now < start_reg):
		season_type = 'PRE'
	elif(now < start_post):
		season_type = 'REG'
	else:
		season_type = 'POST'
	return season_type

def determine_NFL_week(season_type):
	now = arrow.now('US/Eastern')
	week = -1;
	if season_type == 'PRE':
		print("PRESEASON")
	elif season_type == 'REG':
		if (arrow.get(2018, 9, 4) <= now and now < arrow.get(2018, 9, 11)):
			week = 1
		elif (arrow.get(2018, 9, 11) <= now and now < arrow.get(2018, 9, 18)):
			week = 2
		elif (arrow.get(2018, 9, 18) <= now and now < arrow.get(2018, 9, 25)):
			week = 3
		elif (arrow.get(2018, 9, 25) <= now and now < arrow.get(2018, 10, 2)):
			week = 4
		elif (arrow.get(2018, 10, 2) <= now and now < arrow.get(2018, 10, 9)):
			week = 5
		elif (arrow.get(2018, 10, 9) <= now and now < arrow.get(2018, 9, 16)):
			week = 6
		elif (arrow.get(2018, 10, 16) <= now and now < arrow.get(2018, 10, 23)):
			week = 7
		elif (arrow.get(2018, 10, 23) <= now and now < arrow.get(2018, 10, 30)):
			week = 8
		elif (arrow.get(2018, 10, 30) <= now and now < arrow.get(2018, 11, 6)):
			week = 9
		elif (arrow.get(2018, 11, 6) <= now and now < arrow.get(2018, 11, 13)):
			week = 10
		elif (arrow.get(2018, 11, 13) <= now and now < arrow.get(2018, 11, 20)):
			week = 11
		elif (arrow.get(2018, 11, 20) <= now and now < arrow.get(2018, 11, 27)):
			week = 12
		elif (arrow.get(2018, 11, 27) <= now and now < arrow.get(2018, 12, 4)):
			week = 13
		elif (arrow.get(2018, 12, 4) <= now and now < arrow.get(2018, 12, 11)):
			week = 14
		elif (arrow.get(2018, 12, 11) <= now and now < arrow.get(2018, 12, 18)):
			week = 15
		elif (arrow.get(2018, 12, 18) <= now and now < arrow.get(2018, 12, 25)):
			week = 16
		elif (arrow.get(2018, 12, 25) <= now and now < arrow.get(2018, 12, 31)):
			week = 17
	else:
		print("POST SEASON")
	return str(week)

def location_to_name(loc):
	names = {'LA': 'Rams', 'MIN' : 'Vikings', 'JAX': 'Jaguars', 'NYJ': "Jets", 'NE': 'Patriots', 'MIA': 'Dolphins',
	          'TEN': 'Titans', 'PHI': 'Eagles', 'ATL': 'Falcons', 'CIN': 'Bengals', 'CHI': 'Bears', 'TB': 'Bucs',
	          'DAL': 'Cowboys', 'DET': 'Lions', 'GB': 'Packers', 'BUF': 'Bills', 'IND': 'Colts', 'HOU': 'Texans',
	          'ARI': 'Cardnials', 'SEA': 'Seattle', 'CLE' : 'Browns', 'OAK': 'Raiders', 'LAC': 'Chargers', 'SF':
	          '49ers', 'NYG': 'Giants', 'NO': 'Saints', 'PIT': 'Steelers', 'BAL': 'Ravens', 'DEN': 'Broncos', 
	          'KC': 'Chiefs', 'WAS': 'Redskins', 'CAR': 'Panthers'}
	return names[loc]



if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()