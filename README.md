# 127scraper
The world's first webscraper focussed only on the CMPT 127 scoreboard, and notifies you when the scoreboard updates so you don't have to god damn check it and refresh a billion times.

## Instructions

1. Clone the repository
```
git clone https://github.com/FrankWhoee/127scraper.git
cd 127scraper
```
2. Open update-notifier.py and set the YOUR_USERNAME variable to your username on the scoreboard.
3. Run the notifier
`./run`
4. Now detach the process
```
Ctrl + Z
bg %1
disown %1
```

The job numbers (`%1`) might be different depending on your computer, but generally that should be correct. Bet bet bet.

Have fun being notified that you got 0/10 lmaooooooo
