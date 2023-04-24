import os

skills = {
    "Python": 1,
    "Ruby": 2,
    "Bash": 4,
    "Git": 8,
    "HTML": 16,
    "TDD": 32,
    "CSS": 64,
    "JavaScript": 128
}

def print_ui(skill_inputs_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---------------------------------------------")
    print("follow the steps bellow")
    print("1. Input a skill you have from the list")
    print("2. Hit enter to input another skill ")
    print("3. Enter submit to calculate your skill score")
    print("+---------------------+")
    print("| Python | Ruby       |")
    print("| Bash   | Git        |")
    print("| HTML   | TDD        |")
    print("| CSS    | JavaScript |")
    print("+---------------------+")
    if skill_inputs_list:
        print(f"The skills you have added are: {skill_inputs_list}")
    print("---------------------------------------------")
    return

def calculate_skill():
    skill_inputs = None
    skill_inputs_list = []
    skill_score = 0
    
    while True:
        
        print_ui(skill_inputs_list)
        skill_inputs = input("ENTER HERE: ")
        skill_inputs= skill_inputs.strip()
        
        if skill_inputs == "submit":
            break 
            

        
        elif skill_inputs not in skills or skill_inputs in skill_inputs_list:
            print("--INPUT INVALID--")
            print("check spelling")
            print("or")
            print("skill already input")
            input("Press enter to try again: ")
            continue
        else:
            skill_inputs_list.append(skill_inputs)
            skill_score += skills[skill_inputs]
    
    print(f"Your skill score is: {skill_score}")
    print(f"skills you may want to learn and points they will add to your score are as follows")
    for skill in skills:
        if skill not in skill_inputs_list:
            print(f"{skill} : {skills[skill]} points")          


calculate_skill()