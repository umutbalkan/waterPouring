
##  CS 461 - Artificial Intelligence - HOMEWORK 1
##  @author: Sencer Umut Balkan
##  @info:  state space search on water pouring puzzle

def pour_problem(X,Y,goal,start=(0,0)):
    """ X and Y are capacity of jugs; (x,y) is current water levels
    and represents a state. The goal is a level that can be in either glass.
    Start at  initial state and follow successors until we reach goal.
    Keep track of frontier and previously explored; fail when  to frontier."""
    Fail = []
    # initial state = goal
    if goal in start:
        return [start]
    explored = set() # set of states we have visited.
    explored.add(start) # initial state saved
    frontier = [ [start] ] # ordered list of paths we have walked
    #i = 0;
    #j = 0;
    while frontier:
        path = frontier.pop(0) # frontier is a FIFO (queue).
        (x,y) = path[-1]
        #print(i * " ", end='')
        print("\nstate: ",(x,y), "\nchild:")
        #if len(frontier) <= j:
        #i += 4
        for (state, action) in successors(x,y, X, Y).items():
            if state not in explored: # Check repeated states
                explored.add(state) # add state to set of states
                #j += 1
                #print(i * " ", end='')
                print("     |--> " + action + " --> ", state)

                path2 =  path  + [action, state]
                if goal in state:
                    Fail = path2
                    #print(path2)
                else:
                        frontier.append(path2)
                        #print()
    return Fail




def successors(x,y,X,Y):
    """Return a dict of {state:action} pairs describing what can be reached
    from the (x,y) state, and how."""
    assert x <= X and y <= Y ## (x,y) is jug levels; X and Y are jug sizes
    return {
            ## Operators & Their conditions
            ( (0,y+x) if y+x <= Y else (x - (Y-y),y + (Y-y)) ):'pour from X to Y',
            ( (x+y,0) if y+x <= X else (x + (X-x),y - (X-x)) ):'pour from Y to X ',
            (X,y):'fill X',
            (x,Y):'fill Y',
            ( (0,y) if x > 0 else (x,y) ):'empty X',
            ( (x,0) if y > 0 else (x,y) ):'empty Y'
            }


print ("Now running.")
print("All possible states and possible actions:")
goal_path = pour_problem(10,6,8,(0,0))
print()
print("Solution path:")
for x in goal_path:
    print(x, "-> ", end='')

print("Goal\n")
