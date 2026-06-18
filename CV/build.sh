#!/bin/bash

cd /cv

xelatex -interaction=nonstopmode main.tex

if [ -f "main.pdf" ]; then
    echo "main.pdf готов"

    mkdir -p /cv/output
    cp main.pdf /cv/output/

    echo "PDF скопирован в output/main.pdf"
else
    echo "Все поломалось :("
    exit 1
fi