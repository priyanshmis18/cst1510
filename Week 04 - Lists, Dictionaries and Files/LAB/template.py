"""
RECORD CHECK  -  my version
===========================

Name  : Priyansh Mishra
Lane  :  AI
Date  : 17.10.26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
def check_record(value, limit):
    """Calculate the difference, percentage, and status for a given value and limit."""
    diff = value - limit
    percent = (value / limit) * 100
    
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 80:
        status = "WARNING"
    else:
        status = "OK"
        
    return diff, percent, status


def print_report(label, value, limit, diff, percent, status):
    """Print a clean, formatted report line for a single record."""
    print(f"{label} -> Value: {value} | Limit: {limit} | Diff: {diff:.1f} | Percent: {percent:.1f}% | Status: {status}")




def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records_list = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records_list.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })
    return records_list



try:
    records = load_records("it_records.txt")
except FileNotFoundError:
    print("Error: 'it_records.txt' could not be found. Starting with an empty list.")
    records = []




over_limit_count = 0
results_lines = []

for r in records:

    diff, percent, status = check_record(r["value"], r["limit"])
    

    print_report(r["label"], r["value"], r["limit"], diff, percent, status)
    
    if status == "OVER LIMIT":
        over_limit_count += 1
        
    results_lines.append(f"{r['label']},{status}")

total_count = len(records)
print("-" * 50)
print(f"Summary: {over_limit_count} of {total_count} were over limit.")


with open("results.txt", "w") as out_f:
    for line in results_lines:
        out_f.write(line + "\n")

print("Results successfully written to 'results.txt'.")

