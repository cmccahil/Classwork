class Node:

   def __init__(self,data,prevNode=None):
       self.data = data
       self.prevNode = prevNode
       self.childNodes = []
       self.depth=0
       self.heuristic=0

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getPrevNode(self):
       return self.prevNode

   def setPrevNode(self,val):
       self.prevNode = val
       
   def setChildNodes(self,nodes):
      self.childNodes = nodes
         
   def getChildNodes(self):
      return self.childNodes
   
   def setDepth(self,newDepth):
      self.depth=newDepth
      
   def getDepth(self):
      return self.depth

   def setHeuristic(self,val):
      self.heuristic = val

   def getHeuristic(self):
      return self.heuristic
       
##class LinkedList:
##
##   def __init__(self,head = None):
##       self.head = head
##       self.size = 0
##
##   def getSize(self):
##       return self.size
##
##   def addNode(self,data):
##       newNode = Node(data,self.head)
##       self.head = newNode
##       self.size+=1
##       return True
##       
##   def printNode(self):
##       curr = self.head
##       while curr:
##           print(curr.data)
##           curr = curr.getPrevNode()

def checkLength(number):
   node=str(number)
   if len(node)==1:
      node="00"+node
      return node
   elif len(node)==2:
      node="0"+node
      return node
   else:
      return node
   
def add(node,value):
    if value == 100:
        if str(node)[0] == '9':
            return "-1"
        else:
            number = int(node)+100
            node=checkLength(number)
            return node
    elif value == 10:
        if str(node)[1] == '9':
            return "-1"
        else:
            number = int(node)+10
            node=checkLength(number)
            return node
         
    elif value == 1:
        if str(node)[2] == '9':
            return "-1"
        else:
            number = int(node)+1
            node=checkLength(number)
            return node
    else:
        return "-1"

def subtract(node,value):
    if value == 100:
        if node[0] == '0':
            return "-1"
        else:
            number = int(node)-100
            node=checkLength(number)
            return node
         
    elif value == 10:
        if node[1] == '0':
            return "-1"
        else:
            number = int(node)-10
            node=checkLength(number)
            return node
    elif value == 1:
        if node[2] == '0':
            return "-1"
        else:
            number = int(node)-1
            node=checkLength(number)
            return node
    else:
        return "-1"
    
def expand(node,previousNode):
    if node[0] != previousNode[0]:  
        return [subtract(node,10), add(node,10), subtract(node,1), add(node,1)]
    elif node[1] != previousNode[1]:
        return [subtract(node,100), add(node,100), subtract(node,1), add(node,1)]
    elif node[2] != previousNode[2]:
        return [subtract(node,100), add(node,100), subtract(node,10), add(node,10)]
    else:
        return[subtract(node,100), add(node,100), subtract(node,10), add(node,10), subtract(node,1), add(node,1)]

##def hillAlgorithmExpand(node,previousNode,direction)
##   if direction=="up":
##      if node[0] != previousNode[0]:  
##         return [add(node,10), add(node,1)]
##      elif node[1] != previousNode[1]:
##         return [add(node,100), add(node,1)]
##      elif node[2] != previousNode[2]:
##         return [add(node,100), add(node,10)]
##      else:
##         return[add(node,100), add(node,10), add(node,1)]
##   elif direction=="down":
##      if node[0] != previousNode[0]:  
##        return [subtract(node,10), subtract(node,1)]
##    elif node[1] != previousNode[1]:
##        return [subtract(node,100), subtract(node,1)]
##    elif node[2] != previousNode[2]:
##        return [subtract(node,100), subtract(node,10)]
##    else:
##        return[subtract(node,100), subtract(node,10), subtract(node,1)]

def printSolution(numbers):
   current=numbers[len(numbers)-1]
   path=[]
   while current.getPrevNode() != None:
  #    print("Iteration: "+str(current.getData()))
      path.insert(0,current.getData())
      current=current.getPrevNode()
   path.insert(0,current.getData())
   output=""
   for i in path:
      output=output+str(i)+", "
   output=output[0:len(output)-2]
   print(output)
   output=""
   for i in numbers:
      output=output+str(i.getData())+", "
   output=output[0:len(output)-2]
   print(output)

def breadthFirstSearch(start,end,forbidden):
   expandedNodes = []
   fringe=[]
   previousNode = None
   count=0
   startnode=Node(start)
   fringe.append(startnode)
   while(len(expandedNodes)<1000):
      if len(fringe)>0: #this block of code checks to see if the node we are about to expand is valid
         repeatNode=False
         foundNode=False
         while(foundNode==False):
            if(len(fringe)==0):
               print("No solution found.")
               return
            new=fringe.pop(0)
            if new.getData() == end: #indicates reaching the goal node
               expandedNodes.append(new)
               printSolution(expandedNodes)
               return
            if new.getPrevNode() == None:
               firstGenNodes=expand(new.getData(),new.getData())
            else:
               firstGenNodes=expand(new.getData(),new.getPrevNode().getData())
            secondGenNodes=[]
            for i in firstGenNodes:
               if (i in forbidden) or (i == "-1"):
                  continue
               else:
                  secondGenNodes.append(Node(i,new))
            new.setChildNodes(secondGenNodes)
            for k in expandedNodes:                            #this checks if there are any repeats?
               if k.getData() == new.getData():
                  currentList=new.getChildNodes()
                  establishedList=k.getChildNodes()
                  if len(currentList)==len(establishedList):
                     for m in range(len(currentList)):
                        if currentList[m].getData() != establishedList[m].getData():
                           break
                        elif m==len(currentList)-1:
                           repeatNode=True
            if repeatNode==True:
               repeatNode=False
               continue
            else:
               foundNode=True
      for node in new.getChildNodes():
         fringe.append(node)
      count+=1
      expandedNodes.append(new)
   print("No solution found.")

def depthFirstSearch(start,end,forbidden):
   expandedNodes = []
   fringe=[]
   previousNode = None
   count=0
   startnode=Node(start)
   fringe.append(startnode)
   while(len(expandedNodes)<1000):
      if len(fringe)>0: #this block of code checks to see if the node we are about to expand is valid
         repeatNode=False
         foundNode=False
         while(foundNode==False):
            if(len(fringe)==0):
               print("No solution found.")
               return
            new=fringe.pop(0)
            if new.getData() == end: #indicates reaching the goal node
               expandedNodes.append(new)
               printSolution(expandedNodes)
               return
            if new.getPrevNode() == None:
               firstGenNodes=expand(new.getData(),new.getData())
            else:
               firstGenNodes=expand(new.getData(),new.getPrevNode().getData())
            secondGenNodes=[]
            for i in firstGenNodes:
               if (i in forbidden) or (i == "-1"):
                  continue
               else:
                  secondGenNodes.append(Node(i,new))
            new.setChildNodes(secondGenNodes)
            for k in expandedNodes:
               if k.getData() == new.getData():
                  currentList=new.getChildNodes()
                  establishedList=k.getChildNodes()
                  if len(currentList)==len(establishedList):
                     for m in range(len(currentList)):
                        if currentList[m].getData() != establishedList[m].getData():
                           break
                        elif m==len(currentList)-1:
                           repeatNode=True
            if repeatNode==True:
               repeatNode=False
               continue
            else:
               foundNode=True
      for node in reversed(new.getChildNodes()):
         fringe.insert(0,node)
      count+=1
      expandedNodes.append(new)
   print("No solution found.")
   output=""
   for i in expandedNodes:
      output=output+str(i.getData())+", "
   output=output[0:len(output)-2]
   print(output)

def IDS(start,end,forbidden):
   expandedNodes = []
   allExpandedNodes= []
   fringe=[]
   previousNode = None
   count=0
   startnode=Node(start)
   startnode.setDepth=0
   fringe.append(startnode)
   cutoffLimit=0
   while(len(allExpandedNodes)+len(expandedNodes)<1000):
      if len(fringe)>0: #this block of code checks to see if the node we are about to expand is valid
         repeatNode=False
         foundNode=False
         while(foundNode==False):
            if(len(fringe)==0):
               #print("Fringe empty! Node is: " + new.getData())
               #print(fringe)
               cutoffLimit+=1
               startnode=Node(start)
               startnode.setDepth=0
               fringe.append(startnode)
               allExpandedNodes=allExpandedNodes+expandedNodes
               #allExpandedNodes=allExpandedNodes[:-1]
               expandedNodes=[]
               count+=1
               repeatNode=False
               foundNode=False
               
               #print(fringe[0].getData())
               continue
            new=fringe.pop(0)
            if new.getData() == end: #indicates reaching the goal node
               expandedNodes.append(new)
               for i in expandedNodes:
                  allExpandedNodes.append(i)
               printSolution(allExpandedNodes)
               return
            if new.getPrevNode() == None:
               firstGenNodes=expand(new.getData(),new.getData())
            else:
               firstGenNodes=expand(new.getData(),new.getPrevNode().getData())
            secondGenNodes=[]
            for p in firstGenNodes:
               secondGenNodes.append(Node(p,new))
            thirdGenNodes=[]
            for i in secondGenNodes:
               if (i.getData() in forbidden) or (i.getData() == "-1"):
                  continue
               else:
                  thirdGenNodes.append(i)
            new.setChildNodes(thirdGenNodes)
            for k in expandedNodes:
               if k.getData() == new.getData():
                  currentList=new.getChildNodes()
                  establishedList=k.getChildNodes()
                  if len(currentList)==len(establishedList):
                     for m in range(len(currentList)):
                        if currentList[m].getData() != establishedList[m].getData():
                           break
                        elif m==len(currentList)-1:
                           repeatNode=True
            if repeatNode==True:
               repeatNode=False
               continue
            else:
               #print("new node")
               foundNode=True
      else:
         cutoffLimit+=1
         startnode=Node(start)
         startnode.setDepth=0
         fringe.append(startnode)
         allExpandedNodes=allExpandedNodes+expandedNodes
         expandedNodes=[]
         count+=1
         continue
      for node in reversed(new.getChildNodes()):
         node.setDepth(node.getPrevNode().getDepth()+1)
         if(node.getDepth() <= cutoffLimit):
            fringe.insert(0,node)
      count+=1
      expandedNodes.append(new)
   print("No solution found.")
   output=""
   expandedNodes.append(new)
   for i in expandedNodes:
      allExpandedNodes.append(i)
   for i in allExpandedNodes[:-1]:
      output=output+str(i.getData())+", "
   output=output[0:len(output)-2]
   print(output)

def greedy(start,end,forbidden):
   expandedNodes = []
   fringe=[]
   previousNode = None
   startnode=Node(start)
   fringe.append(startnode)
   while(len(expandedNodes)<1000):
      if len(fringe)>0: #this block of code checks to see if the node we are about to expand is valid
         repeatNode=False
         foundNode=False
         while(foundNode==False):
            if(len(fringe)==0):
               print("No solution found.")
               return
            smallestHeuristic=999
            smallestNodeIndex=0
            count=0
            for i in fringe:
               if i.getHeuristic()<=smallestHeuristic:
                  smallestNodeIndex=count
                  smallestHeuristic=i.getHeuristic()
               count+=1
            new=fringe.pop(smallestNodeIndex)
            #print(new.getData(),new.getHeuristic())
            if new.getData() == end: #indicates reaching the goal node
               expandedNodes.append(new)
               printSolution(expandedNodes)
               return
            if new.getPrevNode() == None:
               firstGenNodes=expand(new.getData(),new.getData())
            else:
               firstGenNodes=expand(new.getData(),new.getPrevNode().getData())
            secondGenNodes=[]
            for i in firstGenNodes:
               if (i in forbidden) or (i == "-1"):
                  continue
               else:
                  secondGenNodes.append(Node(i,new))
            heuristic=0
            for j in secondGenNodes:
               newNumber=j.getData()
               heuristic = abs(int(newNumber[0])-int(end[0])) + abs(int(newNumber[1])-int(end[1])) + abs(int(newNumber[2])-int(end[2]))
               j.setHeuristic(heuristic)
            new.setChildNodes(secondGenNodes)
            for k in expandedNodes:
               if k.getData() == new.getData():
                  currentList=new.getChildNodes()
                  establishedList=k.getChildNodes()
                  if len(currentList)==len(establishedList):
                     for m in range(len(currentList)):
                        if currentList[m].getData() != establishedList[m].getData():
                           break
                        elif m==len(currentList)-1:
                           repeatNode=True
            if repeatNode==True:
               repeatNode=False
               continue
            else:
               foundNode=True
      for node in new.getChildNodes():
         fringe.append(node)
      expandedNodes.append(new)
   print("No solution found.")
   output=""
   for i in expandedNodes:
      output=output+str(i.getData())+", "
   output=output[0:len(output)-2]
   print(output)
   
def aStar(start,end,forbidden):
   expandedNodes = []
   fringe=[]
   previousNode = None
   startnode=Node(start)
   fringe.append(startnode)
   while(len(expandedNodes)<1000):
      if len(fringe)>0: #this block of code checks to see if the node we are about to expand is valid
         repeatNode=False
         foundNode=False
         while(foundNode==False):
            if(len(fringe)==0):
               print("No solution found.")
               return
            smallestHeuristic=999
            smallestNodeIndex=0
            count=0
            for i in fringe:
               if i.getHeuristic()<=smallestHeuristic:
                  smallestNodeIndex=count
                  smallestHeuristic=i.getHeuristic()
               count+=1
            new=fringe.pop(smallestNodeIndex)
            #print(new.getData(),new.getHeuristic())
            if new.getData() == end: #indicates reaching the goal node
               expandedNodes.append(new)
               printSolution(expandedNodes)
               return
            if new.getPrevNode() == None:
               firstGenNodes=expand(new.getData(),new.getData())
            else:
               firstGenNodes=expand(new.getData(),new.getPrevNode().getData())
            secondGenNodes=[]
            for i in firstGenNodes:
               if (i in forbidden) or (i == "-1"):
                  continue
               else:
                  secondGenNodes.append(Node(i,new))
            heuristic=0
            for j in secondGenNodes:
               newNumber=j.getData()
               j.setDepth(new.getDepth()+1)
               heuristic = abs(int(newNumber[0])-int(end[0])) + abs(int(newNumber[1])-int(end[1])) + abs(int(newNumber[2])-int(end[2]))+j.getDepth()
               j.setHeuristic(heuristic)
            new.setChildNodes(secondGenNodes)
            for k in expandedNodes:
               if k.getData() == new.getData():
                  currentList=new.getChildNodes()
                  establishedList=k.getChildNodes()
                  if len(currentList)==len(establishedList):
                     for m in range(len(currentList)):
                        if currentList[m].getData() != establishedList[m].getData():
                           break
                        elif m==len(currentList)-1:
                           repeatNode=True
            if repeatNode==True:
               repeatNode=False
               continue
            else:
               foundNode=True
      for node in new.getChildNodes():
         fringe.append(node)
      expandedNodes.append(new)
   print("No solution found.")
   output=""
   for i in expandedNodes:
      output=output+str(i.getData())+", "
   output=output[0:len(output)-2]
   print(output)
   
def hill(start,end,forbidden):
   expandedNodes = []
   fringe=[]
   previousNode = None
   startnode=Node(start)
   fringe.append(startnode)
##   direction=""
##   if start < end:
##      direction="up"
##   else:
##      direction="down"
   bestHeuristic=999
   while(len(expandedNodes)<1000):
      if len(fringe)>0: #this block of code checks to see if the node we are about to expand is valid
         repeatNode=False
         foundNode=False
         while(foundNode==False):
            if(len(fringe)==0):
               print("No solution found.")
               output=""
               for i in expandedNodes:
                  output=output+str(i.getData())+", "
               output=output[0:len(output)-2]
               print(output)
               return
            smallestNodeIndex=0
            count=0
            for i in fringe:
               if i.getHeuristic()<=bestHeuristic:
                  smallestNodeIndex=count
                  smallestHeuristic=i.getHeuristic()
               count+=1
            new=fringe.pop(smallestNodeIndex)
            fringe=[]
            #print(new.getData(),new.getHeuristic())
            if new.getData() == end: #indicates reaching the goal node
               expandedNodes.append(new)
               printSolution(expandedNodes)
               return
            
            if new.getPrevNode() == None:
               firstGenNodes=expand(new.getData(),new.getData())
            else:
               firstGenNodes=expand(new.getData(),new.getPrevNode().getData())
            secondGenNodes=[]
            for i in firstGenNodes:
               if (i in forbidden) or (i == "-1"):
                  continue
               else:
                  secondGenNodes.append(Node(i,new))
            heuristic=0
            for j in secondGenNodes:
               newNumber=j.getData()
               heuristic = abs(int(newNumber[0])-int(end[0])) + abs(int(newNumber[1])-int(end[1])) + abs(int(newNumber[2])-int(end[2]))
               j.setHeuristic(heuristic)
            new.setChildNodes(secondGenNodes)
            for k in expandedNodes:
               if k.getData() == new.getData():
                  currentList=new.getChildNodes()
                  establishedList=k.getChildNodes()
                  if len(currentList)==len(establishedList):
                     for m in range(len(currentList)):
                        if currentList[m].getData() != establishedList[m].getData():
                           break
                        elif m==len(currentList)-1:
                           repeatNode=True
            if repeatNode==True:
               repeatNode=False
               continue
            else:
               foundNode=True
      newBestHeuristic=999
      for node in new.getChildNodes():
         if node.getHeuristic()< bestHeuristic:
            fringe.append(node)
            if node.getHeuristic() < newBestHeuristic:
               newBestHeuristic = node.getHeuristic()
#      print("Fringe after first iteration:")
      if len(fringe)==0:
         expandedNodes.append(new)
         break
    #  for h in fringe:
   #      print(h.getData())
      bestHeuristic=newBestHeuristic
      newFringe=[]
   
      for node in fringe:
         if node.getHeuristic() > bestHeuristic:
            continue
         else:
            newFringe.append(node)
      if len(fringe)==0:
         expandedNodes.append(new)
         break
      #print("fringe after second iteration")
      #for k in newFringe:
       #  print(k.getData(),k.getHeuristic())
      fringe=newFringe
      if len(fringe)==0:
         expandedNodes.append(new)
         break
      expandedNodes.append(new)
   print("No solution found.")
   output=""
   for i in expandedNodes:
      output=output+str(i.getData())+", "
   output=output[0:len(output)-2]
   print(output)
   
#MAIN    
import sys
algorithm=sys.argv[1]
file=open(sys.argv[2])
counter=0
forbiddenBoolean=False
for line in file:
    if counter==0:
        start=line.strip()
    elif counter==1:
        end=line.strip()
    else:
        forbidden=(line.strip().split(","))
        forbiddenBoolean=True
    counter+=1
if forbiddenBoolean==False:
   forbidden=[]

if algorithm == 'B':
   breadthFirstSearch(start,end,forbidden)
elif algorithm == 'D':
   depthFirstSearch(start,end,forbidden)
elif algorithm == 'I':
   IDS(start,end,forbidden)
elif algorithm == 'G':
   greedy(start,end,forbidden)
elif algorithm == 'A':
   aStar(start,end,forbidden)
elif algorithm == 'H':
   hill(start,end,forbidden)
