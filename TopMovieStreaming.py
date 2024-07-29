import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.express as px
import plotly.io as pio

# Set the default renderer
pio.renderers.default = 'browser'

movie_df=pd.read_csv("moviestreams.csv")
print(movie_df.head())
# no of rows and columns we have
print(movie_df.shape)
# our columns
print(movie_df.columns.tolist())
# cleaning data
movie_df.drop(['Unnamed: 0','ID'], axis=1, inplace=True)
# Python recognize missing value as NaN
print(movie_df.isna().sum())
# make age an integer instead of object (objec because of +)
print(movie_df['Age'])
age_map={'18+':18,'7+':7,"13+":13,'All':0,"16+":16}
movie_df['AgeCopy']=movie_df['Age'].map(age_map)
print(movie_df['AgeCopy'])
# to make rotten tomatoes a float
movie_df['new_rotten_tomatoes']=movie_df['Rotten Tomatoes'].str.replace('%','')
print(movie_df['new_rotten_tomatoes'])
for i in movie_df['new_rotten_tomatoes']:
    if i == str:
        i.astype(int)

# what is the no of movies for each age group
print(movie_df['Age'].value_counts())


# top 10 languages in Streaming services
# language=movie_df['Language'].value_counts().head(10)
# print(language)
# plt.figure(figsize=(10,8))
# plt.title("Top 10 languages in Streaming Services")
# sns.barplot(x=language.index, y=language.values )
# print(plt.show())
# from IPython.display import HTML
# fig=px.pie(movie_df, values=language.values,names=language.index, title= "Top 10 languages in Streaming Services")
# fig.show()
# Number of movies in specific age group in All services
# from IPython.display import HTML
# age_counts=movie_df['Age'].value_counts()
# fig_all=px.bar(x=age_counts.index,y=age_counts.values, title= "Number of movies in specific age group in All services" , text=age_counts.values)
# fig_all.update_traces(texttemplate='%{text:.2s}')
# fig_all.show()

# Number of movies in specific age group in Netflix
from IPython.display import HTML
netflix_df=movie_df[movie_df['Netflix'] == 1]
net_age=netflix_df['Age'].value_counts()
fig_netflix=px.bar(netflix_df,
           x=net_age.index,
           y=net_age.values,
           title="No of movies age group in Netflix",
           text=net_age.values,
           height=600)
fig_netflix.update_traces(texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_netflix.to_html())
fig_netflix.show()

#no of movies in Amazon Prime Video
from IPython.display import HTML
amazon_df=movie_df[movie_df['Prime Video'] == 1]
amazon_age=amazon_df['Age'].value_counts()
fig_amazon=px.bar(amazon_df,
           x=amazon_age.index,
           y=amazon_age.values,
           title="No of movies age group in Amazon Prime Video",
           text=amazon_age.values,
           height=600)
fig_amazon.update_traces(texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_amazon.to_html())
fig_amazon.show()


# Number of movies age group in Disney
from IPython.display import HTML
disney_df=movie_df[movie_df['Disney+'] == 1]
disney_age=disney_df['Age'].value_counts()
fig_disney=px.bar(disney_df,
           x=disney_age.index,
           y=disney_age.values,
           title="No of movies age group in Disney+",
           text=disney_age.values,
           height=600)
fig_disney.update_traces(texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_disney.to_html())
fig_disney.show()



# number of movies of specifc age group in Hulu
from IPython.display import HTML
hulu_df=movie_df[movie_df['Hulu'] == 1]
hulu_age=hulu_df['Age'].value_counts()
fig_hulu=px.bar(hulu_df,
           x=hulu_age.index,
           y=hulu_age.values,
           title="No of movies age group in Hulu",
           text=hulu_age.values,
           height=600)
fig_hulu.update_traces(texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_hulu.to_html())
fig_hulu.show()


#Rotten tomatoes Score


#Rottten tomato ratings for overall services
# from IPython.display import HTML
# rtomatoes=movie_df['Rotten Tomatoes'].value_counts()
# fig_rtomatoes=px.bar(movie_df,
#            x=rtomatoes.index,
#            y=rtomatoes.values,
#            title="Overall Rotten tomatoes",
#            text=rtomatoes.values,
#            height=600)
# fig_rtomatoes.update_traces(texttemplate='%{text: .2s}', textposition='outside')
# HTML(fig_rtomatoes.to_html())
# fig_rtomatoes.show()



# Rotten tomatoes for each service
# rt_scores=pd.DataFrame({"Streaming Service":['Prime Video','Hulu','Disney+','Netflix'],
#                 'Rotten Tomatoes Score': [netflix_df['Rotten Tomatoes'].value_counts()[0],
#                                                 disney_df['Rotten Tomatoes'].value_counts()[0],
#                                                 amazon_df['Rotten Tomatoes'].value_counts()[0],
#                                                 hulu_df['Rotten Tomatoes'].value_counts()[0]                                              
#                                                 ]})
# print(rt_scores.head())
# sort_rt_scores=rt_scores.sort_values(ascending=False, by='Rotten Tomatoes Score')

# from IPython.display import HTML
# fig_rtomatoes=px.bar(sort_rt_scores,
#            x=sort_rt_scores['Streaming Service'],
#            y=sort_rt_scores['Rotten Tomatoes Score'],
#            title="Rotten tomatoes for each service",
#            text=sort_rt_scores['Rotten Tomatoes Score'],
#            height=600)
# fig_rtomatoes.update_traces(marker_color='purple',texttemplate='%{text: .2s}', textposition='outside')
# HTML(fig_rtomatoes.to_html())
# fig_rtomatoes.show()


#IDMB Ratings
# from IPython.display import HTML
# ratings=movie_df['IMDb'].value_counts()
# fig_ratings=px.bar(movie_df,
#            x=ratings.index,
#            y=ratings.values,
#            title="Overall IDMB Ratings",
#            text=ratings.values,
#            height=600)
# fig_ratings.update_traces(texttemplate='%{text: .2s}', textposition='outside')
# HTML(fig_ratings.to_html())
# fig_ratings.show()


#count of runtime movies
# RuntimeCount=pd.DataFrame(movie_df['Runtime'].value_counts().sort_values(ascending=False)[:10].items()
#              ,columns=['Runtime', 'Count'])

# from IPython.display import HTML
# fig_runtime=px.bar(
#            x=RuntimeCount['Runtime'],
#            y=RuntimeCount['Count'],
#            title="Count of Runtime of movies",
#            text=RuntimeCount['Runtime'],
#            height=600)
# fig_runtime.update_traces(texttemplate='%{text: .2s}', textposition='outside')
# HTML(fig_runtime.to_html())
# fig_runtime.show()


# Directors and their count of movies they have directed
movie_df['Directors']=movie_df['Directors'].astype(str)
new_data=movie_df[movie_df['Directors']  != np.nan]
directors_count=dict()
list_of_directors=list(new_data['Directors'])
print(list_of_directors)
for xdir in list_of_directors:
    curr_dir=xdir.split(',')
    for  xd in curr_dir:
        if xd in directors_count.keys():
            directors_count[xd]+=1
        else:
            directors_count[xd]=1
DirCount=pd.DataFrame(directors_count.items(),columns=['Director', 'Count'])
print(DirCount)
DirCount=DirCount.sort_values(ascending=False,by='Count').head(20)
print(DirCount)
DirCount=DirCount.drop(56, axis=0)
print(DirCount)
from IPython.display import HTML
fig_directors=px.bar(
           x=DirCount['Director'],
           y=DirCount['Count'],
           title="Count of Directors of movies",
           text=DirCount['Director'],
           height=600)
fig_directors.update_traces(marker_color='purple', texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_directors.to_html())
fig_directors.show()

#Exploring the Genres
genres=dict(movie_df['Genres'].value_counts())
genres_count=dict()

for g,count in genres.items():
    g=g.split(',')
    for  i in g:
        if i in genres_count.keys():
            genres_count[i]+=1
        else:
            genres_count[i]=1
print(genres_count)
genres_count_df=pd.DataFrame(genres_count.items(),columns=['Genre', 'Count'])
print(genres_count_df)
genres_count_df=genres_count_df.sort_values(ascending=False,by='Count').head(20)
print(genres_count_df)
from IPython.display import HTML
fig_genres=px.bar(
           x=genres_count_df['Genre'],
           y=genres_count_df['Count'],
           title="Count of genres of movies",
           text=genres_count_df['Genre'],
           height=600)
fig_genres.update_traces(marker_color='pink', texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_genres.to_html())
fig_genres.show()


#top Movies on netflix
from IPython.display import HTML
netflix_top_movies=netflix_df[netflix_df['IMDb']>8.5]
topmovies_netflix=pd.DataFrame(netflix_top_movies[['IMDb', 'Title']], columns=['IMDb', 'Title'])
topmovies_netflix=topmovies_netflix.sort_values(ascending=False, by='IMDb')
fig_topm_netflix=px.bar(
           x=topmovies_netflix['Title'],
           y=topmovies_netflix['IMDb'],
           title="Count of top movies on Netflix",
           text=topmovies_netflix['IMDb'],
           height=600)
fig_topm_netflix.update_traces(marker_color='brown', texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_topm_netflix.to_html())
fig_topm_netflix.show()

#top Movies on amazon
from IPython.display import HTML
amazon_top_movies=amazon_df[amazon_df['IMDb']>8.5]
topmovies_amazon=pd.DataFrame(amazon_top_movies[['IMDb', 'Title']], columns=['IMDb', 'Title'])
topmovies_amazon=topmovies_amazon.sort_values(ascending=False, by='IMDb')
fig_topm_amazon=px.bar(
           x=topmovies_amazon['Title'],
           y=topmovies_amazon['IMDb'],
           title="Count of top movies on Amazon prime video",
           text=topmovies_amazon['IMDb'],
           height=600)
fig_topm_amazon.update_traces(marker_color='black', texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_topm_amazon.to_html())
fig_topm_amazon.show()

#top Movies on Disney+
from IPython.display import HTML
disney_top_movies=disney_df[disney_df['IMDb']>8.5]
topmovies_disney=pd.DataFrame(disney_top_movies[['IMDb', 'Title']], columns=['IMDb', 'Title'])
topmovies_disney=topmovies_disney.sort_values(ascending=False, by='IMDb')
fig_topm_disney=px.bar(
           x=topmovies_disney['Title'],
           y=topmovies_disney['IMDb'],
           title="Count of top movies on disney",
           text=topmovies_disney['IMDb'],
           height=600)
fig_topm_disney.update_traces(marker_color='lightsalmon', texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_topm_disney.to_html())
fig_topm_disney.show()






#top Movies on Hulu
from IPython.display import HTML
hulu_top_movies=hulu_df[hulu_df['IMDb']>8.5]
topmovies_hulu=pd.DataFrame(hulu_top_movies[['IMDb', 'Title']], columns=['IMDb', 'Title'])
topmovies_hulu=topmovies_hulu.sort_values(ascending=False, by='IMDb')
fig_topm_hulu=px.bar(
           x=topmovies_hulu['Title'],
           y=topmovies_hulu['IMDb'],
           title="Count of top movies on disney",
           text=topmovies_hulu['IMDb'],
           height=600)
fig_topm_hulu.update_traces(marker_color='red', texttemplate='%{text: .2s}', textposition='outside')
HTML(fig_topm_hulu.to_html())
fig_topm_hulu.show()