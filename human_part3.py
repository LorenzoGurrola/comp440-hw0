"""
Part 3: the most ___ movie.

    uv run python human_part3.py

Pick an adjective. Write it on the `**My adjective:**` line of WRITEUP.md and a one-sentence
definition a classmate could code on the `**My definition:**` line. Print the top 5 movies
under it.
"""

from load_data import load_all


def top5_my_definition(ratings, ratings_df, movies, movies_df):
    print("== My definition ==")
    movies_df["num_ratings"] = 0
    for rating in ratings:
        movies_df.at[rating.movie_id-1, "num_ratings"] = movies_df.at[rating.movie_id-1, "num_ratings"] + 1
    movies_df["total_ratings"] = 0
    for rating in ratings:
        movies_df.at[rating.movie_id-1, "total_ratings"] = movies_df.at[rating.movie_id-1, "total_ratings"] + rating.rating
    movies_df["avg_rating"] = movies_df["total_ratings"]/movies_df["num_ratings"]
    movies_df = movies_df[movies_df["total_ratings"] >= 20]
    movies_df["genres"] = movies_df[["Action", "Adventure", 'Animation', 'Children\'s', 'Comedy', 'Crime',
       'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
       'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']].sum(axis=1)
    movies_df["my_score"] = movies_df["genres"] - movies_df["avg_rating"]
    print(movies_df.sort_values(by="my_score", ascending=False)[["title","genres","avg_rating","my_score"]][0:5])


def human_part3(ratings, ratings_df, movies, movies_df):
    top5_my_definition(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part3(ratings, ratings_df, movies, movies_df)
