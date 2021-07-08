"""
Created on Fri Apr 10 15:28:23 2020

@author: Swintabel Agyei
"""

#=====================================================
# HELPER FUNCTIONS
#=====================================================
# The functions here are provided for your convenience
# To help you explore the data. Use them as needed
print(" ")
print('written by: Swintabel Agyei')
print(" ")


print('Project Title: Profitable App Profiles for the App Store and Google Play Markets') # Project Title
print(" ")


print('Project Description: This project seeks to analyze data to help in decision making for an Android and iOS mobile apps building company' +
''' whose source of revenue is primarily from in-app adds''')
print(" ")


print('''Project Goal: my main goal is to help developers understand what type of apps are most likely to attract more users''')
print('----------------')



APPLE_STORE = r'F:\micro masters\PYTHON\Swintabel Agyei - Mini Capstone Project 1 - Profitable App Profiles\Mini Capstone Project 1 - Profitable App Profiles\AppleStore.csv'
GOOGLE_PLAY_STORE= r"F:\micro masters\PYTHON\Swintabel Agyei - Mini Capstone Project 1 - Profitable App Profiles\Mini Capstone Project 1 - Profitable App Profiles\googleplaystore.csv"
from csv import reader
def read_data(data):
    '''
    Takes in a data sets and opens them in a readable form.
    Also creates a list of strings for the zeroth index of the data for easy 
    identification of column names.
    data: csv file
    '''
    data=(open(data, encoding="utf8")).readlines() #opens the dataset
    data=list(reader(data)) # creates a list of strings for 0th index 
    return data
    


def explore_data(dataset, start, end, rows_and_columns=False):
       """
      takes a dataset and returns a small slice for preview
      Params:
        dataset: data file you've opened and read into python
        start: start index of slice
        end: end index of the slice
        rows_and_columns: boolean, whether or not to inlcude count of rows and columns

      """
       
       dataset_slice = dataset[start:end]
       print('printing a preview of rows...')
       print(" ")
       for row in dataset_slice:
           print(row)
           print('\n') # adds a new (empty) line after each row
       print('end of rows preview')
       
       print('\n')
      
       if rows_and_columns:
           print('Number of rows:', len(dataset))
           print('Number of columns:', len(dataset[0]))
           print('printing column names ...')
           print(" ")
           columns=[]
           for column in dataset[0]:           
               columns.append(column)  #print column names
           print('column names=', columns)
             

            
  
      

#TASK 3: removing wrong data input 

GOOGLE_PLAY_STORE=read_data(GOOGLE_PLAY_STORE)

del(GOOGLE_PLAY_STORE[10473]) # the deleted index is a wrong input
print('I have deleted row 10473 in the dataset for google playstore because it is a wrong input')

APPLE_STORE=read_data(APPLE_STORE)
#print(APPLE_STORE)
count=0
for row in APPLE_STORE[1:]:
       if len(row) !=len(APPLE_STORE[0]):
                   print(row)#this will print the row data.
                   print(APPLE_STORE.index(row)) #this will print the row no
                   del(row)
                   count+=1
                   
print('Total wrong input in APPLESTORE data= ', count)
print('----------------')


##TASK 4: removing wrong data input


print('There are also duplicates in Google playstore data which I have removed.')

def deal_duplicate(data):
        '''
        takes in as input, data and fishes out duplicates.
        counts duplicates and a provide a preview of them. 
        deletes duplicates not needed.
        input: formated data(with no commas)
        ouput: duplicates, count, delete duplicates'''
    
        app_names=[row[0] for row in data[1:]]
        unique_names=set(app_names)
        counts={name:app_names.count(name) for name in unique_names}
        duplicate_count=0
        duplicate=[]
        for name, count in counts.items():
            if count>1:
               duplicate_count+=count-1
               duplicate.append(name)
        app_names_and_reviews=[row for row in data[1:]] # creating a list of apps and their reviews
        
        dup_full_list={}
        for dup in duplicate:
            list_dup_reviews=[float(app[3]) for app in app_names_and_reviews if app[0]==dup]  #changing reviews to float
            dup_full_list[dup]=list_dup_reviews # creating a dictionary of duplicated apps and their reviews
    
        all_nondup_apps_reviews={} #Task 5: creating a dict of unique apps and their highest review
        for row in data[1:]:
            app=row[0]
            num_of_reviews=row[1:]
            if app in dup_full_list:
                temp=row
                temp[3]=max(dup_full_list[app])
                all_nondup_apps_reviews[app]=temp[1:]
            else:
                all_nondup_apps_reviews[app]=num_of_reviews

        android_clean=[]    #Task 5 cont'd: cleaning google apps data
        already_added=[]
        android_clean.append(data[0])
        for row in data[1:]:
            app_name=row[0]
            row_data=row[1:]
            if app_name in all_nondup_apps_reviews and row_data==all_nondup_apps_reviews[app_name]:
                   if row not in already_added:
                            
                            android_clean.append(row)
                            already_added.append(row)
                            

       
            
       
        print('Below is a preview of such duplicated apps.')
        print(" ")
        print(duplicate[0:5])
        print(" ")
        print('Total duplicates:', duplicate_count)
        print('----------------')
        print('cleaning data...')
        print(" ")
        print('Below is a preview of the cleaned data and the total rows and columns in the data')
        print(" ")
        explore_data(android_clean, 0, 5, rows_and_columns=True)
        
        return android_clean
        
#deal_duplicate(GOOGLE_PLAY_STORE)   

# Task 6 and 7: non english apps 

def is_english_app(name):
    '''this function takes in the name of an app 
    and determines if it is an english or non-english app
    input= name of the app(string)
    output=True or False(boolean)
    '''
    non_eng_char=0
    for character in name:
        
        if ord(character)>127:
            non_eng_char+=1
            
            if non_eng_char>3:
                return False
                break
    else:
        return True


def english_app_in_data(data1, data2): 
    '''
    This function takes in two datasets and 
    returns the non english apps in the datasets.
    data=list
    output=list of non english apps'''
    
    
    data1=deal_duplicate(data1)
    google_names=[rowb for rowb in data1[0:]]
    play_names=[rowa for rowa in data2[0:]]
    
    
    english_play_2=[]
    english_goo_1=[]
    non_english_goo_1=[]
    non_english_play_2=[]
    
    for app_p in play_names:
        Ans1=is_english_app(app_p[1])
        if Ans1==True:
            english_play_2.append(app_p)
        elif Ans1==False:
            non_english_play_2.append(app_p)
    
    for app_g in google_names:
        Ans2=is_english_app(app_g[0])
        if Ans2==True:
             english_goo_1.append(app_g)
        elif Ans2==False:
              non_english_goo_1.append(app_g)
              
    
              
    print('----------------')            
    print('We are interested in english apps. Therefore I have removed the non-english Apps as well from both datasets')
    
    
    
    print(" ")     
    print('non english apps preview for Apps store is as follows')
    print(" ") 
    print(non_english_play_2[0:10])
    
    
    
    print(" ")
    print('non english apps preview for google playstore is as follows')
    print('----------------')
    print(non_english_goo_1[0:10])
    print(" ")
    
    
    
    print('The following are some english apps found in the Apps store datasets as well as current total rows and columns')
    print('----------------')
    explore_data(english_play_2, 0, 10, rows_and_columns=True)
    print('initial total rows in Apps store data=', len(data2))
    print('----------------')
    
    
    print(" ")
    print('The following are some english apps found in the google playstore datasets, current rows and columns')
    print('----------------')
    explore_data( english_goo_1, 0, 10, rows_and_columns=True)
    print('initial total rows in google data=', len(data1))
    print('----------------')
    return english_goo_1, english_play_2



#english_app_in_data(GOOGLE_PLAY_STORE, APPLE_STORE) 
  
# TASK 8
def free_apps(data1, data2):
    
    
    data=english_app_in_data(data1, data2)
    data1=data[0]
    data2=data[1]
    
    
    google=[rowa for rowa in data1[1:]]
    play=[rowb for rowb in data2[1:]]
    non_free_google=[]
    non_free_play=[]
    
    for app in google:
        if app[6]!='Free':
            google.remove(app)
            non_free_google.append(app)
            
    for appp in play:
        if appp[4]!='0':
           play.remove(appp)
           non_free_play.append(appp)
           
           
           
    print('\n')
    print('Since we are also interested in free Apps, we need to remove the paid apps from both datasets.')
    print('Below is a preview of paid apps in the google playstore dataset that I am removing')
    print('----------------')
    print(non_free_google[1:10])
    print('----------------')
    print('\n')
    print('Below is a preview of non-free apps in the Apps store dataset that I am removing')
    print('----------------')
    print(non_free_play[1:10])
    print('\n')
    print('Total apps in google playstore after removing duplicates and non-english Apps=', len(data1))
    print('Total free apps in google playstore=', len(google))
    print('Total apps in Apps store after removing non-english Apps=', len(data2))
    print('Total free apps in Apps store=', len(play))
    print('----------------')
    

    print('Now, our main goal is to get apps that thrive in both App store and Google play markets to invest in them.', end=' ')    
    print('To this end, I would be looking for the most common genres in both markets.', end=' ')    
    print('This is because, our source of revenue rellies on in app adds which also relies on how attractive and satisfying people find the app to be.' )    
    google[0]=data1[0]
    play[0]=data2[0]
    return google, play    
#free_apps(GOOGLE_PLAY_STORE, APPLE_STORE)    


def frequency(data):
    
        'Takes in data and anylzes it to provide frequency of unique apps'
    
    
    
        print('Below are the genres in both markets and the frequency of apps under each genre')    
        print('----------------')
        print(" ") 
        
        count=0
        google=data[0]
        Apps_store=data[1]
        genre_0=[row[1] for row in google[1:]]
        reviews=[[row[1],list(row[5])] for row in google[1:]]
        google_reviews=[]
        Total_0=len(genre_0)
        genre_1=[row1[11] for row1 in Apps_store[1:]]
        reviews1=[[row1[11],row1[5]] for row1 in Apps_store[1:]]
        Total_1=len(genre_1)
        
        unique_genre=set(genre_0)
        unique_genre_1=set(genre_1)
           
        frequency_0={}
        frequency_1={}
        
        for genre in unique_genre:
            count=genre_0.count(genre)
            per_1=(count/Total_0)*100
            frequency_0[genre]=[round(per_1,2)]
            
        for genre1 in unique_genre_1:
            count=genre_1.count(genre1)
            per_2=(count/Total_1)*100
            frequency_1[genre1]=[round(per_2,2)]
        for char in reviews:
            if ' ' in char[1]:
                char[1].remove(' ')
            if str('+') in char[1]:
                char[1].remove(str('+'))
            if ' ' in char[1]:
                char[1].remove(' ')
            
            new_char=''.join(char[1])
            if new_char=='1000000 000':
                new_char='1000000000'
            list0=(char[0],int(new_char))
            google_reviews.append(list0)
        google_review={}
        for genre in google_reviews:
            google_review[genre[0]]=0
        
        for genre in google_reviews:
            if genre[0] in google_review:
                google_review[genre[0]]+=genre[1]
            
        for char in reviews1:
            char[1]=int(char[1])
        Appstore_reviews={}
        for genre in reviews1:
            Appstore_reviews[genre[0]]=0
        for genre in reviews1:
            if genre[0] in Appstore_reviews:
                 Appstore_reviews[genre[0]]+=genre[1]
        
        return frequency_0, frequency_1,google_review,Appstore_reviews


data=free_apps(GOOGLE_PLAY_STORE, APPLE_STORE)    
frequency(data)    
    
market=frequency(data)
google_playstore_market=market[0]
App_store_market=market[1]
google_reviews=market[2]
Appstore_reviews=market[3]

import pandas as pd

google_playstore_market_df=pd.DataFrame.from_dict(google_playstore_market, orient="index", columns=["App frequency"])
App_store_market_df=pd.DataFrame.from_dict(App_store_market, orient="index", columns=["App frequency"])
google_reviews_df=pd.DataFrame.from_dict(google_reviews, orient='index', columns=['Total Installations'])
Appstore_reviews_df=pd.DataFrame.from_dict(Appstore_reviews, orient='index', columns=['Total count of ratings'])

print('Google Playstore Market genres and their App frequencies in descending order')
googlefre=google_playstore_market_df.sort_values(by=['App frequency'], ascending=False)
print(google_playstore_market_df.sort_values(by=['App frequency'], ascending=False))
  
print('----------------')    
print('Apple store Market genres and their App frequencies')
Appstorefre=App_store_market_df.sort_values(by=['App frequency'], ascending=False)    
print(App_store_market_df.sort_values(by=['App frequency'], ascending=False)) 

print('----------------') 
print('From the initial results, it seems frequency of apps produced under genre only tells us half of the story.', end='')  
print('For this reason, we would like to find out how engaged customers are with the apps under each genre.', end='')
print('Total number of installations and ratings under google market and Apple store market will tell us this')
print('----------------') 
print('let us have a look at the total installations per genre for google market in descending order')
print(' ')
google_asc=google_reviews_df.sort_values(by=['Total Installations'], ascending=False)
print(google_reviews_df.sort_values(by=['Total Installations'], ascending=False))
print('----------------') 

print('let us have a look at the total rating counts per genre for Apple store market in descending order')
print(' ')
appstore_asc=Appstore_reviews_df.sort_values(by=['Total count of ratings'], ascending=False)
print(Appstore_reviews_df.sort_values(by=['Total count of ratings'], ascending=False))
print(' ')
print("RECOMMENDATIONS FOR APPS THAT WOULD BE PROFITABLE")
print(' ')
print('According to total installations, the top ten genres I recommend for the production of apps in Google play store market are as follows')
print('----------------')
print(google_asc.head(10))
print(' ')
print('According to total rating counts, the top ten genres I recommend for the production of apps in Apple store market are as follows')
print('----------------')
print(appstore_asc.head(10))
print('----------------') 
print('Thank you')















