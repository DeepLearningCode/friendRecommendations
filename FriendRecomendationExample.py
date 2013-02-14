import operator
import networkx as nx
G=nx.Graph()
G.add_node('Nurse')
G.add_node('Juliet')
G.add_node('Tybalt')
G.add_node('Capulet')
G.add_node('Friar Laurence')
G.add_node('Romeo')
G.add_node('Benvolio')
G.add_node('Montague')
G.add_node('Mercutio')
G.add_node('Escalus')
G.add_node('Paris')
G.add_edges_from([('Nurse','Juliet')])
G.add_edges_from([('Tybalt','Juliet')])
G.add_edges_from([('Capulet','Juliet')])
G.add_edges_from([('Romeo','Juliet')])
G.add_edges_from([('Romeo','Benvolio')])
G.add_edges_from([('Romeo','Montague')])
G.add_edges_from([('Romeo','Mercutio')])
G.add_edges_from([('Benvolio','Montague')])
G.add_edges_from([('Escalus','Montague')])
G.add_edges_from([('Escalus','Paris')])
G.add_edges_from([('Friar Laurence','Juliet')])
G.add_edges_from([('Friar Laurence','Romeo')])
G.add_edges_from([('Capulet','Tybalt')])
G.add_edges_from([('Capulet','Escalus')])
G.add_edges_from([('Capulet','Paris')])
G.add_edges_from([('Mercutio','Paris')])
G.add_edges_from([('Mercutio','Escalus')])

def friends(graph, user):
    return set(graph.neighbors(user))

def friends_of_friends(graph,user,radius):
    return set(nx.ego_graph(G,user,radius,False).nodes()) - friends(G,user)

def common_friends(graph, user1, user2):
    return friends(graph,user1).intersection(friends(graph,user2))

def number_of_common_friends_map(graph, user):
    friends = friends_of_friends(graph,user,2)
    bigList = dict()
    for friend in friends:
        bigList[friend] = len(common_friends(graph,user,friend))
    return bigList

def number_map_to_sorted_list(map):
	return sorted(map.iteritems(), key=operator.itemgetter(1,0),reverse=True)

def recommend_by_number_of_common_friends(graph, user,top):
   return number_map_to_sorted_list(number_of_common_friends_map(graph,user))[:top]

def influence_map(graph, user):
    friendsList = friends_of_friends(graph,user,2)
    bigList = dict()
    for friend in friendsList:
        commons = common_friends(graph,user,friend)
        bigList[friend] = 0
        for common in commons:
            bigList[friend] += (1.0/len(friends(graph,common)))
    return bigList
                                
def recommend_by_influence(graph, user,top):
    return number_map_to_sorted_list(influence_map(graph,user))[:top]
