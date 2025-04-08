nuitka ^
  --onefile ^
  --standalone ^
  --include-data-file=assets/.env=assets/.env ^
  --windows-icon-from-ico=assets/goat-return.ico ^
  --output-dir=build ^
  --enable-plugin=tk-inter ^
  main.py
