#!/usr/bin/env bash

pdflatex main.tex
killall preview
open -a Preview main.pdf