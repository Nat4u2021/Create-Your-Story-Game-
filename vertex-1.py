#Name : Nathaniel Mensah
#Date : November 10, 2020
#Purpose: Defining the vertex class


#defining the vertex class, which takes name and the data as parameters
class Vertex:
    def __init__(self, name, data):
        self.name = name       #instance variable which stores the name of vertex
        self.data = data       #instance variable which stores the data
        self.adj = []          #instance variable which stores the list of other vertices connected to this particular vertex