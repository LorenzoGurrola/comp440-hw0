"""
Part 2: the best movie.

    uv run python human_part2.py

Write your rule on the `**My rule:**` line of WRITEUP.md. Print the top 10 movies (id, title,
ratings count, mean rating) under it.
"""

from load_data import load_all


def top10_my_rule(ratings, ratings_df, movies, movies_df):
    print("== My rule ==")
    movies_df["num_ratings"] = 0
    for rating in ratings:
        movies_df.at[rating.movie_id-1, "num_ratings"] = movies_df.at[rating.movie_id-1, "num_ratings"] + 1
    movies_df["total_ratings"] = 0
    for rating in ratings:
        movies_df.at[rating.movie_id-1, "total_ratings"] = movies_df.at[rating.movie_id-1, "total_ratings"] + rating.rating
    movies_df["avg_rating"] = movies_df["total_ratings"]/movies_df["num_ratings"]
    movies_df["year"]=0
    for i in range(len(movies_df)):
        l = len(str(movies_df.at[i, "title"]))
        try:
            movies_df.at[i, "year"] = int(str(movies_df.at[i, "title"])[l-5:l-1])
        except(ValueError):
            movies_df.at[i, "year"] = 1995
    movies_df["my_score"] = movies_df["avg_rating"]/5 + movies_df["total_ratings"]/max(movies_df["total_ratings"]) + (2026-movies_df["year"])/400
    print(movies_df.sort_values(by="my_score", ascending=False)[["movie_id", "title", "num_ratings", "avg_rating", "my_score"]][0:10])

def human_part2(ratings, ratings_df, movies, movies_df):
    top10_my_rule(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part2(ratings, ratings_df, movies, movies_df)
