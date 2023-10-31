import numpy as np

class Node:

   left=None
   right=None
   key:int = 0 
   def __init__(self,key:int,value:int):
      self.value=value
      self.key=key
      left=None
      right=None

   def constructor(self,key,value):
      self.value=value
      self.key=key

def insert(node:Node, key:int, value:int):
   if(key<node.key):
      if(node.left == None):
         node.left = Node(key,value)
      else :
         insert(node.left,key,value)
   elif(key>=node.key):
      if(node.right==None):
         node.right = Node(key,value)
      else: 
         insert(node.right,key,value)

def search(node,key):
   if( node==None):
      return None
   if (node.left == None):
      return node
   if (key<node.key): 
      search(node.left, key) 
   return search(node.right, key)

def getMin(node:Node):
   if(node == None):
      return None
   if(node.left == None):
      return node
   return getMin(node.left)

def getMax(node:Node):
   if(node == None):
      return None
   if(node.right== None):
      return node
   return getMax(node.right)

def delete(node:Node,key:int):
   """
      delete node - key
   """
   if(node == None):
      return None
   elif(key<node.key):
      node.left = delete(node.left,key)
   elif(key>node.key):
      node.right = delete(node.right,key)
   else:
      if(node.left == None or node.right == None):
         if (node.left == None):
            node =node.right
         else:
            node = node.left
      else:
         maxInLeft = Node()
         maxInLeft = getMax(node.left)
         node.key = maxInLeft.key
         node.value = maxInLeft.value
         node.right = delete(node.right, maxInLeft.key)
   
   return node


def printTree(node:Node):
   if(node == None):
      return
   printTree(node.left)
   print(node.value)
   printTree(node.right)

def deleteTree(node:Node):
   if(node == None):
      return
   deleteTree(node.left)
   deleteTree(node.right)
   print(node.value)

def copyTree(node:Node):
   if(node == None):
      return
   copyTree(node.left)
   copyTree(node.right)
   print(node.value)

def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = Node(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode

def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def main():
   lst = [5,4,8,11,None,13,4,7,2,None,None,None,1]
   node:Node = Node(0,lst[0])
   for i in range(1,len(lst)):
      insert(node,i,lst[i])
   #print(node.value)
   #pre_order(node)
   pre_order(node)
   #root = creatBTree(lst, 0)
   #pre_order(root)
   #print()
   #root = search(root,4)
   #pre_order(root)
   #print()
   #root=delete(node,6)
   #pre_order(root)
   return 



if __name__ =="__main__":
   main()