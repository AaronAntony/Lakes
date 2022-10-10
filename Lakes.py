from matplotlib import pyplot as plt

file= open("orglakes.txt", "r")

Superior= []
Michigan=[]
Huron=[]
Erie=[]
Ontario=[]
St_Clair=[]

def initialize():
  #skips the first  10 Lines as they are for reader only
  for i in range(1,11):
    file.readline()
  return

def processline(line):
  #Sorts the data into individual lists for each Lake
  Superior.append(float(line[11:16]))
  Michigan.append(float(line[19:24]))
  Huron.append(float(line[27:32]))
  Erie.append(float(line[35:40]))
  Ontario.append(float(line[43:48]))
  St_Clair.append(float(line[51:56]))
  return

def statsForLake(lake):
  Maximum=max(lake)
  Minimum=min(lake)
  
  total=0

  for day in range(0,365):
    total=total+lake[day]
  Average=total/365

  total=0
  for day in range(0,80):
    total=total+lake[day]
  for day in range(355,365):
    total=total+lake[day]
  Winter_Average=total/90

  total=0
  for day in range(172,266):
    total=total+lake[day]
  Summer_Average=total/365
  return [Minimum,round(Winter_Average,2),round(Average,2), round(Summer_Average,2),Maximum]

def frequency(lake):
  data={}
  for day in range(0,365):
    count=0
    for temp in lake:
      if(temp==lake[day]):
        count= count+1
    data.update({lake[day] : count})
  plt.figure(2)
  plt.stem(data.keys(),data.values())
  plt.show()

def main():
  initialize()
  for day in range(0,365):
    line=file.readline()
    processline(line)
  file.close()

  days=range(1,366)
  #Plot each Lakes temperature
  plt.figure()
  plt.plot(days,Superior, label='Lake Superior')
  plt.plot(days,Michigan, label='Lake Michigan')
  plt.plot(days,Huron, label='Lake Huron')
  plt.plot(days,Erie, label='Lake Erie')
  plt.plot(days,Ontario, label='Lake Ontario')
  plt.plot(days,St_Clair, label='Lake St.Clair')
  plt.title('Temperature of Each Lake Every Day in 2019')
  plt.xlabel('Days')
  plt.ylabel('Temperature (C)')
  plt.legend()
  plt.grid(True)
  plt.show()

  stats=statsForLake(Superior)
  print('\nFor Lake Superior:','\n\tMinimum: ',stats[0],'\n\tWinter Average:',stats[1],'\n\tAverage: ',stats[2],'\n\tSummer Average:',stats[3],'\n\tMaximum: ',stats[4])

  stats=statsForLake(Michigan)
  print('\nFor Lake Michigan:','\n\tMinimum: ',stats[0],'\n\tWinter Average:',stats[1],'\n\tAverage: ',stats[2],'\n\tSummer Average:',stats[3],'\n\tMaximum: ',stats[4])

  stats=statsForLake(Huron)
  print('\nFor Lake Huron:','\n\tMinimum: ',stats[0],'\n\tWinter Average:',stats[1],'\n\tAverage: ',stats[2],'\n\tSummer Average:',stats[3],'\n\tMaximum: ',stats[4])

  stats=statsForLake(Erie)
  print('\nFor Lake Erie:','\n\tMinimum: ',stats[0],'\n\tWinter Average:',stats[1],'\n\tAverage: ',stats[2],'\n\tSummer Average:',stats[3],'\n\tMaximum: ',stats[4])

  stats=statsForLake(Ontario)
  print('\nFor Lake Ontario:','\n\tMinimum: ',stats[0],'\n\tWinter Average:',stats[1],'\n\tAverage: ',stats[2],'\n\tSummer Average:',stats[3],'\n\tMaximum: ',stats[4])

  stats=statsForLake(St_Clair)
  print('\nFor Lake St_Clair:','\n\tMinimum: ',stats[0],'\n\tWinter Average:',stats[1],'\n\tAverage: ',stats[2],'\n\tSummer Average:',stats[3],'\n\tMaximum: ',stats[4])
  return  
main()