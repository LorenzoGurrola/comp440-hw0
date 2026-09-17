# HW0 writeup

**Name:** Lorenzo Gurrola
**Date:** 2026-09-11

Replace every placeholder below with your answer. Every number you give comes from a script in this repo; say which one.

## Part 1. Basic rating statistics

Code: `human_part1.py`. One or two sentences per answer, with the numbers.

**(a) How many ratings, users, and movies are there, and how are ratings distributed across 1–5 stars?**

We can use a numpy array to hold the number of each amount of stars, where index = num_stars

**(b) What is the median number of ratings per user, and how many users have 100 or more ratings?**

We can use the same where count[user_id] is the number of ratings for that user. Then filter.

**(c) Which 10 movies have the most ratings?**

Now we change tactics, and work with the pandas library to do some data wrangling.

**(d) Among movies with at least 20 ratings, which 10 have the highest mean rating?**

Made some new columns to hold the data...totaled the number of stars then divided by num_ratings to reach average.

**Anything you got stuck on (what you tried, where it broke), or "none":**

Tried using the numpy indexing tactic for parts c and d, then had to learn some pandas from youtube and google.

## Part 2. The best movie

Code: `human_part2.py`.

**My rule:** (avg_rating/5) + total_ratings/max(total_ratings) + (2026-year)/400

**One rule I considered and rejected, and why:** I was going to go with (avg_rating/5) + total_ratings/max(total_ratings), but I wanted to do some extra data wrangling to get year column, and a bit more complex equation.

**Top 10 under my rule:**

     movie_id                             title  num_ratings  avg_rating  my_score
49         50                  Star Wars (1977)          583    4.358491  1.994198
99        100                      Fargo (1996)          508    4.155512  1.736878
180       181         Return of the Jedi (1983)          507    4.007890  1.708763
126       127             Godfather, The (1972)          413    4.283293  1.687841
173       174    Raiders of the Lost Ark (1981)          420    4.252381  1.665849
97         98  Silence of the Lambs, The (1991)          390    4.289744  1.603851
257       258                    Contact (1997)          509    3.803536  1.595112
171       172   Empire Strikes Back, The (1980)          367    4.204360  1.563113
0           1                  Toy Story (1995)          452    3.878319  1.543050
482       483                 Casablanca (1942)          243    4.456790  1.527568

**Why my rule, in at most 150 words. Name one thing it gains and one thing it loses:**

I think ratings are the most important factor, so I wanted to heavily weight that. I also think that a movie that has been rated more proved that it deserves its rating more. I also included a small bias towards older movies, but that's my own personal bias.

## Part 3. The most ___ movie

Code: `human_part3.py`.

**My adjective:** confused

**My definition** (one sentence, precise enough that a classmate could code it)**:** A movie that is in too many genres for its own good. (lots of genres + has low rating)

**One definition I considered and rejected, and why:** I was thinking about doing something more sophisticated, but figured it would be nice to keep it simple for this one.

**Top 5 under my definition:**

                                     title  genres  avg_rating  my_score
559   Kid in King Arthur's Court, A (1995)       6    2.727273  3.272727
425    Transformers: The Movie, The (1986)       6    2.843750  3.156250
1075                Pagemaster, The (1994)       5    2.250000  2.750000
20           Muppet Treasure Island (1996)       5    2.761905  2.238095
819                       Space Jam (1996)       5    2.774194  2.225806

**What your definition captures, what it misses, and where "___-ness" lives in this data — the
genre labels, what the crowd did, or the words in the titles. At most 150 words:**

My definition does a good job of finding movies that are listed in lots of genres and have low rating. Whether this means the movie was rated low because it was "confused," or because of another reason, is something my definition doesn't capture.

## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code
or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

Yes, they did!

## Part 5. Comparing the best movie

**Claude's rule:**

Bayesian-averaged score

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

A raw highest-mean ranking is dominated by movies with a handful of 5-star ratings (e.g. one rating of 5 gives a "perfect" 5.0 mean). To find a movie that's genuinely good, not just lucky, use a Bayesian-averaged score that pulls each movie's mean toward the overall mean, with strength proportional to how few ratings it has. This is the same shrinkage IMDb uses for its "Top 250" list.

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

== My rule ==
     movie_id                             title  ...  avg_rating  my_score
49         50                  Star Wars (1977)  ...    4.358491  1.994198
99        100                      Fargo (1996)  ...    4.155512  1.736878
180       181         Return of the Jedi (1983)  ...    4.007890  1.708763
126       127             Godfather, The (1972)  ...    4.283293  1.687841
173       174    Raiders of the Lost Ark (1981)  ...    4.252381  1.665849
97         98  Silence of the Lambs, The (1991)  ...    4.289744  1.603851
257       258                    Contact (1997)  ...    3.803536  1.595112
171       172   Empire Strikes Back, The (1980)  ...    4.204360  1.563113
0           1                  Toy Story (1995)  ...    3.878319  1.543050
482       483                 Casablanca (1942)  ...    4.456790  1.527568

Claude
 score   mean   count  title
  4.33   4.47     298  Schindler's List (1993)
  4.31   4.45     283  Shawshank Redemption, The (1994)
  4.30   4.46     243  Casablanca (1942)
  4.29   4.36     583  Star Wars (1997)
  4.25   4.39     267  Usual Suspects, The (1995)
  4.22   4.39     209  Rear Window (1954)
  4.20   4.29     390  Silence of the Lambs, The (1991)
  4.20   4.28     413  Godfather, The (1972)
  4.19   4.49     112  Close Shave, A (1995)
  4.19   4.47     118  Wrong Trousers, The (1993)

**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

Claude's rule is better for when the movie has very few ratings, as it tries to average it out around ~3.5. Our rules are roughly identical when the number of ratings grows and becomes more reliable. I guess mine is a bit better if the user is biased towards old movies.

## Part 6. Comparing the most ___ movie

**Claude's definition:**

The highest standard deviation of star ratings, among movies with ≥20 ratings

**Is Claude's film in your top 5?**

No

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

Interesting. Claude's definition is based around viewer perception, while mine is around genre and intended meaning. Claude ranks a movie that has divisive ratings as confused, while I rank a movie in multiple categories and with low overall rating as confused.

## Working with Claude

**What you asked Claude for during Parts 1–3** (debugging and installing only — say what you
got stuck on)**:**

Nothing. I had to switch from using numpy indexing to working with pandas, which I was unfamiliar with (I'm used to working with dataframes in R), but I did all of my research on Google.

**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

I didn't look too closely at the equation for the bayesian mean, but I asked it how using that mean affects the score of a movie with few ratings vs. a movie with many.

**What you would do differently next time, in 3–5 sentences:**

Abandon the numpy indexing sooner when I started to struggle with it. Recognize it was kind've a niche solution and that there was likely a better way to work with the dataframes.

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at
the step. Or "nowhere." One or two sentences:**

I was a bit confused on where I was supposed to look for Claude's answers and logic for its parts. But I asked it to summarize what it (or I guess the other agent), did, and that worked well.

**Hours spent:** 3.5

**Anyone who helped you, or "no one":** No one
