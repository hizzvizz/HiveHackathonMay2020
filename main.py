# Name: Ruben Alexander
# Url: https://peakd.com/@rubenalexander
# Hackathon Submission Post Url: https://peakd.com/
# Date/Time: 5/13/2020 2:05 PM EST

from beem.discussions import Query, Trending_tags
import random

def tagmenu(tm):
  for x in range(0,len(tm),1):
    print(str(x+1) + ": " + tm[x])

def answermenu(am):
  alpha='a'
  for x in range(0,4,1):
    print("[" + str(chr(ord(alpha)+x)) + "]: " + str(am[x]))

def close_answer(am,correct_a,user_a):
  diff_ans=[]
  for v in am:
    if v-correct_a != 0:
      diff_ans.append(v-correct_a)
  if abs(min(diff_ans))==abs(correct_a-user_a):
    return True
  else: 
    return False


categories = ['comments','top_posts','total_payouts']
q_list = ['How many comments are in tag ', 'How many top posts are in tag ', 'What is the total payout (in HBD) for tag ']

q = Query(limit=20, start_tag="")
taglist = []
chosen_tags = []
chosen = 0 
question_index=0
question_max=5
q_correct=0
q_missed=0
q_percent=0
meta_list=[]
score=0
answers=[]

# Collect top tags
for h in Trending_tags(q):
  #print(h)
  taglist.append(h['name'])
  meta_list.append([h['name'],h['comments'],h['top_posts'],h['total_payouts']])

"""
#For debugging the metalist
print("metalist: ")
print(meta_list)
"""

# User selects 10 tags from top tags
print()
print("TAG SELECTION ROUND")
while chosen < question_max:
  tagmenu(taglist)
  print("Choose " + str(question_max-chosen) + " tag(s)")
  x=int(input())
  if x<0 or x>len(taglist):
    print("Please choose a tag from the tag list.")
  else:
    chosen_tags.append(taglist[x-1])
    print("You added: " + str(taglist[x-1]))
    taglist.remove(taglist[x-1])
    chosen+=1

print()
print('Your tags selection is complete.')
print('Here are your chosen tags: ')

# User answers questions from their top tags, random categories
print()
print("QUESTION ROUND")
while question_index < question_max:
  # tagmenu(chosen_tags)
  x=random.randint(0,len(chosen_tags)-1)
  print()
  print("Current Tag: " + str(chosen_tags[x]))
  y=random.randint(0,2)
  print("Current Category: " + str(categories[y]))
  print()
  print(q_list[y] + str(chosen_tags[x] + "?"))
  print()
  
  # Append correct answers to answer option list
  for n in meta_list:
    if n[0] == chosen_tags[x]:
      for i in range(0,4,1):
        if y == 2:
          temp = n[y+1].split(".")
          answers.append(int(temp[0]))
        else:
          answers.append(n[y+1])

  # Tweak three answers, preserve one
  protect = random.randint(0,3)
  for m in range(0,4,1):
    if m != protect:
      tweak_value = random.randint(0,int(answers[0]/10))
      coin = random.randint(0,1)
      if coin==0:
        answers[m]+=tweak_value
      else:
        answers[m]-=tweak_value
      answers[m]=abs(answers[m])
      
  answermenu(answers)
  print("Enter your answer (a, b, c, or d): ")
  z=input()
  if z=='a':
    z=0
  elif z=='b':
    z=1
  elif z=='c':
    z=2
  elif z=='d':
    z=3
  else: 
    z=-1

  if z==protect:
    print("CORRECT! +10 points")
    score+=10
  elif close_answer(answers,answers[protect],answers[z]) is True:
    print("So close! +5 points")
    score+=5
  else:
    print("+0 points")

  chosen_tags.remove(chosen_tags[x])
  question_index+=1
  answers=[]
  if question_max-question_index==0:
    print("Thanks for playing. Player score total is... " + str(score) + " points!")
  else:
    print(str(question_max-question_index) + " question(s) left.")
  