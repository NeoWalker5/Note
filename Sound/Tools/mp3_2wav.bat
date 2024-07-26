@echo off
setlocal enabledelayedexpansion

rem 设置FFmpeg路径（如果未添加到系统路径中）
set ffmpeg_path="D:\__FeiQWork\tools\FormatFactory\FFModules\Encoder\ffmpeg"

rem 获取拖放到脚本上的第一个参数作为文件夹路径
set folder_path=%1

rem 检查是否指定了文件夹路径
if not exist "%folder_path%" (
    echo Folder not found.
    exit /b
)

rem 检查文件夹是否包含MP3文件
if not exist "%folder_path%\*.mp3" (
    echo No MP3 files found in the folder.
    exit /b
)

rem 创建用于存储转换文件的新目录，与拖放的文件夹平级
set output_dir=%~dp1.\Converted_WAV
mkdir "%output_dir%"

rem 迭代文件夹中的每个MP3文件
for %%F in ("%folder_path%\*.mp3") do (
    rem 构建输出文件名（去除原始文件名的扩展名，并追加.wav）
    set "output_file=%output_dir%\%%~nF.wav"
    
    rem 使用FFmpeg进行转换
    %ffmpeg_path% -i "%%F" -c:a pcm_s16le "!output_file!"
    
    echo Converted: %%F to !output_file!
)

pause
