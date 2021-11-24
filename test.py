from perlin import PerlinNoiseFactory
import PySimpleGUI as sg

def mapCollapseTest(tempArray, cutoffValue=0.5):
  x = len(tempArray)
  y = len(tempArray[0])
  
  for yi in range(0,y):
    for xi in range(0,x):
      if tempArray[xi][yi] > cutoffValue:
        tempArray[xi][yi] = 1
        continue
      elif tempArray[xi][yi] <= cutoffValue:
        tempArray[xi][yi] = 0
        continue
      pass
    pass
  return tempArray


    # Dimentions of the planned map; how many units
widthOfMap = 400
heightOfMap = 400
    # I'm not sure what the resolution does. Needs testing
res = 20
    # Defines how large each point-value is represented on the graph
pixelSize = 2

    # In this portion, a class is defined for noise.
    # By calling it with a set of coordinates, it returns a random value between 0 and 1.
pnf = PerlinNoiseFactory(2, octaves=4)
newArray = []
for x in range(widthOfMap):
    newArray.append([])
    for y in range(heightOfMap):
        n = pnf(x / res, y / res)
        newArray[x].append(n + 0.5)

    # Calls function to "Collapse" values into either 0 or 1
newArray = mapCollapseTest(newArray)

    # Starts and displays a window with a simple graph
myGraph = sg.Graph(
  (widthOfMap*pixelSize,heightOfMap*pixelSize),
  (0,0),
  (widthOfMap*pixelSize,heightOfMap*pixelSize),
  background_color='White', key='graph')
window = sg.Window('Windowzzz', layout=[[myGraph]], margins=(0,0),location=(0,0)).finalize()
graph = window['graph']

    # Graphically shows "newArray" by printing units to the graph class
for yi in range(0,heightOfMap):
    for xi in range(0,widthOfMap):
        if newArray[xi][yi] == 1:
            graph.draw_rectangle(
                (xi*pixelSize,(yi*pixelSize)+pixelSize),
                ((xi*pixelSize)+pixelSize,yi*pixelSize),
                fill_color="Black")
            continue
        pass
    pass

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()