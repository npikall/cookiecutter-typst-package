# ruff: noqa: D100, D101, D103, EXE001
import shutil
from datetime import date
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd().resolve()


def remove_file(file: str) -> None:
    filepath: Path = PROJECT_DIRECTORY / file
    filepath.unlink()


def remove_dir(directory: str) -> None:
    dir_path: Path = PROJECT_DIRECTORY / directory
    shutil.rmtree(dir_path)


def main() -> None:
    license = "{{cookiecutter.license}}"

    if license == "None":
        remove_file("LICENSE")

    license_file = PROJECT_DIRECTORY / "LICENSE"
    if license_file.exists():
        license_dated = license_file.read_text().replace(
            "[yyyy]", str(date.today().year)
        )
        with license_file.open("w") as f:
            f.write(license_dated)


if __name__ == "__main__":
    main()
