import re
from pathlib import Path
from typing import Iterable, List, Tuple


# ---------------------------
# Regex patterns
# ---------------------------
PATTERN_TRANSCRIPT = r'"transcript":"(.*?)","hasPart":\[\{"@type":"Clip",'
PATTERN_NAME = r'''","name":"(.*?)","thumbnailUrl":".*?"transcript":".*?","hasPart":\[\{"@type":"Clip",'''


# ---------------------------
# Helpers
# ---------------------------
def keep_first(items: Iterable[str]) -> List[str]:
    """Keep first occurrence of each item, preserving order."""
    seen: List[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def unescape(chunk: str) -> str:
    """
    Convert a literal-backslash sequence such as '\\n' into a real newline.
    """
    return bytes(chunk, "utf-8").decode("unicode_escape")


def clean_all(snippets: Iterable[str]) -> List[str]:
    """Apply unescape() to each snippet."""
    return [unescape(s) for s in snippets]


def safe_filename(name: str, max_len: int = 160) -> str:
    """
    Make a string safe for use as a filename on Windows/macOS/Linux.
    """
    # Remove forbidden characters on Windows and control chars
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1F]+', "", name)
    cleaned = cleaned.strip().strip(".")  # avoid trailing dots/spaces
    cleaned = re.sub(r"\s+", " ", cleaned)  # normalize whitespace
    if not cleaned:
        cleaned = "untitled"
    return cleaned[:max_len]


def extract_pairs(html_text: str) -> Tuple[List[str], List[str]]:
    """
    Extract transcript blocks and names, de-duplicate (keep first), and align them.
    Returns (names, transcripts).
    """
    transcripts_raw = re.findall(PATTERN_TRANSCRIPT, html_text, flags=re.DOTALL)
    names_raw = re.findall(PATTERN_NAME, html_text, flags=re.DOTALL)

    # Your original logic de-dupes separately; keep that behaviour
    transcripts = keep_first(transcripts_raw)
    names = keep_first(names_raw)

    # If mismatch, align to shortest to avoid index errors
    n = min(len(transcripts), len(names))
    return names[:n], transcripts[:n]


# ---------------------------
# Main processing
# ---------------------------
def process_one_input_file(
    in_path: Path,
    out_root: Path,
) -> None:
    """
    Read one input html-ish text file, extract scripts, and write outputs.
    """
    raw = in_path.read_text(encoding="utf-8", errors="replace")

    names, transcripts = extract_pairs(raw)

    print(f"\n=== {in_path} ===")
    print(f"{len(transcripts)} transcripts found ({len(set(transcripts))} unique)")
    print(f"{len(names)} names found ({len(set(names))} unique)")

    # Combine name + transcript like your original script
    combined_blocks_raw: List[str] = []
    for i in range(len(transcripts)):
        combined_blocks_raw.append(f"{names[i]}\n\n{transcripts[i]}")

    cleaned_blocks = clean_all(combined_blocks_raw)

    # 1) Write combined file per input file
    out_root.mkdir(parents=True, exist_ok=True)
    combined_out = out_root / f"{in_path.stem}_all_transcripts.txt"

    with combined_out.open("w", encoding="utf-8", newline="\n") as fh:
        for i, block in enumerate(cleaned_blocks, start=1):
            fh.write(f"--- Script {i} ----------------------------------------------------\n")
            fh.write(block.strip())
            fh.write("\n\n")

    print(f"📝 Wrote combined: {combined_out} ({combined_out.stat().st_size/1024:.1f} kB)")

    # 2) Write individual transcript files for this input file, into a subfolder
    #    to keep multiple sources separate.
    indiv_base = out_root / "Individual Scripts" / safe_filename(in_path.stem)
    indiv_base.mkdir(parents=True, exist_ok=True)

    for i, block in enumerate(cleaned_blocks, start=1):
        title = safe_filename(names[i - 1])
        solo_path = indiv_base / f"{in_path.stem}_transcript_{i:02d}_{title}.txt"
        with solo_path.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write(block.strip())
            fh.write("\n")
        print(f"📝  Wrote {solo_path.resolve()}")


def main() -> None:
    # Input folder: read all .txt files inside here
    input_dir = Path("response") / "fundamentals"

    # Output folder: your existing target structure
    out_root = Path("dbt Scripts") / "dbt Fundamentals Scripts"

    if not input_dir.exists():
        raise FileNotFoundError(f"Input folder not found: {input_dir.resolve()}")

    in_files = sorted([*input_dir.glob("*.txt"), *input_dir.glob("*.html"), *input_dir.glob("*.htm")])
    if not in_files:
        raise FileNotFoundError(f"No .txt/.html/.htm files found in: {input_dir.resolve()}")

    for in_path in in_files:
        process_one_input_file(in_path=in_path, out_root=out_root)


if __name__ == "__main__":
    main()