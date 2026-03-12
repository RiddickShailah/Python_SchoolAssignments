# lab12.py  — Pandas Mini-Practice 
# pip or pip3 install pandas if you have not installed pandas
# Run:  python lab12.py

import pandas as pd

# ----------------------------
# Fixed mini datasets (given)
# ----------------------------

df_people = pd.DataFrame(
    {
        "id":   [101, 102, 103, 104],
        "name": ["Ana", "Bo", "Chen", "Dee"],
        "age":  [20,   22,   21,    20],
    }
)

df_scores = pd.DataFrame(
    {
        "id":    [101, 102, 104, 105],
        "score": [88,   72,   59,  91],
    }
)

# ==========================================
# TODO functions (students fill in the body)
# ==========================================

def sort_by_age(df):
    """
    Return df sorted by 'age' ascending.
    """
    return df.sort_values(by="age").reset_index(drop=True)


def sort_by_age_then_name(df):
    """
    Return df sorted by age asc, then name desc.
    """
    return df.sort_values(by=["age", "name"], ascending=[True, False]).reset_index(drop=True)


def select_name_age_21_plus(df):
    """
    Keep columns ["name","age"] and rows where age >= 21.
    """
    return df.loc[df["age"] >= 21, ["name", "age"]].reset_index(drop=True)


def resize_people(df):
    """
    Resize df_people:
      - Add one new row (id=106, name='Eli', age=23)
      - Add a new column 'age_plus_1' = age + 1
      - Drop the original 'age' column and return
    """
    new_row = pd.DataFrame({"id": [106], "name": ["Eli"], "age": [23]})
    df_new = pd.concat([df, new_row], ignore_index=True)
    df_new["age_plus_1"] = df_new["age"] + 1
    df_new = df_new.drop(columns=["age"])
    return df_new


def merge_people_scores_left(df_ppl, df_scr):
    """
    Left-merge df_people with df_scores on 'id' (keep all people).
    """
    return pd.merge(df_ppl, df_scr, how="left", on="id")


def concat_rows(df):
    """
    Row-wise: split df_people into two parts and concat back together.
    """
    n = len(df)
    df1 = df.iloc[:n//2, :]
    df2 = df.iloc[n//2:, :]
    return pd.concat([df1, df2], ignore_index=True)


def concat_cols(df_ppl, df_scr):
    """
    Column-wise: concat df_people[["id"]] and df_scores[["score"]].
    """
    df1 = df_ppl[["id"]].reset_index(drop=True)
    df2 = df_scr[["score"]].reset_index(drop=True)
    return pd.concat([df1, df2], axis=1)


# ==========================
# Tiny PASS/FAIL test suite. DO NOT EDIT CONTENT BELOW.
# ==========================
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def check(name, cond):
    print(f"{name}: " + (f"{GREEN}PASS{RESET}" if cond else f"{RED}FAIL{RESET}"))

def main():
    print("=== Lab 12: Pandas Mini-Practice ===\n")

    # 1) Sorts
    s1 = sort_by_age(df_people)
    check("Sort by age asc (is_monotonic_increasing)",
          s1["age"].is_monotonic_increasing)

    s2 = sort_by_age_then_name(df_people)
    ok_age = s2["age"].is_monotonic_increasing
    ok_ties = True
    for age_val, group in s2.groupby("age"):
        names = list(group["name"])
        if names != sorted(names, reverse=True):
            ok_ties = False
            break
    check("Sort by age asc, then name desc (ties handled)", ok_age and ok_ties)

    # 2) Select
    sel = select_name_age_21_plus(df_people)
    check("Select columns ['name','age']",
          list(sel.columns) == ["name", "age"])
    check("Select rows age >= 21",
          (sel["age"].min() >= 21) if not sel.empty else True)

    # 3) Resize
    rz = resize_people(df_people)
    check("Resize: +1 row",
          rz.shape[0] == df_people.shape[0] + 1)
    check("Resize: has 'age_plus_1' and dropped 'age'",
          ("age_plus_1" in rz.columns) and ("age" not in rz.columns))

    # 4) Merge (left)
    mg = merge_people_scores_left(df_people, df_scores)
    check("Merge-left keeps all people",
          mg.shape[0] == df_people.shape[0])
    check("Merge-left produces NaN for missing scores",
          mg["score"].isna().any())

    # 5) Concat
    rcat = concat_rows(df_people)
    check("Concat rows reconstructs df_people",
          rcat.reset_index(drop=True).equals(df_people.reset_index(drop=True)))

    ccat = concat_cols(df_people, df_scores)
    check("Concat cols has both 'id' and 'score'",
          set(ccat.columns) == {"id", "score"})

    print("\nDone.")

if __name__ == "__main__":
    main()
