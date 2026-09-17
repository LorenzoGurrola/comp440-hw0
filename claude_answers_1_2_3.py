"""
Claude's answers to the three questions in questions.md.

    uv run python claude_answers_1_2_3.py

Filled in by a Claude that has never seen the student's work. Kept as it was written.
"""

from load_data import load_all


def question1(ratings_df, movies_df):
    print("=" * 70)
    print("1(a) Basic counts and rating distribution")
    print("=" * 70)
    n_ratings = len(ratings_df)
    n_users = ratings_df["user_id"].nunique()
    n_movies = ratings_df["movie_id"].nunique()
    print(f"{n_ratings:,} ratings, {n_users:,} users, {n_movies:,} movies")
    print("\nRatings by star value:")
    dist = ratings_df["rating"].value_counts().sort_index()
    for stars, count in dist.items():
        pct = 100 * count / n_ratings
        print(f"  {stars} stars: {count:>6,} ({pct:5.1f}%)  {'#' * int(pct)}")

    print()
    print("=" * 70)
    print("1(b) Ratings per user")
    print("=" * 70)
    per_user = ratings_df.groupby("user_id").size()
    print(f"Median ratings per user: {per_user.median():.1f}")
    print(f"Users with >= 100 ratings: {(per_user >= 100).sum():,} out of {len(per_user):,}")

    print()
    print("=" * 70)
    print("1(c) The 10 most-rated movies")
    print("=" * 70)
    counts = ratings_df.groupby("movie_id").size().rename("count")
    joined = movies_df.set_index("movie_id")[["title"]].join(counts)
    most_rated = joined.sort_values("count", ascending=False).head(10)
    for title, count in zip(most_rated["title"], most_rated["count"]):
        print(f"  {count:>4,}  {title}")

    print()
    print("=" * 70)
    print("1(d) Highest mean rating (>= 20 ratings)")
    print("=" * 70)
    stats = ratings_df.groupby("movie_id")["rating"].agg(["mean", "count"])
    joined = movies_df.set_index("movie_id")[["title"]].join(stats)
    qualified = joined[joined["count"] >= 20]
    top_mean = qualified.sort_values("mean", ascending=False).head(10)
    for title, mean, count in zip(top_mean["title"], top_mean["mean"], top_mean["count"]):
        print(f"  {mean:.2f}  ({count:>3} ratings)  {title}")


def question2(ratings_df, movies_df):
    print()
    print("=" * 70)
    print("2. What is the best movie in this dataset?")
    print("=" * 70)
    stats = ratings_df.groupby("movie_id")["rating"].agg(["mean", "count"])
    joined = movies_df.set_index("movie_id")[["title"]].join(stats)

    # A raw highest-mean ranking is dominated by movies with a handful of 5-star
    # ratings (e.g. one rating of 5 gives a "perfect" 5.0 mean). To find a movie
    # that's genuinely good, not just lucky, use a Bayesian-averaged score that
    # pulls each movie's mean toward the overall mean, with strength proportional
    # to how few ratings it has. This is the same shrinkage IMDb uses for its
    # "Top 250" list.
    overall_mean = ratings_df["rating"].mean()
    min_ratings = 50  # how many ratings a movie needs before we trust it much
    joined["bayesian_mean"] = (
        (joined["count"] * joined["mean"] + min_ratings * overall_mean)
        / (joined["count"] + min_ratings)
    )

    best = joined.sort_values("bayesian_mean", ascending=False).head(10)
    print(f"(Bayesian-shrunk mean toward the overall average of {overall_mean:.2f}, "
          f"prior strength = {min_ratings} ratings)\n")
    print(f"{'score':>6}  {'mean':>5}  {'count':>6}  title")
    for title, score, mean, count in zip(best["title"], best["bayesian_mean"], best["mean"], best["count"]):
        print(f"{score:6.2f}  {mean:5.2f}  {count:6,}  {title}")

    winner = best.iloc[0]
    print(f"\nBest movie: {winner['title']!r} "
          f"(mean {winner['mean']:.2f} over {winner['count']:,.0f} ratings)")


def question3(ratings_df, movies_df):
    print()
    print("=" * 70)
    print("3. Which movie is the most confused?")
    print("=" * 70)
    # "Most confused" = the movie users disagree about the most: the highest
    # standard deviation of star ratings. Require a reasonable number of ratings
    # so the result isn't just a movie with two wildly different ratings.
    stats = ratings_df.groupby("movie_id")["rating"].agg(["mean", "std", "count"])
    joined = movies_df.set_index("movie_id")[["title"]].join(stats)

    min_ratings = 20
    qualified = joined[joined["count"] >= min_ratings]
    most_confused = qualified.sort_values("std", ascending=False).head(10)
    print(f"(highest standard deviation of ratings, among movies with >= {min_ratings} ratings)\n")
    print(f"{'std':>5}  {'mean':>5}  {'count':>6}  title")
    for title, std, mean, count in zip(
        most_confused["title"], most_confused["std"], most_confused["mean"], most_confused["count"]
    ):
        print(f"{std:5.2f}  {mean:5.2f}  {count:6,}  {title}")

    winner = most_confused.iloc[0]
    print(f"\nMost confused movie: \"{winner['title']}\" -- std dev {winner['std']:.2f}, "
          f"mean {winner['mean']:.2f} over {winner['count']:,.0f} ratings")

    print("\nRating breakdown for the most confused movie:")
    top_movie_id = most_confused.index[0]
    breakdown = ratings_df[ratings_df["movie_id"] == top_movie_id]["rating"].value_counts().sort_index()
    for stars, count in breakdown.items():
        print(f"  {stars} stars: {count}")


def claude_answers():
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    question1(ratings_df, movies_df)
    question2(ratings_df, movies_df)
    question3(ratings_df, movies_df)


if __name__ == "__main__":
    claude_answers()
