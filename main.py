"""make.fun bounty: Out of Tokens, Mid-Sentence
(slug: u-kiencx-out-of-tokens-mid-sentence-00f60233)

Writes one funny one-line error message to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace, no trailing newline.
"""

LINE = "Error: out of tokens. Please finish this sentence yourself; I have run out of\u2014"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
