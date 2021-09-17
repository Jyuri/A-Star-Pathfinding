

def visualizeNoise(noiseArray,x,y):
  for yi in range(0,y):
    newLine=''
    for xi in range(0,x):
      tempVal = noiseArray[xi][yi][0]
      if tempVal > 1.00:
        #Black 40
        newLine += '\u001b[40mX'
      elif 1.00 >= tempVal > 0.75:
        #Red 41
        newLine += '\u001b[41mX'
      elif 0.75 >= tempVal > 0.50:
        #Magenta 45
        newLine += '\u001b[45mX'
        continue
      elif 0.50 >= tempVal > 0.25:
        #Blue 44
        newLine += '\u001b[44mX'
        continue
      elif 0.25 >= tempVal:
        #Cyan 46
        newLine += '\u001b[46mX'
        continue
      else:
        newLine += '\u001b[41mO'
        pass
      pass
    newLine += '\u001b[0m'
    print(newLine)
    pass
  pass

def mapCollapse(tempArray):
  x = len(tempArray)
  y = len(tempArray[0])
  
  for yi in range(0,y):
    for xi in range(0,x):
      if tempArray[xi][yi] > 0.5:
        tempArray[xi][yi] = [1, 0, [0, 0]]
        continue
      elif tempArray[xi][yi] <= 0.5:
        tempArray[xi][yi] = [0, 0, [0, 0]]
        continue
      pass
    pass
  return tempArray

def mapCleaner(tempArray):
  x = len(tempArray)
  y = len(tempArray[0])
  
  for yi in range(0, y):
    for xi in range(0, x):
      #Creates Border
      if xi == 0 or yi == 0 or xi == int(x - 1) or yi == int(y - 1):
        tempArray[xi][yi][0] = 1
      # Modifies Internal Map
      else:
        solidCount = 0
        for subxi in range(-1, 2):
          for subyi in range(-1, 2):
            if tempArray[int(xi + subxi)][int(yi + subyi)][0] == 1:
              if subxi == 0 and subyi == 0:
                continue
              else:
                solidCount += 1
            if int(solidCount) < 5:
              tempArray[xi][yi][0] = 0
            elif int(solidCount) >= 5:
              tempArray[xi][yi][0] = 1
            else:
              print('Error')
              pass
            pass
          pass
        pass
      pass
    pass
  return tempArray