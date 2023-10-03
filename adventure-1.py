#Name: Nathaniel Mensah
#Date: November 10, 2020
#Purpose: Reading from a file, and writing code to create the "Create your adventure game"

from SA9.vertex import Vertex

#defining a function that allows us to create a list out of the lines in the text file
def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text

#defining a function that allows us to read each line from the text file and then pass it as a parameter into the parse_line function
def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)
            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

            # create a graph vertex here and add it to the dictionary

            graph_vertex = Vertex(vertex_name, text)   #creating a graph vertex and storing it as a variable
            graph_vertex.adj = adjacent_vertices       #storing the names of the adjacent vertices as a list in the adj instance variable of the vertex object
            vertex_dict[vertex_name] = graph_vertex    #storing the address of the graph vertex as a vlaue in a dictionary with the vertex name as the key



    file.close()

    return vertex_dict      # return the dictionary of the vertices


#defining the play game function which takes the vertex dictionary as a parameter
def play_game(vertex_dict):
    current_vertex = vertex_dict["START"]  # first store the value, which is a vertex address, of the "START" key as a variable
    print(current_vertex.data)             #print the text of the current vertex, which is stored in the data instance variable, to initiate the game


    while len(current_vertex.adj) != 0:    # while through the linked vertices of the START vertex based on the options chosen, till the adj instance variable of a particular
                                           # vertex is zero, which signifies the end of the adventure story

        choice = (input("Enter your option: ")).lower() #enter your option, in order to choose the direction of adventure. The lower function helps convert every choice to lower case
        index = ord(choice) - ord("a")                  #compute the index, which helps us index the appopriate adj vertex in order to keep the adventure moving in the direction the user chooses

        #set the current vertex to the appropriate vertex object based on the option selected
        if index >= len(current_vertex.adj):  #if print the statement below if the user enters an invalid choice
            print("Invalid choice! Try again.")
        else:
            current_vertex = vertex_dict[current_vertex.adj[index]]

        print(current_vertex.data)  #print the text associated with current vertex


dictionary = load_story("../story_line.txt")
play_game(dictionary)
