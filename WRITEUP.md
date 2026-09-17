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

**My definition** (one sentence, precise enough that a classmate could code it)**:** A movie that is in too many genres for its own good.

**One definition I considered and rejected, and why:** XXXX

**Top 5 under my definition:**

XXXX

**What your definition captures, what it misses, and where "___-ness" lives in this data — the
genre labels, what the crowd did, or the words in the titles. At most 150 words:**

XXXX

## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code
or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

XXXX

## Part 5. Comparing the best movie

**Claude's rule:**

XXXX

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

XXXX

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

XXXX

**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

XXXX

## Part 6. Comparing the most ___ movie

**Claude's definition:**

XXXX

**Is Claude's film in your top 5?**

XXXX

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

XXXX

## Working with Claude

**What you asked Claude for during Parts 1–3** (debugging and installing only — say what you
got stuck on)**:**

XXXX

**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

XXXX

**What you would do differently next time, in 3–5 sentences:**

XXXX

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at
the step. Or "nowhere." One or two sentences:**

XXXX

**Hours spent:** XXXX

**Anyone who helped you, or "no one":** XXXX
