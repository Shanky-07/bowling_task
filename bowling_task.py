def calc_bowling_score():
  score = 0
  for i in range(1,11):
    shots = 2
    shot_count = 1
    pins_down = 0
    while shots > 0:
      a = int(input('number pins knocked down in {} shot of {} frame = '.format(shot_count, i)))
      pins_down += a
      if pins_down == 10 and shot_count == 1:
        pins_down == 0
        shots += 1
        shot_count+=1
        score+=10
      elif pins_down == 10 and shot_count == 2:
        pins_down = 0
        shot_count+=1
        shots+=1
        score+=a
      else:
        score+=a
        shot_count+=1
      shots-=1
  return "Your Score is {} Points".format(score)



a = calc_bowling_score()
print(a)
