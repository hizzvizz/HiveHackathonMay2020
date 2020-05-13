This is a submission by https://peakd.com/@rubenalexander to the hive hackerthon -> https://peakd.com/stem/@themarkymark/stemgeek-s-first-hackathon.

The goal of this entry is to gamify information available from
the hive blockchain. In particular I give the user a multiple choice quiz based on the comments, posts, and total payout based on the most used tags.

The backend is written in Python (communicates through beempy) and the front in is in HTML CSS and Javascript.

This is a MVP and simply tallies a users points, asks questions based on the user's choice of tags. 

In the future, I could see this site dig into hive data and have quizzes based on post content. I could also see this site support multiple quiz takers at once and have the results posted to an account dedicated to this quiz game.

This is my first hackerthon and I am really happy the python I learned in grad school earlier this year is seeing new uses.

Original plan

"""
- STAGE ONE: 
-- game TQ: Ten Questions about the hive blockchain!
-- game to guess stats about hive
-- stats: comments, payouts, posts
-- gamer chooses 10 tags. 
-- code generates 10 questions multiple _choice
-- 5 points for a close answer, 10 points for the exact answer
-- (started on 5/1 bug free as of 5/2)

- STAGE TWO: 
-- present the game as 'pleasing to the eye' website
-- write hive post with proper tags
-- include link to game in post
-- code is migrated to a public repo on github
-- update post with github link
-- submit to Hackathon discord when stage two is complete

- STAGE THREE: 
-- report game resuls to hive as a post from a dedicated
hive account.
-- comments -> results for each answer

- BONUS: 
-- retro graphics and a mouth speaking the words
-- words for each question are spoken with computer voice

"""
"""
imported remi and beem
"""

"""
https://healeycodes.com/javascript/python/beginners/webdev/2019/04/11/talking-between-languages.html