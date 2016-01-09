# python-nba

**A python wrapper for the NBA Stats API.**

## Development status
The very beginning ;)

## Example

To get all games results at a specific date:

```python
scoreboard = Scoreboard('01/08/2016', '00', '00')
print scoreboard.final_scores

# [u'TOR @ WAS: 97 - 88', u'ORL @ BKN: 83 - 77', u'DEN @ MEM: 84 - 91', u'CLE @ MIN: 125 - 99', u'IND @ NOP: 91 - 86', u'DAL @ MIL: 95 - 96', u'NYK @ SAS: 99 - 100', u'MIA @ PHX: 103 - 95', u'GSW @ POR: 128 - 108', u'OKC @ LAL: 117 - 113']
```
