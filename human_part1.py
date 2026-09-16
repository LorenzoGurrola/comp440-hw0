"""
Part 1: basic rating statistics.

    uv run python human_part1.py

Answer the four questions below with your own code, print each answer under its label, and
explain each in one sentence in WRITEUP.md.
"""

from load_data import load_all
import statistics
import numpy as np
import pandas


def human_part1(ratings, ratings_df, movies, movies_df, users, users_df):


    # print(users)
    # print(users_df)

    print("== (a) ==")
    print("Numer of ratings: " + str(len(ratings)))
    print("Number of users: " + str(len(users)))
    print("Number of movies: " + str(len(movies_df)))
    count = [0,0,0,0,0,0]
    for rating in ratings:
        count[rating.rating] += 1
    print("One star: " + str(count[1]) + 
          "\nTwo star: " + str(count[2]) +
          "\nThree star: " + str(count[3]) +
          "\nFour star: " + str(count[4]) +
          "\nFive star: " + str(count[5]))
    # (a) How many ratings, users, and movies are there, and how are ratings distributed across 1-5 stars?

    print("== (b) ==")
    count = np.zeros(max(users_df.user_id)+1)
    for rating in ratings:
        count[rating.user_id] += 1
    print("Median numer of ratings per user: " + str(statistics.median(count)))
    print("Num of users with 100 or more ratings: " + str(len(count[count >= 100])))

    # (b) What is the median number of ratings per user, and how many users have 100 or more ratings?

    print("== (c) ==")
    movies_df["num_ratings"] = 0
    for rating in ratings:
        movies_df.at[rating.movie_id-1, "num_ratings"] = movies_df.at[rating.movie_id-1, "num_ratings"] + 1
    print(movies_df.sort_values(by="num_ratings", ascending=False)[["title", "num_ratings"]][0:10])
    
    
    # (c) Join ratings to titles. Which 10 movies have the most ratings?

    print("== (d) ==")
    movies_df["total_ratings"] = 0
    for rating in ratings:
        movies_df.at[rating.movie_id-1, "total_ratings"] = movies_df.at[rating.movie_id-1, "total_ratings"] + rating.rating

    movies_df["avg_rating"] = movies_df["total_ratings"]/movies_df["num_ratings"]

    movies_df_modified = movies_df[movies_df["num_ratings"] >= 20]
    
    print(movies_df_modified.sort_values(by="avg_rating", ascending=False)[["title","avg_rating","num_ratings"]][0:10])
    
    # (d) Among movies with at least 20 ratings, which 10 have the highest mean rating?
    #     Show title, mean, and count.


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part1(ratings, ratings_df, movies, movies_df, users, users_df)
