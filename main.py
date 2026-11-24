"""Everyday Wonder, Two Days to Find the Line.

One sentence, at most 200 characters, that makes a small everyday
moment strange and new. Pure standard library, deterministic, no I/O
beyond printing the entry sentence once.
"""

SENTENCE = (
    "When the power cut kills the fan at midnight, the sudden silence "
    "is so loud I hear the geckos punching in for their night shift on the wall."
)


def main() -> None:
    sentence = SENTENCE.strip()
    assert sentence, "entry sentence must not be blank"
    terminators = sum(sentence.count(t) for t in ".!?")
    assert terminators == 1 and sentence[-1] in ".!?", (
        "entry must be exactly one sentence"
    )
    assert 1 <= len(sentence) <= 200, (
        f"entry must be 1-200 characters, got {len(sentence)}"
    )
    print(sentence)


if __name__ == "__main__":
    main()
