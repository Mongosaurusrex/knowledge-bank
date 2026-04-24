from pathlib import Path
import re

ROOT = Path(".") 


def snake_case(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[ -]+", "_", name)          
    name = re.sub(r"[^a-z0-9_]", "", name)     
    name = re.sub(r"_+", "_", name)            
    return name.strip("_")


dirs = sorted(
    [p for p in ROOT.rglob("*") if p.is_dir()],
    key=lambda p: len(p.parts),
    reverse=True
)

for old_path in dirs:
    new_name = snake_case(old_path.name)

    if new_name and new_name != old_path.name:
        new_path = old_path.with_name(new_name)

        if new_path.exists():
            print(f"SKIP exists: {old_path} -> {new_path}")
            continue

        old_path.rename(new_path)
        print(f"RENAMED: {old_path} -> {new_path}")