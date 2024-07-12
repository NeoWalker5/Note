# sh权限
chmod ugo+x *
sudo

# 远程
vnc://10.0.32.160

# 显示隐藏文件/mac show hide file
defaults write com.apple.finder AppleShowAllFiles true

# 关闭进程/skillall finder
killall Finder

# Pod 
pod update
sudo gem update --system // 如果pod无法更新到最新
sudo gem uninstall cocoapods
sudo gem install cocoapods
pod --version