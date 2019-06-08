import random
import pprint
from terminaltables import AsciiTable

player_list = [ 
    { "player_number": 75, "player_name": "Shakib Al Hasan (vc)", "dob": "24 March 1987 (aged 32)", "ODIs": 198, "player_type": "All-rounder", "handed": "Left", "bowler_type": "Left-arm orthodox", "club": "Abahani Limited" }, 
    { "player_number": 28, "player_name": "Tamim Iqbal", "dob": "20 March 1989 (aged 30)", "ODIs": 193, "player_type": "Batsman", "handed": "Left", "bowler_type": "Right-arm off spin", "club": "Mohammedan Sporting" }, 
    { "player_number": 16, "player_name": "Liton Das", "dob": "13 October 1994 (aged 24)", "ODIs": 28, "player_type": "Wicket-keeper-batsman", "handed": "Right", "bowler_type": "-", "club": "Mohammedan Sporting" },
    { "player_number": 15, "player_name": "Mushfiqur Rahim (wk)", "dob": "9 May 1987 (aged 32)", "ODIs": 205, "player_type": "Wicket-keeper-batsman", "handed": "Right", "bowler_type": "Right-arm medium", "club": "Legends of Rupganj" }, 
    { "player_number": 30, "player_name": "Mahmudullah", "dob": "4 February 1986 (aged 33)", "ODIs": 175, "player_type": "Batsman", "handed": "Right", "bowler_type": "Right arm off spin", "club": "Abahani Limited" }, 
    { "player_number": 8, "player_name": "Mohammad Mithun", "dob": "13 February 1990 (aged 29)", "ODIs": 18, "player_type": "Wicket-keeper-batsman", "handed": "Right", "bowler_type": "-", "club": "Abahani Limited" }, 
    { "player_number": 1, "player_name": "Sabbir Rahman", "dob": "22 November 1991 (aged 27)", "ODIs": 61, "player_type": "Batsman", "handed": "Right", "bowler_type": "Right arm leg spin", "club": "Abahani Limited" }, 
    { "player_number": 53, "player_name": "Mehedi Hasan Miraz", "dob": "25 October 1996 (aged 22)", "ODIs": 28, "player_type": "All-rounder", "handed": "Right", "bowler_type": "Right-arm off spin", "club": "Abahani Limited" }, 
    { "player_number": 59, "player_name": "Soumya Sarkar", "dob": "25 February 1993 (aged 26)", "ODIs": 44, "player_type": "All-rounder", "handed": "Left", "bowler_type": "Right-arm medium", "club": "Abahani Limited" }, 
    { "player_number": 34, "player_name": "Rubel Hossain", "dob": "1 January 1990 (aged 29)", "ODIs": 97, "player_type": "Bowler", "handed": "Right", "bowler_type": "Right-arm medium-fast", "club": "Abahani Limited" }, 
    { "player_number": 74, "player_name": "Mohammad Saifuddin", "dob": "1 September 1996 (aged 22)", "ODIs": 13, "player_type": "All-rounder", "handed": "Left", "bowler_type": "Right-arm medium-fast", "club": "Abahani Limited" }, 
    { "player_number": 32, "player_name": "Mosaddek Hossain", "dob": "10 December 1995 (aged 23)", "ODIs": 26, "player_type": "All-rounder", "handed": "Right", "bowler_type": "Right-arm off spin", "club": "Abahani Limited" }, 
    { "player_number": 90, "player_name": "Mustafizur Rahman", "dob": "6 September 1995 (aged 23)", "ODIs": 46, "player_type": "Bowler", "handed": "Left", "bowler_type": "Left-arm fast-medium", "club": "Shinepukur" }, 
    { "player_number": 17, "player_name": "Abu Jayed", "dob": "2 August 1993 (aged 25)", "ODIs": 2, "player_type": "Bowler", "handed": "Right", "bowler_type": "Right-arm fast-medium", "club": "Prime Doleshwar" }
]

print('Full player list: ')
print(player_list)
print('Bangladesh has total ' + str(len(player_list)) + ' players')

random.shuffle(player_list)
ODI_players = player_list[:11]
print('ODI has the following players: ')
pprint.pprint(ODI_players)
print('ODI has ' + str(len(ODI_players))) + ' Players' 

table = [
    list(ODI_players[0].keys())
]
for player in ODI_players:
    table.append(player.values())

table = AsciiTable(table)
print(table.table)
