# lol-worlds-2020
Colaborative ML models to predict the results of League of Legends Worlds 2020

The datasets are from [Oracle's Elixir](https://oracleselixir.com/) and are structured as follows in the folders:

World's statistics so far:
datasets/worlds/*.csv

Summer playoff statistics:
datasets/summer-playoffs/name-of-region/*.csv

In each folder you have 3 different types of datasets, one with information about the players, another with information about the teams and another with information about the champions.

### Definitions

In most of the stats on the Oracle's Elixir's website, values are calculated for each individual game, then averaged across games. This is true for the "share" and "per minute" numbers for damage to champions, earned gold, wards placed/cleared, CKPM, and so on. Some of the numbers used on broadcasts use totals rather than averages, which can make minor differences to some values. They prefer averages because they reduce the impact of game length. Bear this in mind when comparing between Oracle's Elixir and stats you find elsewhere.

| Stats | Definitions |
| --- | --- |
| A	| Total assists|
| AGT	| Average game time/duration, in minutes |
| APG	| Assists per game |
| B%	| Percentage of games in which the champion was banned (not tied to a specific role) |
| BN%	| Baron control rate |
| CCPM	| Crowd control dealt to champions per minute |
| Champion	| Champion name |
| CKPM	| Average combined kills per minute (team kills + opponent kills) |
| CS%P15	| Average share of team's total CS post-15-minutes |
| CSD10	| Average creep score difference at 10 minutes |
| CSD15	| Average creep score difference at 15 minutes |
| CSD20	| Average creep score difference at 20 minutes |
| CSPM	| Average monsters + minions killed per minute |
| CTR%	| Counter-pick rate: percentage of games in which this player/champion was picked after their lane opponent (not always available) |
| CWPM	| Control wards purchased per minute |
| D	| Total deaths |
| DMG%	| Damage Share: average share of team’s total damage to champions |
| DPG	| Deaths per game |
| DPM	| Average damage to champions per minute |
| DRG%	| Dragon control rate: percent of all Dragons killed that were taken by the team, reflecting only elemental drakes if ELD% is present |
| DTH%	| Average share of team’s deaths |
| EGPM	| Average earned gold per minute (excludes starting gold and inherent gold generation) |
| EGR	| Early-Game Rating |
| ELD%	| Elder dragon control rate |
| F3T%	| First-to-three-towers rate (percentage of games in which team was the first to 3 tower kills |
| FB%	| First Blood rate -- for players/champions, percent of games earning a First Blood participation (kill or assist) |
| FBN%	| First Baron rate |
| FBV%	| First Blood Victim rate -- percent of games player/champion was killed for First Blood |
| FD%	| First dragon rate |
| FT%	| First tower rate |
| GD10	| Average gold difference at 10 minutes |
| GD15	| Average gold difference at 15 minutes |
| GD20	| Average gold difference at 20 minutes |
| GOLD%	| Gold Share: average share of team’s total gold earned (excludes starting gold and inherent gold generation) |
| GP	| Games Played |
| GPM	| Average gold per minute |
| GPR	| Gold percent rating (average amount of game’s total gold held, relative to 50%) |
| GSPD	| Average gold spent percentage difference |
| GXD10	| Average gold+experience difference at 10 minutes |
| GXD15	| Average gold+experience difference at 15 minutes |
| GXD20	| Average gold+experience difference at 20 minutes |
| HLD%	| Rift Herald control rate |
| IWC%	| Average percentage of opponent’s invisible wards cleared |
| JNG%	| Jungle Control: average share of game’s total jungle CS |
| K	| Total kills |
| KD	| Kill-to-Death Ratio |
| KDA	| Total Kill/Death/Assist ratio |
| KP	| Kill participation: percentage of team's kills in which player earned a Kill or Assist |
| KPG	| Kills per game |
| KS%	| Kill share: player's percentage of their team's total kills |
| L	| Losses |
| LNE%	| Lane Control: average share of game’s total lane CS |
| MLR	| Mid/Late Rating |
| P%	| Percentage of games champion was picked in this role. |
| P+B%	| Percentage of games in which the champion was either banned or picked in any role |
| Player	| Player's in-game name |
| Pos	| Position |
| Team	| Team name |
| VSPM	| Vision score per minute |
| VWC%	| Average percentage of opponent’s visible wards cleared |
| W	| Wins |
| W%	| Win percentage |
| WC%	| Average percentage of opponent wards cleared |
| WCPM	| Average wards cleared per minute |
| WPM	| Average wards placed per minute |
| XPD10	| Average experience difference at 10 minutes |
| XPD15	| Average experience difference at 15 minutes |
| XPD20	| Average experience difference at 20 minutes |
