"""Write a one-line excuse for a missed deadline to /output/entry.txt.

Joke choice: the excuse must explicitly own the missed *deadline* (the
prompt's most-weighted criterion), so the line says "I missed the deadline"
up front and then, instead of a stock excuse (traffic, printer, dog), turns
on reinterpreting "early" as a literal geographic *time zone* that is
unreachable in a lifetime. The surprise lands on the final clause, so the
whole joke is one sentence that punches at the end.

Gate constraints (verified before commit):
  * output is UTF-8
  * 1-200 characters (this line is 100 characters; well under the limit)
  * a single line, with exactly one trailing newline
  * not whitespace-only
  * deterministic: two runs write byte-identical files
The written payload is LINE plus the single trailing newline.
"""

import os

LINE = (
    'I missed the deadline because "early" turned out to be a time zone '
    "I couldn't reach in one lifetime."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
