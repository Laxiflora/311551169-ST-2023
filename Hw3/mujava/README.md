
[mujava官網](https://cs.gmu.edu/~offutt/mujava/)

# setup

請注意安裝openjdk-11-jdk
```
sudo apt-get install openjdk-11-jdk
```
將`mujava.jar`、`junit-4.12.jar`(不可是其他版本)、`openjava.jar`、`hamcrest-core-1.3.jar`加入CLASSPATH


# usage
透過下面指令產生mutants
```
java mujava.gui.GenMutantsMain
```
設計好test cases以後，透過下面指令執行testing
```
java mujava.gui.RunTestMain
```

如果跟我一樣設定CLASSPATH遭遇困難，可以使用簡單的script:
```
bash run_gui.sh
```
跑之前記得打開來決定要執行哪個mujava gui

# note
- 在產生好mutants之前，不要將編譯好的src file放到classes中，會造成錯誤，請先產生好mutants以後，跑測式前再放入
