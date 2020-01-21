""" Adds (potentially) missing version to setup.cfg
"""
import pathlib, os, re

setup_cfg = pathlib.Path(os.environ["SRC_DIR"]) / "setup.cfg"

setup_cfg_text = setup_cfg.read_text()

version_matches = re.findall(r"^version\s=\s(.*)$", setup_cfg_text, flags=re.M)

if version_matches:
    print("setup.cfg looks fine", version_matches)
else:
    print("setup.cfg needs a version")

    setup_cfg_text = re.sub(
        r"\[metadata\]",
        f"[metadata]\nversion = {os.environ['PKG_VERSION']}\n",
        setup_cfg_text
    )

    print(setup_cfg_text)

    setup_cfg.write_text(setup_cfg_text)
