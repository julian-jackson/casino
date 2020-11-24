import os, pickle

PATH = os.path.dirname(__file__)
dir_list = []
default_user_data = {
    "name": "placeholder",
    "elo": 300,
    "games_played": 0,
    "wins": 0,
    "avg_rank": 300,
    "high_score": 0,
    "highest_elo": 300,

}

for file in os.listdir(PATH):
    if file.endswith(".cas"):
        current_file = os.path.join(PATH, file)
        file = file[:-4]
        dir_list.append(file)

print("1: New User")
for i, element in  enumerate(dir_list, start=2):
    print(f"{i}: {element}")

user_input = input("\nSelect Account:")

if user_input == "1":
    new_user_id = input("Enter name of new user:")
    default_user_data["name"] = new_user_id
    with open(f'{PATH}/{new_user_id}.cas', 'wb') as f:
        pickle.dump(default_user_data, f)

else:
    for i, element in  enumerate(dir_list, start=2):
        if str(i) == str(user_input):
            current_session_id = element
            current_session_id = PATH+"/"+current_session_id+".cas"

with open(f'user.dat', 'wb') as f:
    pickle.dump(current_session_id, f)
   
import casino