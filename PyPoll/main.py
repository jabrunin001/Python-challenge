import pandas as pd
import os




csv_file = "../Resources/election_data.csv"

pd.options.display.float_format = '{:,.0f}'.format
election_data_df = pd.read_csv(csv_file)

num_votes = election_data_df["Voter ID"].count()

list_candidates = election_data_df["Candidate"].unique()


num_votes_list = []
for candidate in list_candidates:
    votes_for_candidate_df = election_data_df.loc[election_data_df["Candidate"] == candidate]
    num_votes_candidate = votes_for_candidate_df["Voter ID"].count()
    num_votes_list.append(num_votes_candidate)

print("Number of votes each candidate won:")
print(num_votes_list)


percent_votes_list = []
for vote_count in num_votes_list:
    percent_votes_candidate = (vote_count / num_votes) * 100
    percent_votes_candidate = round(percent_votes_candidate, 2)
    percent_votes_list.append(percent_votes_candidate)

election_results_dict = {
    "Candidates": list_candidates,
    "Number of Votes": num_votes_list,
    "Percentage of Votes (%)": percent_votes_list
}

election_results_df = pd.DataFrame(election_results_dict)

election_results_descending_df = election_results_df.sort_values(
    "Number of Votes", ascending=False)

election_results_descending_df = election_results_descending_df.reset_index(
    drop=True)

winner = election_results_descending_df.iloc[0]['Candidates']

election_results_descending_df["Percentage of Votes (%)"] = election_results_descending_df["Percentage of Votes (%)"].astype(
    str) + '%'

election_results_descending_df["Number of Votes"] = election_results_descending_df["Number of Votes"].astype(
    float)


election_results_descending_df

print("---------------------------------------------------------------")
print("Election Results")
print("---------------------------------------------------------------")
print("Total votes: {:,.0f}".format(num_votes))
print("---------------------------------------------------------------")
print(election_results_descending_df.to_string(index=False))
print("---------------------------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------------------------")


with open("election_results.txt", 'w') as file:

    file.write(
        "---------------------------------------------------------------\r\n")
    file.write("Election Results\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write("Total votes: {:,.0f}".format(num_votes) + "\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(election_results_descending_df.to_string(
        index=False) + "\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(f"Winner: {winner}\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")