# Модуль №7. Работа с файлами и форматированный вывод. "Форматирование строк".

team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451


# Использование %:
def team_numbers(name, numbers):
    print('"В команде %s участников %d !"' % (name, numbers))

team_numbers(team1_name, team1_num)
team_numbers(team2_name, team2_num)

print('"Итого сегодня в командах участников: %d и %d !"' % (team1_num, team2_num))


# Использование format():
def number_of_tasks(name, score):
    print('Команда {0:s} решила задач: {1:d} !'.format(name, score))

def team_time(name, time):
    print('{0:s} решили задачи за {1:6.1f} c !'.format(name, time))

number_of_tasks(team1_name, score1)
number_of_tasks(team2_name, score2)
team_time(team1_name, team1_time)
team_time(team2_name, team2_time)


# Использование f-строк:
print(f'"Команды решили {score1} и {score2} задач."')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team1_name}'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team2_name}'
else:
    challenge_result = 'Ничья'

print(f'"Результат битвы: {challenge_result}!"')

tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:4.1f} секунды на задачу!"')
