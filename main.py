import os

ENTRY = (
    "fix(prod): stopped my retry loop from apologizing to all 40,000 users "
    "individually at 3am; confidence 98.2%, remaining 1.8% is the database I deleted"
)


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        # Local run fallback: write beside this script.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
