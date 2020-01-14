
from dijkstramanager import DijkstraManager
from heapdijkstra import HeapDijkstra
from fibonacciheapdijkstra import FibonacciHeapDijkstra
import time

print("******WARNING******")
print("\n")
print("***BEFORE USING THIS PROGRAM PLEASE CHECK THE INPUT OF THE PYTHON FILES FOR GRAPH GENERATION***")
versionOfAlgorithm = int(input("Hello! This is a Dijkstra Algorithm Simulator" + "\n" + "Choose between 3 versions" + "\n" + "Type 1 for a classic Dijkstra Algorithm approach (list)"
                           +"\n" + "Type 2 for heap based approach" + "\n" + "Type 3 for Fibonacci Heap approach"))

while versionOfAlgorithm != 1 and versionOfAlgorithm !=2 and versionOfAlgorithm != 3:
    print("Choose a valid approach")
    versionOfAlgorithm = input("Type 1    2    3")

if versionOfAlgorithm == 1:
    dijkstra = DijkstraManager()
    minimumPath = dijkstra.dijkstra()
    print("Minimum Path found is: " + str(minimumPath))

if versionOfAlgorithm == 2:

    dijkstra = HeapDijkstra()
    minimumPath = dijkstra.dijkstraWithHeap()
    print("Minimum Path found is: " + str(minimumPath))


if versionOfAlgorithm == 3:

    dijkstra = FibonacciHeapDijkstra()
    minimumPath = dijkstra.dijkstraWithFibonacciHeap()
    print("Minimum Path found is:" + str(minimumPath))