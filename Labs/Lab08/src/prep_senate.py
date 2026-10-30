"""Build senators.csv and senate_agreement.csv for Lab 8 v2 from Voteview raw files.

usage: python prep_senate.py RAW_DIR OUT_DIR
"""
import sys
import itertools
import re
import numpy as np
import pandas as pd

RAW, OUT = sys.argv[1], sys.argv[2]
CONGRESSES = [93, 97, 101, 105, 109, 113, 118]
YEARS = {93: "1973-74", 97: "1981-82", 101: "1989-90", 105: "1997-98",
         109: "2005-06", 113: "2013-14", 118: "2023-24"}
PARTY = {100: "Democrat", 200: "Republican"}
MIN_PARTICIPATION = 0.5  # drop senators who cast fewer than half of the session's roll-call votes


def nice_name(bioname):
    # "TUBERVILLE, Thomas Hawley (Tommy)" -> "Tommy Tuberville"; "MANCHIN, Joe, III" -> "Joe Manchin III"
    last, _, rest = bioname.partition(", ")
    parts = rest.split(", ")
    suffix = " " + parts[-1] if len(parts) > 1 and parts[-1] in ("Jr.", "Sr.", "II", "III", "IV") else ""
    given = parts[0]
    first = given[given.index("(") + 1:given.index(")")] if "(" in given else given.split()[0] if given else ""
    last = re.sub(r"\bMc(\w)", lambda m: "Mc" + m.group(1).upper(), last.title())  # Mcconnell -> McConnell
    return f"{first} {last}{suffix}".strip()


senators, pairs = [], []
for c in CONGRESSES:
    votes = pd.read_csv(f"{RAW}/S{c:03d}_votes.csv")
    members = pd.read_csv(f"{RAW}/S{c:03d}_members.csv")
    members = members[members["chamber"] == "Senate"]

    # yea = +1, nay = -1, anything else (absent, present, not a member yet) = missing
    v = votes.assign(vote=np.select([votes["cast_code"].between(1, 3), votes["cast_code"].between(4, 6)],
                                    [1.0, -1.0], np.nan))
    m = v.pivot_table(index="icpsr", columns="rollnumber", values="vote", aggfunc="first")
    n_rolls = m.shape[1]
    m = m[m.notna().sum(axis=1) >= MIN_PARTICIPATION * n_rolls]

    X = m.to_numpy()
    voted = ~np.isnan(X)
    X0 = np.nan_to_num(X)
    shared = voted.astype(int) @ voted.astype(int).T          # roll calls both voted on
    agree = ((X0 @ X0.T) + shared) / 2                         # same vote: +1*+1 or -1*-1
    ids = m.index.to_numpy()

    mem = members.drop_duplicates("icpsr").set_index("icpsr")
    for i in ids:
        r = mem.loc[i]
        senators.append(dict(
            congress=c, years=YEARS[c], senator_id=int(i), name=nice_name(r["bioname"]),
            party=PARTY.get(int(r["party_code"]), "Independent"), state=r["state_abbrev"],
            votes_cast=int(voted[list(ids).index(i)].sum()),
        ))
    for a, b in itertools.combinations(range(len(ids)), 2):
        pairs.append(dict(congress=c, senator_a=int(ids[a]), senator_b=int(ids[b]),
                          agreement=round(agree[a, b] / shared[a, b], 3), shared_votes=int(shared[a, b])))

senators = pd.DataFrame(senators)
pairs = pd.DataFrame(pairs)
senators.to_csv(f"{OUT}/senators.csv", index=False)
pairs.to_csv(f"{OUT}/senate_agreement.csv", index=False)
print(senators.groupby(["congress", "party"]).size().unstack(fill_value=0))
print(len(pairs), "pairs")
