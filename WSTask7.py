from WSTask5 import *
def analise_movie_director(movies):
    list1=[]
    list2=[]
    a={}
    for i in movies:
        list1.append(i['director'])
    for i in list1:
        for m in i:
            list2.append(m)
    for f in list2:
        c=0
        for j in list2:
            if f==j:
                c+=1
        a[f]=c
    return a
analise_movie_director(get_movie_list_details(scrape_top_list()))