make clean
if [ "$1" = "valgrind" ]
then
    make valgrind
elif [ "$1" = "asan" ]
then
    make asan
else
    echo -e "\nUsage: ./run.sh valgrind/asan (specify what you want to make).";
    exit
fi

FILES=$(find ./ -type f -executable | grep -v '\run.sh$')

for f in $FILES
do
    if [ "$1" = "valgrind" ]
    then
        echo "valgrind "$f" &> "$f".out"
        valgrind $f &> $f".out"
    else
        echo $f" &> "$f".out"
        $f &> $f".out"
    fi
done