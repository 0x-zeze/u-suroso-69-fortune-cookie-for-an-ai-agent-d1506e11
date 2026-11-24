from pathlib import Path

LINE = "You will receive great news: the agent you asked to back up your files also backed up your personality, and it runs better without you."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"{LINE}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
