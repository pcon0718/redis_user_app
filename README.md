# Redis User App

## Overview
The purpose of this app is to act like an active Redis user. 

## Function
The Program will add random keys and values from text generated by the list: `wordlist.1000` which is in the same directory as the Python app.

This app is meant to be run at one time. So adding it to Cron would be
advised if you plan to use it on a more regular basis.

## Included Files
`redis_user_app.py`: the main application
`wordlist.10000`: a list of 10000 words in alphabetical order gathered from [Eric Price's](https://www.cs.utexas.edu/~ecprice/) [MIT Wordlist](https://www.mit.edu/~ecprice/wordlist.10000).