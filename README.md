# Election Audit for Counties in Colorado
## Overview of Election Audit
The purpose of this audit analysis is to quickly verify counts for multiple counties and different candidates. The goal is to identify the winner, including the percentage of votes and the total votes they received. It is also helpful to understand which counties had more participation than others. It can be verified against the number of registered voters in those counties as an election integrity verification. 

## Election Audit Results
* 369,711 votes were cast in this congressional election 
* The counties that were included in this analysis were Jefferson, Denver and Arapahoe. The results for each of these were as follows: 
    * Jefferson: 38,855 votes, which was 10.5% of the total votes
    * Denver:    306,055 votes, which was 82.8% of the total votes
    * Arapahoe:  24,801 votes, which was 6.7% of the total votes
* According to this information, **Denver** had the largest number of votes
* There were 3 candidates in this election. The results for each candidate are:
   * Charles Casper Stockham: 23.0% of the overall vote with 85,213 votes
   * Diana DeGette:           73.8% of the overall vote with 272,892 votes
   * Raymon Anthony Doane:    3.1% of the overall vote with 11,606 votes
* Based on this information, **Diana DeGette** won this congressional election with 272,892 votes and 73.8% 
<p align="center" width="100%">
    <img width="50%" src=https://user-images.githubusercontent.com/105991478/176971014-68fd10a4-5cd2-46ce-9f76-d6ad77d405e5.png>
</p>
## Election Audit Summary
Now that this script has been created, it can be used for future elections as well. The script will work for elections with more than 3 candidates, or for including other states and counties as well. The election data would need to be formatted correctly, and the references to the csv file would need to be updated as well. The line of code referencing the csv file is shown below. 

```   
file_to_load = os.path.join("Resources", "election_results.csv")

```
