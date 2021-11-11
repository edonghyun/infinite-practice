#! /bin/bash

echo "Starts compile java files and execute main with problem number, test case"
if [ $# -ne 2 ]

  then
    echo "Usage: <PROBLEM NUMBER> <TEST TEXT PATH>"
    exit
fi

find . -name "*.java" -print | xargs javac 
java main.Main $1 $2

