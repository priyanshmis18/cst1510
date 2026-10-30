"""
RECORD CHECK  -  my version
===========================

Name  : Priyansh Mishra
Lane  :  AI
Date  : 24 october, 2026


run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    """record containing data"""
    def __init__(self, label, value, limit):
        """ record attributes"""
        self.label = label
        self.value = value
        self.limit = limit
    def status(self):
        """ record status"""
        per = (self.value / self.limit) * 100
        if per >= 100:
            return "OVER LIMIT"
        elif per >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.
def load_records(path):
    """try and execpt with dect"""
    records = []
    try:
        with open(path, "r") as f:
            for l in f:
                l = l.strip()
                if not l:
                    continue
                label,val,lim = l.split(",")
                records.append(Record(label,float(val),float(lim)))
    except FileNotFoundError:
        print(f"file'{path}'not found try again")
    return records
records = load_records("records_sample.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)
over = 0
total = 0
for record in records:
    total += 1
    current = record.status()
    if current == "OVER LIMIT":
        over += 1

    percent=(record.value / record.limit) * 100
    difference = record.value - record.limit

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value       : {record.value:>10.2f}")
    print(f"  Limit       : {record.limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {current:>10}")
    print("=" * 34)

# Print final summary line after loop ends
print()
print(f"Checked {total} records. {over} were over limit.")
