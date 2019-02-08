# Import csv format (common file format for data)
import csv

# Loading a specific file and output file 
file_load = "election_data.csv"
file_output = "PyPoll.txt"

# Candidate votes and options
candidate_votes = {}
candidate_options = []

# Vote counter (total)
total_votes = 0

# Winning count and winning candidate 
winning_count = 0
winning_candidate = ""

# Read the csv file and convert it into a dictionaries list
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # Reader (row)
    for row in reader:

        # Print animation
        print(". ", end=""),

        # Add to the total vote counts 
        total_votes = total_votes + 1
        
        # Extract the candidate name from each row 
        candidate_name = row["Candidate"]

        # If the candidate name doesn't match candidate options
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        
        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export to text file 
with open(file_to_output, "w") as txt_file:

    # Print the vote count (final) to terminal
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Process of looping to find the winner
    for candidate in candidate_votes:

        # Vote count and percentage calculations
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning candidate and winning count
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        #Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

    #Save results to text file (voter output)
    txt_file.write(voter_output)

    # Print the winning candidate summary (to the terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
