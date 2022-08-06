from turtle import onclick
import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender')

selected_movie = st.selectbox('Select a movie to get recommended movies ', (movies['title'].values))
names = []
poster = []

def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2c6055f9b71a9a64762171331a5ad0f3&language=en-US'.format(id))
    data = response.json()
    # st.write(data)
    global ratings
    ratings = data['vote_average']
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x:x[1])
    recommended = distances[1:11]
    
    
    for i in recommended:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        recommended_poster = fetch_poster(movie_id)
        poster.append(recommended_poster)
        
    
                     
if st.button('Recommend'):
    recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(poster[0])
        st.write(names[0])
        st.write("Ratings: ",ratings)
    with col2:
        st.image(poster[1])
        st.write(names[1])
        st.write("Ratings: ",ratings)    
    with col3:
        st.image(poster[2])
        st.write(names[2])
        st.write("Ratings: ",ratings)    
    with col4:
        st.image(poster[3])
        st.write(names[3])
        st.write("Ratings: ",ratings)   
    with col5:
        st.image(poster[4])
        st.write(names[4])
        st.write("Ratings: ",ratings)           
    with col1:
        st.image(poster[5])
        st.write(names[5])
        st.write("Ratings: ",ratings)
    with col2:
        st.image(poster[6])
        st.write(names[6])
        st.write("Ratings: ",ratings)    
    with col3:
        st.image(poster[7])
        st.write(names[7])
        st.write("Ratings: ",ratings)    
    with col4:
        st.image(poster[8])
        st.write(names[8])
        st.write("Ratings: ",ratings)   
    with col5:
        st.image(poster[9])
        st.write(names[9])
        st.write("Ratings: ",ratings)                   