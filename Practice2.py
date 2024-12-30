
student_name=input('What is name: ')
age=int(input('what age are you: '))
grade=int(input('what grade are you: '))
class1=input('what class are you in: ')
subject_mark=float(input('what mark did you get on your subject: '))

print(f'sudent name is: {student_name} his age is:{age} his grade is: {grade} he is in: {class1} he got: {subject_mark} ')

#test match details
match_title="Australia vs India test match"
team1="Australia"
team2="india"
match_info="Australia: 450/9d in 150 overs | india 320 & 250 in 120 overs "
best_player="steve smith"
venue="Melbourne cricket ground"
print(f'Match title { match_title}')

# extracting scores 
aus_score1=match_info[:17]
india_score=match_info[33:48]
print(aus_score1)
print(india_score)
#concatenation
final_result= aus_score1+india_score
print(final_result)

print(match_info.find('250'))

first_player_name=best_player.split()[0]
last_player_name=best_player.split()[1]
print(first_player_name)
print(last_player_name)

#displaying first/last character using slice
print(f"first 10 characters of match {match_info[:10]}")
print(f"last 10 characters of match {match_info[-10:]}")
print(f"lets reverse the whole text {match_info[:: -1]}")

updated_best_player=best_player.replace("Smi,Smith")
print(updated_best_player)