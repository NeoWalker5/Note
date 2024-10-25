# 编译处理
# 环境准备
java18
ndk
Gradle 7.3.3

# 修改
- wrapper.properties
  distributionUrl=https\://services.gradle.org/distributions/gradle-7.3.3-bin.zip
- gradle.properties
    - # android.enableR8=false
- build.gradle
    classpath "com.android.tools.build:gradle:7.2.0"
    //apply plugin: 'android-aspectjx'