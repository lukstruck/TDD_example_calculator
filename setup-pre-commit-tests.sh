echo "#!/bin/zsh
python -m unittest discover -s tests
" > .git/hooks/pre-commit-run-tests
chmod +x .git/hooks/pre-commit-run-tests
