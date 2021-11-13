# Election_Analysis - Overview of Election Audit
## Project Overview
The objective of this analysis is to assist Colorado Board of Elections employee with an election audit for a recent local congressional election following the steps below;
 * How many votes were cast in this congressional election?
 * Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
 * Which county had the largest number of votes?
 * Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
 * Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

## Election-Audit Results
 * In order to determine the total votes cast in this congressional election, the variable `total_votes` was set to `0` and iterated through each row and increments by `1`
 * A breakdown of the number of votes and the percentage of total votes for each county in the precinct was determined by creating a county list and county votes dictionary `county_names = []` and
`county_votes = {}`and tracking the largest county and county voter turnout `winning_county = ""`
`winning_votes = 0`, as well as running a `for loop` to retrieve vote count and percentage, calculate the percentage of votes for the county using the script `vote_percentage_county = float(votes_county)/float(total_votes) * 100` and printing the the county results using an `f" string`function. An `if statement` was looped into the above `for loop`to determine the winning county and get its vote count 
 
 * To obtain the county with the largest number of votes, using the `for loop` above, the veriable     `winning_county` was nested into the `f" string`  `(
        f"------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"------------------------------\n"
        )` 
        and the winning county was printed and saved to a `.txt` file.
 * An `if statement` was looped into another `for loop`to determine the number of votes and the percentage of the total votes each candidate received and initializing a varable `candidate_results` to be equal to an `f" string` the result was printed and saved to a `.txt` file
 * Below is a breakdown of the election results
    
    * The analysis of the election show that:
        * There were "369,711" votes cast in the election.
        * The canditates were:
         * Charles Casper Stockham
         * Diana DeGette
         * Raymon Anthony Doane
        * The canditates results were:
            * Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes
            * Diana DeGette received "73.8%" of the vote and "272,892" number of votes
            * Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes
    
        * The winner of the election was
            * Diana DeGette, who received "73.8%" of the vote and "272,892" number of votes
     * The analysis of the election challenge on the election results show that:
        * Jefferson County received "10.5%" of the vote and "38,855" number of votes
        * Denver County received "82.8%" of the vote and "306,055" number of votes
        * Arapahoe County received "6.7%" of the vote and "24,801" number of votes
    * The county with the highest turnout is Denver
    * Election screenshot is shown below
    
    `Election Results`
    
    ![Election_Results.png](https://github.com/charleside2001/Election_Analysis/blob/main/Resources/Election_Result.png)
 ## Election-Audit Summary
The python script written for this analysis can be used to perform analysis for other elections by;     
* Changing the current     file part to a file      part with the source     data with the same       number of columns. 
* alternatively, this      script will also work    for other data with more columns by appropriating the correct row index `row[i]` in the `for loop`.
* The `f" string` can also be formatted to show several election variables


 
