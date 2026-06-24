#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PGP_CONFIG = ROOT / "src/config/pgp.json"
POSTS_DIR = ROOT / "src/content/posts"
SIGS_DIR = ROOT / "public/signatures"


def load_fingerprint() -> str:
    return json.loads(PGP_CONFIG.read_text())["fingerprint"]


def find_post(arg: str) -> Path:
    slug = Path(arg).stem  # strips any extension and path
    for ext in ("mdx", "md"):
        path = POSTS_DIR / f"{slug}.{ext}"
        if path.exists():
            return path
    print(f"Error: no post found for slug '{slug}'")
    print(f"  looked in {POSTS_DIR}/{slug}.{{mdx,md}}")
    sys.exit(1)


def inject_signed(post: Path) -> None:
    content = post.read_text()
    parts = content.split("---", 2)
    if len(parts) < 3:
        print("Warning: couldn't parse frontmatter, skipping signed: true injection")
        return

    frontmatter = parts[1]
    if re.search(r"^signed:", frontmatter, re.MULTILINE):
        frontmatter = re.sub(r"^signed:.*", "signed: true", frontmatter, flags=re.MULTILINE)
    else:
        frontmatter = frontmatter.rstrip("\n") + "\nsigned: true\n"

    post.write_text("---" + frontmatter + "---" + parts[2])


def sign(post: Path, sig: Path, fingerprint: str) -> None:
    subprocess.run(
        ["gpg", "--armor", "--detach-sign", "--local-user", fingerprint, "--output", str(sig), str(post)],
        check=True,
    )


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: scripts/sign-post.py <post-slug-or-filename>")
        print("  e.g. scripts/sign-post.py holy-gap-batman")
        print("  e.g. scripts/sign-post.py src/content/posts/holy-gap-batman.mdx")
        sys.exit(1)

    fingerprint = load_fingerprint()
    post = find_post(sys.argv[1])
    slug = post.stem

    SIGS_DIR.mkdir(parents=True, exist_ok=True)
    sig = SIGS_DIR / f"{slug}.asc"

    inject_signed(post)
    sign(post, sig, fingerprint)

    print(f"\n✓ Signed '{slug}'")
    print(f"  Signature:  {sig.relative_to(ROOT)}")
    print(f"  Frontmatter updated with signed: true")
    print(f"\nReaders can verify with:")
    print(f"  curl https://shaungarwood.com/source/{slug} > post.mdx")
    print(f"  curl https://shaungarwood.com/signatures/{slug}.asc > post.asc")
    print(f"  gpg --verify post.asc post.mdx")


if __name__ == "__main__":
    main()
