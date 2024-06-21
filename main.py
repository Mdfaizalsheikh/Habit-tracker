import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def add_habit(name):
  try:
    data=pd.read_csv('habit.csv') 
  except FileNotFoundError:
    data=pd.DataFrame(columns=['name', 'date']) 

  new_habit=pd.DataFrame({'Name':[name], 'date':[None]}) 

  data = pd.concat([data,new_habit],ignore_index=True)
  data.to_csv('data.csv',index=False)

def mark_habit_done(name, date):
  try:
    data = pd.read_csv('habit.csv')
  except FileNotFoundError:
    print('No habit found')
    return

  if name not in data['name'].values:
    print(f'habit {name} not found')
    return

  data.loc[data['name'] == name, 'date']=date
  date.to_csv('habit.csv',index=False)
  print(f'Habit {name} marked as done on {date}')

def view_habits():
  try:
    data=pd.read_csv('habit.csv')
    print(data)
  except FileNotFoundError:
    print('No habit Found')
 
def gen_summary():
  try:
    data=pd.read_csv('habit.csv') 
  except FileNotFoundError:
    print ('No habit found')
    return
    
  data['date'] = pd.to_datetime(data['date'])
  summary = data.groupby('name')['date'].count()
  print (summary)
  
  summary.plot(kind='bar')
  plt.title('Habit tracking summary') 
  plt.xlabel('habits') 
  plt.ylabel('days completed')
  plt.show()

def main():
  print('\n Habit Tracker')
  print('1. Add a new habit')
  print('2. Mark a habit as Done')
  print('3. view all habits')
  print('4. Generate summary')
  print('5. Exit')

  choice = input('Enter your choice (1-5) : ')
  if choice == '1':
    name =input('Enter name of habit') 
    add_habit(name)
    print(f'Habit {name} added')
  elif choice=='2':
    
    name=input("Enter habit name") 
    date=input('Enter date (YYYY-MM-DD): ')
    mark_habit_done(name,date)

  elif choice=='3':
    view_habits()
  elif choice=='4':
    gen_summary() 
  elif choice=='5':
    print ('Goodbye! ')
    break 
    
  else:
    print('Invalid choice choose between (1-5)')

if __name__ == '__main__ ' :  
  main()
  




