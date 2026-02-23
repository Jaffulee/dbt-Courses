from __future__ import annotations

from pathlib import Path

from course_parser.captions_loader import load_captions_index


def main() -> None:
    captions_root = Path(r"response\refactoring SQL for modularity")
    index = load_captions_index(captions_root=captions_root, slug_subdir_name="slug")

    print("Captions media count:", len(index))
    # Show a few samples
    for i, (hid, cap) in enumerate(index.items()):
        print(f"hashedId={hid} name={cap.media_name!r} chunks={len(cap.chunks)}")
        if cap.chunks:
            print("  first:", (cap.chunks[0].text[:120] + "...") if len(cap.chunks[0].text) > 120 else cap.chunks[0].text)
        if i >= 9:
            break


if __name__ == "__main__":
    main()