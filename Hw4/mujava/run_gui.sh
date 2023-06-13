# Note: this script did not modify mujava.config DIR

# gen mutant=mujava.gui.GenMutantsMain
# run test= mujava.gui.RunTestMain
sudo apt-get install openjdk-11-jdk
jar_path="/home/laxiflora/311551169-ST-2023/Hw4/mujava/include"
run_name="mujava.gui.RunTestMain"


java -cp $jar_path/mujava.jar:$jar_path/openjava.jar:$jar_path/tools.jar:$jar_path/hamcrest-core-1.3.jar:$jar_path/junit-4.12.jar $run_name