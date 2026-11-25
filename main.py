import os

ENTRY = (
    "fix(prod): it works now and I have no idea why, "
    "which means it will break the moment I sleep"
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
