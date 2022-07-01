#!/bin/sh
echo  "$(tput setaf 6)Welcome to c290 basics"
echo  "$(tput setaf 6)All credits to Johan Vos for this libraries strange and strangefx"

echo  "$(tput setaf 6)We will use this library to simulate quantum circuits in java"
echo  "$(tput setaf 6)cloning strange ..."
git clone https://github.com/redfx-quantum/strange
echo  "$(tput setaf 6)strange lib cloned!"
echo  "$(tput setaf 6)cloning strangefx ..."
git clone https://github.com/redfx-quantum/strangefx
echo  "$(tput setaf 6)strangefx cloned!"
echo  "$(tput setaf 6)executing strange"

cd strange
mvn package
cd ..
echo  "$(tput setaf 6)strange set!"
echo  "$(tput setaf 6)executin strangefx"
cd strangefx
mvn package 
cd ..
echo  "$(tput setaf 6)strangefx set!"
echo  "$(tput setaf 6)cloning the course material"
git clone https://github.com/johanvos/quantumjava
echo  "$(tput setaf 6)course cloned!"
echo  "$(tput setaf 6)testing"
echo  "$(tput setaf 6)compiling...."
javac SimpleStrangeDemo.java
echo  "$(tput setaf 6)compiled!"
echo  "$(tput setaf 6)executing..."


java SimpleStrangeDemo
echo  "$(tput setaf 6)executed!"
echo  "$(tput setaf 6)you are set"
