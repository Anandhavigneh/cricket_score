team_score="India"
Virat=int(input("enter the virat score: "))
Dhoni=int(input("Enter the dhoni score: "))
klrahul=int(input("Enter the Klrahul score: "))
Rohith=int(input("Enter the Rohith score: "))
Jadeja=int(input("Enter the Jadeja score: "))
print(team_score,"score board: ")
print(team_score,"Total score: ",Virat+Dhoni+klrahul+Rohith+Jadeja)
if Virat > Dhoni and Virat>klrahul  and Virat>Jadeja and Virat>Rohith:
    print('Virat is the  man of the match')
elif Dhoni> Virat  and Dhoni>klrahul  and Dhoni>Jadeja and Dhoni>Rohith:
    print("Dhoni is the man of the match")
elif klrahul> Virat  and klrahul>Dhoni  and klrahul>Jadeja and klrahul>Rohith:
    print("klrahul is the man of the match")
elif Rohith> Virat  and Rohith>Dhoni  and Rohith>Jadeja and Rohith>klrahul:
    print("Rohith is the man of the match")
elif Jadeja> Virat  and Jadeja>Dhoni  and Jadeja>klrahul and Jadeja>Rohith:
    print("Jadeja is the man of the match.")

else:
    print('man of the match IS TIE')

