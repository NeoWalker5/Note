@echo off
setlocal enabledelayedexpansion

rem 循环处理每个拖放到脚本上的文件或文件夹路径
for %%A in (%*) do (
    rem 检查拖放的是文件还是文件夹
    if exist "%%A" (
        if exist "%%A\*.mp3" (
            rem 进入拖放的文件夹
            pushd "%%A"
            
            rem 循环处理文件夹中的每个MP3文件
            for %%F in (*.mp3) do (
                rem 构建输出文件名（使用相同名称，但更改扩展名为.wav）
                set "output_file=%%~nF.wav"
                
                rem 使用FFmpeg进行转换
                ffmpeg -i "%%F" -c:a pcm_s16le "!output_file!"
                
                echo Converted: %%F to !output_file!
            )
            
            rem 返回到原始目录
            popd
        ) else (
            echo No MP3 files found in the dragged folder: %%A
        )
    ) else (
        echo File or folder not found: %%A
    )
)

pause
