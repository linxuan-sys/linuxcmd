#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux 命令查询助手
作者：轩轩
功能：快速搜索、自动补全、详细说明
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GLib
import re
import os
import html
import json
import subprocess
import threading

# 配置
MANUAL_PATH = os.path.expanduser("~/桌面/Linux命令学习手册.txt")
CACHE_PATH = os.path.expanduser("~/桌面/.command_cache.json")

# 命令详细说明数据库（从网上整理）
COMMAND_DETAILS = {
    "spf": {
        "name": "spf (Superfile)",
        "description": "一个非常现代化和漂亮的终端文件管理器。使用键盘快捷键进行文件操作，支持多面板、文件预览、压缩解压等功能。",
        "category": "文件管理",
        "examples": [
            "spf                    # 启动 superfile 文件管理器",
            "spf /path/to/dir       # 在指定目录启动",
            "spf --help             # 查看帮助信息"
        ],
        "hotkeys": [
            "q / Esc        退出 superfile",
            "s              聚焦侧边栏",
            "p              聚焦进程面板",
            "m              聚焦元数据面板",
            "f              显示/隐藏预览窗口",
            "n              创建新文件面板",
            "w              关闭当前文件面板",
            "j / ↓         向下移动",
            "k / ↑         向上移动",
            "Enter / l      打开文件/进入目录",
            "h / Backspace  返回上级目录",
            "v              切换选择模式",
            "Ctrl+c         复制文件",
            "Ctrl+x         剪切文件",
            "Ctrl+v         粘贴文件",
            "Ctrl+d         删除文件",
            "Ctrl+n         新建文件/文件夹",
            "Ctrl+r         重命名",
            "Ctrl+a         压缩文件",
            "Ctrl+e         解压文件",
            "e              用编辑器打开文件",
            "/              搜索文件",
            ".              显示/隐藏隐藏文件",
            "P              固定目录到侧边栏",
            ":              打开命令执行栏",
            ">              打开 SPF 模式命令"
        ],
        "tips": [
            "安装方法：go install github.com/yorukot/superfile@latest",
            "也可以用包管理器安装：pip install superfile",
            "按 v 进入选择模式，可以批量操作文件",
            "支持多个文件面板，按 n 创建，Tab 切换"
        ]
    },
    "ls": {
        "name": "ls",
        "description": "列出目录内容。最常用的 Linux 命令之一，用于查看当前目录下的文件和子目录。",
        "category": "文件操作",
        "examples": [
            "ls                     # 列出当前目录内容",
            "ls -l                  # 长格式显示（权限、所有者、大小、时间）",
            "ls -la                 # 显示所有文件（包括隐藏文件）",
            "ls -lh                 # 人性化显示文件大小（KB, MB, GB）",
            "ls -la /home           # 列出指定目录内容",
            "ls -lt                 # 按修改时间排序（最新的在前）",
            "ls -lS                 # 按文件大小排序",
            "ls -lr                 # 反向排序",
            "ls -R                  # 递归列出子目录",
            "ls -F                  # 在目录后添加 / 标识",
            "ls -i                  # 显示 inode 号",
            "ls --color=auto        # 彩色显示不同类型文件"
        ],
        "options": [
            "-a, --all          显示所有文件，包括以 . 开头的隐藏文件",
            "-A, --almost-all   显示所有文件，但不包括 . 和 ..",
            "-l                 长格式显示，包含权限、链接数、所有者、组、大小、时间",
            "-h, --human-readable  以人类可读格式显示大小",
            "-r, --reverse      反向排序",
            "-t                 按修改时间排序",
            "-S                 按文件大小排序",
            "-R, --recursive    递归显示子目录",
            "-d, --directory    只显示目录本身，不显示内容",
            "-i, --inode        显示文件的 inode 号",
            "-F, --classify     在文件名后添加类型指示符（*/=>@|）",
            "--color=WHEN       设置颜色显示（never/always/auto）"
        ],
        "tips": [
            "常用组合：ls -lah（显示所有文件，长格式，人性化大小）",
            "可以组合多个选项：ls -lart（长格式、所有文件、反向、按时间）",
            "alias ll='ls -la' 可以设置别名方便使用"
        ]
    },
    "cd": {
        "name": "cd",
        "description": "切换当前工作目录。用于在文件系统中导航。",
        "category": "文件操作",
        "examples": [
            "cd /home/user          # 切换到指定目录",
            "cd                     # 切换到用户主目录",
            "cd ~                   # 切换到用户主目录",
            "cd ..                  # 切换到上一级目录",
            "cd ../..               # 切换到上两级目录",
            "cd -                   # 切换到上一个工作目录",
            "cd ~/Documents         # 切换到主目录下的 Documents",
            "cd /                   # 切换到根目录"
        ],
        "tips": [
            "cd - 非常有用，可以在两个目录之间快速切换",
            "使用 Tab 键可以自动补全目录名",
            "cd 不带参数直接回到主目录"
        ]
    },
    "cp": {
        "name": "cp",
        "description": "复制文件或目录。可以将文件从一个位置复制到另一个位置。",
        "category": "文件操作",
        "examples": [
            "cp file1.txt file2.txt           # 复制文件",
            "cp file.txt /path/to/dest/       # 复制文件到目录",
            "cp -r dir1/ dir2/                # 递归复制目录",
            "cp -p file1 file2                # 保留文件属性（权限、时间戳）",
            "cp -i file1 file2                # 交互模式，覆盖前确认",
            "cp -f file1 file2                # 强制覆盖，不提示",
            "cp -v file1 file2                # 显示详细过程",
            "cp -u file1 file2                # 只复制更新的文件",
            "cp -r dir1/ dir2/ --backup       # 备份已存在的文件",
            "cp file1.txt file2.txt dir/      # 复制多个文件到目录"
        ],
        "options": [
            "-r, -R, --recursive   递归复制目录及其内容",
            "-i, --interactive     覆盖前询问确认",
            "-f, --force           强制复制，覆盖不提示",
            "-v, --verbose         显示详细过程",
            "-p                    保留文件属性",
            "-u, --update          只复制源文件比目标新的文件",
            "-b, --backup          创建备份",
            "-s, --symbolic-link   创建符号链接而不复制"
        ],
        "tips": [
            "复制目录时必须使用 -r 选项",
            "cp -ri dir1/ dir2/ 可以安全地复制目录",
            "使用 -v 可以看到复制进度"
        ]
    },
    "mv": {
        "name": "mv",
        "description": "移动或重命名文件/目录。可以移动文件到另一个位置，也可以用来重命名文件。",
        "category": "文件操作",
        "examples": [
            "mv old.txt new.txt         # 重命名文件",
            "mv file.txt /path/to/dest/ # 移动文件到目录",
            "mv dir1/ dir2/             # 移动/重命名目录",
            "mv -i file1 file2          # 覆盖前确认",
            "mv -f file1 file2          # 强制覆盖",
            "mv -v file1 file2          # 显示详细过程",
            "mv -n file1 file2          # 不覆盖已存在文件",
            "mv *.txt /backup/          # 移动所有 txt 文件"
        ],
        "options": [
            "-i, --interactive     覆盖前询问确认",
            "-f, --force           强制移动，覆盖不提示",
            "-v, --verbose         显示详细过程",
            "-n, --no-clobber      不覆盖已存在的文件",
            "-u, --update          只移动比目标新的文件",
            "-b, --backup          创建备份"
        ],
        "tips": [
            "mv 既可以移动也可以重命名，取决于目标是否存在",
            "mv -i 可以避免意外覆盖文件",
            "移动目录不需要 -r 选项（与 cp 不同）"
        ]
    },
    "rm": {
        "name": "rm",
        "description": "删除文件或目录。小心使用，删除后文件很难恢复！",
        "category": "文件操作",
        "examples": [
            "rm file.txt              # 删除文件",
            "rm -r directory          # 递归删除目录",
            "rm -rf directory         # 强制递归删除目录（不提示）",
            "rm -i file.txt           # 删除前确认",
            "rm -v file.txt           # 显示删除过程",
            "rm -f file.txt           # 强制删除，忽略不存在文件",
            "rm *.log                 # 删除所有 .log 文件",
            "rm -rf /tmp/test/*       # 删除目录内容但保留目录"
        ],
        "options": [
            "-r, -R, --recursive   递归删除目录及其内容",
            "-f, --force           强制删除，不提示确认",
            "-i, --interactive     删除前逐一确认",
            "-v, --verbose         显示删除过程",
            "-d, --dir             删除空目录",
            "--no-preserve-root    不特别对待 / 根目录",
            "--preserve-root[=all]  不递归删除根目录（默认）"
        ],
        "tips": [
            "⚠️ rm -rf / 会删除整个系统，绝对不要执行！",
            "删除前可以用 ls 先确认文件",
            "alias rm='rm -i' 可以增加安全保护",
            "重要文件删除前先备份"
        ]
    },
    "mkdir": {
        "name": "mkdir",
        "description": "创建新目录。可以创建单个目录或多级嵌套目录。",
        "category": "文件操作",
        "examples": [
            "mkdir newdir                # 创建新目录",
            "mkdir -p path/to/dir        # 创建多级目录",
            "mkdir -v newdir             # 显示创建过程",
            "mkdir -m 755 newdir         # 设置目录权限",
            "mkdir dir1 dir2 dir3        # 同时创建多个目录",
            "mkdir -p project/{src,bin,docs}  # 创建项目结构"
        ],
        "options": [
            "-p, --parents    创建父目录，不报错已存在目录",
            "-v, --verbose    显示创建过程",
            "-m, --mode=MODE  设置目录权限（如 755）"
        ],
        "tips": [
            "创建多级目录必须用 -p，如 mkdir -p a/b/c/d",
            "可以用花括号批量创建：mkdir {dir1,dir2,dir3}",
            "-m 可以直接设置权限，不用再 chmod"
        ]
    },
    "cat": {
        "name": "cat",
        "description": "连接并显示文件内容。可以查看文件内容，也可以合并多个文件。",
        "category": "文件操作",
        "examples": [
            "cat file.txt              # 显示文件内容",
            "cat file1 file2           # 显示多个文件内容",
            "cat -n file.txt           # 显示行号",
            "cat -b file.txt           # 显示行号（空行不计）",
            "cat -s file.txt           # 合并连续空行",
            "cat file1 file2 > merged  # 合并文件到新文件",
            "cat > newfile.txt         # 创建新文件（Ctrl+D 结束）",
            "cat << EOF > file.txt     # Here document 创建文件",
            "cat -A file.txt           # 显示所有特殊字符"
        ],
        "options": [
            "-n, --number          显示行号",
            "-b, --number-nonblank 显示行号（空行不计）",
            "-s, --squeeze-blank   合并连续空行为一行",
            "-A, --show-all        显示所有字符（相当于 -vET）",
            "-E, --show-ends       行尾显示 $",
            "-T, --show-tabs       显示 Tab 为 ^I"
        ],
        "tips": [
            "大文件建议用 less 或 more 分页查看",
            "cat 可以快速创建简单文件",
            "cat /dev/null > file 可以清空文件内容"
        ]
    },
    "grep": {
        "name": "grep",
        "description": "搜索文本模式。在文件中搜索匹配的行，是最强大的文本搜索工具之一。",
        "category": "文本处理",
        "examples": [
            "grep 'pattern' file.txt         # 在文件中搜索模式",
            "grep -i 'pattern' file.txt      # 忽略大小写搜索",
            "grep -r 'pattern' /path/        # 递归搜索目录",
            "grep -n 'pattern' file.txt      # 显示行号",
            "grep -v 'pattern' file.txt      # 显示不匹配的行",
            "grep -c 'pattern' file.txt      # 只显示匹配行数",
            "grep -l 'pattern' *.txt         # 只显示匹配的文件名",
            "grep -A 3 'pattern' file.txt    # 显示匹配行及后3行",
            "grep -B 3 'pattern' file.txt    # 显示匹配行及前3行",
            "grep -C 3 'pattern' file.txt    # 显示匹配行及前后各3行",
            "grep -E 'regex' file.txt        # 使用扩展正则表达式",
            "grep --color=auto 'pattern' f   # 彩色高亮匹配",
            "ps aux | grep nginx             # 在进程列表中搜索",
            "grep -rn 'function' ./          # 递归搜索并显示行号"
        ],
        "options": [
            "-i, --ignore-case    忽略大小写",
            "-v, --invert-match   显示不匹配的行",
            "-n, --line-number    显示行号",
            "-r, --recursive      递归搜索目录",
            "-l, --files-with-matches  只显示匹配的文件名",
            "-c, --count          只显示匹配行数",
            "-A NUM, --after-context=NUM  显示匹配行后 NUM 行",
            "-B NUM, --before-context=NUM 显示匹配行前 NUM 行",
            "-C NUM, --context=NUM        显示匹配行前后各 NUM 行",
            "-E, --extended-regexp  使用扩展正则表达式",
            "-w, --word-regexp    匹配整个单词",
            "-x, --line-regexp    匹配整行"
        ],
        "tips": [
            "grep -rn 是代码搜索的神器",
            "配合管道使用：cat log | grep error",
            "alias grep='grep --color=auto' 彩色显示结果"
        ]
    },
    "find": {
        "name": "find",
        "description": "搜索文件和目录。功能强大的文件查找工具，支持按名称、大小、时间等多种条件搜索。",
        "category": "文件操作",
        "examples": [
            "find . -name '*.txt'              # 按名称查找",
            "find /home -name 'file.txt'       # 在指定目录查找",
            "find . -type d                    # 只查找目录",
            "find . -type f                    # 只查找文件",
            "find . -size +100M                # 查找大于100M的文件",
            "find . -size -1k                  # 查找小于1k的文件",
            "find . -mtime -7                  # 7天内修改的文件",
            "find . -mtime +30                 # 30天前修改的文件",
            "find . -user root                 # 按所有者查找",
            "find . -perm 755                  # 按权限查找",
            "find . -empty                     # 查找空文件/目录",
            "find . -name '*.log' -delete      # 查找并删除",
            "find . -exec chmod 644 {} \;     # 对结果执行命令",
            "find . -name '*.txt' | xargs rm   # 配合xargs使用"
        ],
        "options": [
            "-name PATTERN    按文件名查找（支持通配符）",
            "-iname PATTERN   按文件名查找（忽略大小写）",
            "-type TYPE       按类型查找（f文件,d目录,l链接）",
            "-size N          按大小查找（+大于,-小于,c字节,k,kB,M,MB）",
            "-mtime N         按修改时间查找（+N天前,-N天内）",
            "-atime N         按访问时间查找",
            "-user NAME       按所有者查找",
            "-group NAME      按组查找",
            "-perm MODE       按权限查找",
            "-empty           查找空文件/目录",
            "-maxdepth N      最大搜索深度",
            "-delete          删除找到的文件"
        ],
        "tips": [
            "find . -name '*.txt' 2>/dev/null 忽略权限错误",
            "-exec 后面的命令以 \; 结尾",
            "配合 xargs 处理大量文件更高效",
            "用 -maxdepth 限制搜索深度提高速度"
        ]
    },
    "chmod": {
        "name": "chmod",
        "description": "修改文件或目录权限。控制谁可以读取、写入或执行文件。",
        "category": "文件操作",
        "examples": [
            "chmod 755 file.sh         # 设置权限（数字模式）",
            "chmod +x script.sh        # 添加执行权限",
            "chmod -x script.sh        # 移除执行权限",
            "chmod u+r file            # 所有者添加读权限",
            "chmod g-w file            # 组移除写权限",
            "chmod o+r file            # 其他人添加读权限",
            "chmod a+x file            # 所有人添加执行权限",
            "chmod -R 755 directory/   # 递归修改目录权限",
            "chmod u=rwx,g=rx,o=r file # 同时设置多组权限",
            "chmod +x $(which script)  # 使脚本可执行"
        ],
        "options": [
            "-R, --recursive   递归修改目录及其内容",
            "-v, --verbose     显示修改过程",
            "-c, --changes     只显示实际修改的内容",
            "-f, --silent      不显示错误信息"
        ],
        "tips": [
            "数字模式：r=4, w=2, x=1，所以 755 = rwxr-xr-x",
            "chmod +x 是最常用的，使脚本可执行",
            "目录通常设为 755，文件通常设为 644",
            "敏感文件设为 600（只有所有者可读写）"
        ]
    },
    "chown": {
        "name": "chown",
        "description": "修改文件或目录的所有者和所属组。需要 root 权限才能修改。",
        "category": "文件操作",
        "examples": [
            "chown user file               # 修改所有者",
            "chown user:group file         # 修改所有者和组",
            "chown :group file             # 只修改组",
            "chown -R user:group directory # 递归修改",
            "chown --reference=ref file    # 参照另一文件设置",
            "sudo chown root:root file     # 设置为 root 所有"
        ],
        "options": [
            "-R, --recursive      递归修改",
            "-v, --verbose        显示修改过程",
            "-c, --changes        只显示实际修改的内容",
            "--reference=RFILE    参照另一文件的设置",
            "--from=CURRENT_OWNER:GROUP  只修改匹配的文件"
        ],
        "tips": [
            "需要 sudo 权限才能修改所有者",
            "chown user: file 可以同时修改所有者和组",
            "常用：sudo chown -R $USER:$USER ~/project"
        ]
    },
    "tar": {
        "name": "tar",
        "description": "打包和压缩文件。可以创建、解压 tar 归档文件，支持 gzip、bzip2 等压缩格式。",
        "category": "压缩解压",
        "examples": [
            "tar -cvf archive.tar files/       # 创建 tar 包",
            "tar -czvf archive.tar.gz files/   # 创建 gzip 压缩包",
            "tar -cjvf archive.tar.bz2 files/  # 创建 bzip2 压缩包",
            "tar -xvf archive.tar              # 解压 tar 包",
            "tar -xzvf archive.tar.gz          # 解压 gzip 包",
            "tar -xjvf archive.tar.bz2         # 解压 bzip2 包",
            "tar -tvf archive.tar              # 查看包内容",
            "tar -xzvf archive.tar.gz -C /dir/ # 解压到指定目录",
            "tar -rvf archive.tar newfile      # 追加文件到包",
            "tar --exclude='*.log' -czvf a.tar.gz dir/  # 排除文件"
        ],
        "options": [
            "-c, --create     创建新归档",
            "-x, --extract    解压归档",
            "-t, --list       列出归档内容",
            "-v, --verbose    显示详细过程",
            "-f, --file=FILE  指定归档文件名",
            "-z, --gzip       使用 gzip 压缩/解压",
            "-j, --bzip2      使用 bzip2 压缩/解压",
            "-J, --xz         使用 xz 压缩/解压",
            "-C, --directory=DIR  解压到指定目录",
            "--exclude=PATTERN    排除匹配的文件",
            "-r, --append     追加文件到归档"
        ],
        "tips": [
            "记忆口诀：-czvf 压缩，-xzvf 解压",
            "常用：tar -czvf backup.tar.gz folder/",
            "查看不解压：tar -tvf file.tar.gz",
            "压缩比：xz > bzip2 > gzip（速度反之）"
        ]
    },
    "ps": {
        "name": "ps",
        "description": "显示当前运行的进程。可以查看进程状态、PID、资源使用等信息。",
        "category": "进程管理",
        "examples": [
            "ps                    # 显示当前终端进程",
            "ps aux                # 显示所有进程详细信息",
            "ps -ef                # 显示所有进程（完整格式）",
            "ps aux | grep nginx   # 搜索特定进程",
            "ps -u username        # 显示指定用户的进程",
            "ps --forest           # 树状显示进程",
            "ps -e --forest        # 树状显示所有进程",
            "ps aux --sort=-%mem   # 按内存使用排序",
            "ps aux --sort=-%cpu   # 按 CPU 使用排序",
            "ps -p PID             # 显示指定 PID 的进程",
            "ps -o pid,ppid,cmd    # 自定义显示列"
        ],
        "options": [
            "-a              显示所有终端进程",
            "-u              显示用户导向格式",
            "-x              显示无终端进程",
            "-e, -A          显示所有进程",
            "-f              完整格式显示",
            "--forest        树状显示",
            "--sort=SPEC     排序（-表示降序）",
            "-o, --format    自定义输出格式",
            "-p PID          指定进程 ID",
            "-U USER         指定用户"
        ],
        "tips": [
            "ps aux 是最常用的组合",
            "配合 grep 查找进程：ps aux | grep name",
            "按内存排序：ps aux --sort=-%mem | head",
            "查看进程树：ps -ef --forest"
        ]
    },
    "kill": {
        "name": "kill",
        "description": "终止进程。向进程发送信号，通常用于结束进程。",
        "category": "进程管理",
        "examples": [
            "kill PID              # 发送 TERM 信号（优雅终止）",
            "kill -9 PID           # 发送 KILL 信号（强制终止）",
            "kill -15 PID          # 发送 TERM 信号（同默认）",
            "kill -l               # 列出所有信号",
            "kill -HUP PID         # 重新加载配置",
            "kill -STOP PID        # 暂停进程",
            "kill -CONT PID        # 继续进程",
            "killall nginx         # 按名称终止进程",
            "pkill -f 'python'     # 按命令行匹配终止",
            "kill $(pgrep -f app)  # 终止匹配的所有进程"
        ],
        "options": [
            "-s, --signal SIGNAL  发送指定信号",
            "-l, --list           列出所有信号名",
            "-9, -KILL            强制终止（SIGKILL）",
            "-15, -TERM           优雅终止（默认）",
            "-1, -HUP             挂起/重新加载",
            "-2, -INT             中断（Ctrl+C）",
            "-19, -STOP           暂停进程",
            "-18, -CONT           继续进程"
        ],
        "tips": [
            "先用 ps 或 pgrep 找到 PID",
            "优先用 kill PID（优雅终止），不行再用 kill -9",
            "kill -9 可能导致数据丢失",
            "killall 可以批量终止同名进程"
        ]
    },
    "top": {
        "name": "top",
        "description": "实时显示系统进程和资源使用情况。交互式的系统监控工具。",
        "category": "系统监控",
        "examples": [
            "top                   # 启动 top",
            "top -u username       # 只显示指定用户进程",
            "top -p PID1,PID2      # 只显示指定进程",
            "top -d 5              # 设置刷新间隔为5秒",
            "top -b -n 1           # 批处理模式，输出一次",
            "top -H                # 显示线程"
        ],
        "hotkeys": [
            "q              退出 top",
            "h              显示帮助",
            "k              终止进程（输入 PID）",
            "r              修改优先级",
            "M              按内存排序",
            "P              按 CPU 排序（默认）",
            "T              按时间排序",
            "c              显示完整命令行",
            "1              显示各 CPU 核心",
            "u              过滤用户",
            "z              彩色显示",
            "x              高亮排序列"
        ],
        "tips": [
            "按 M 切换到内存排序",
            "按 P 切换回 CPU 排序",
            "按 1 可以看到每个 CPU 核心的使用情况",
            "htop 是增强版，更好用"
        ]
    },
    "df": {
        "name": "df",
        "description": "显示磁盘空间使用情况。查看文件系统的磁盘空间和 inode 使用。",
        "category": "磁盘管理",
        "examples": [
            "df                  # 显示所有文件系统",
            "df -h               # 人性化显示大小",
            "df -T               # 显示文件系统类型",
            "df -i               # 显示 inode 使用情况",
            "df -a               # 显示所有文件系统（包括虚拟）",
            "df -x tmpfs         # 排除指定类型",
            "df -t ext4          # 只显示指定类型",
            "df /home            # 显示指定目录所在分区"
        ],
        "options": [
            "-h, --human-readable  以人类可读格式显示",
            "-H, --si              使用 1000 而非 1024",
            "-T, --print-type      显示文件系统类型",
            "-i, --inodes          显示 inode 信息",
            "-a, --all             显示所有文件系统",
            "-t, --type=TYPE       只显示指定类型",
            "-x, --exclude-type=TYPE  排除指定类型",
            "--total               显示总计"
        ],
        "tips": [
            "df -h 是最常用的",
            "配合 grep 过滤：df -h | grep -v tmpfs",
            "df -h / 可以快速查看根分区空间"
        ]
    },
    "du": {
        "name": "du",
        "description": "显示目录或文件大小。查看指定目录或文件的磁盘使用量。",
        "category": "磁盘管理",
        "examples": [
            "du                      # 显示当前目录大小",
            "du -h                   # 人性化显示大小",
            "du -sh *                # 显示每个子目录大小",
            "du -sh directory        # 显示目录总大小",
            "du -h --max-depth=1     # 只显示一层深度",
            "du -ah                  # 显示所有文件大小",
            "du -sh * | sort -h      # 按大小排序",
            "du -sh /var/* 2>/dev/null # 忽略权限错误",
            "du -h --time            # 显示修改时间"
        ],
        "options": [
            "-h, --human-readable  人性化显示",
            "-s, --summarize       只显示总计",
            "-a, --all             显示所有文件",
            "-d, --max-depth=N     显示 N 层深度",
            "--exclude=PATTERN     排除匹配的文件",
            "--time                显示最后修改时间",
            "-c, --total           显示总计"
        ],
        "tips": [
            "du -sh * 查看当前目录下各子目录大小",
            "配合 sort：du -sh * | sort -h",
            "找出大目录：du -h --max-depth=1 | sort -hr | head"
        ]
    },
    "sudo": {
        "name": "sudo",
        "description": "以超级用户或其他用户身份执行命令。临时获取 root 权限。",
        "category": "系统管理",
        "examples": [
            "sudo command            # 以 root 执行命令",
            "sudo -u user command    # 以指定用户执行",
            "sudo -i                 # 切换到 root shell",
            "sudo -s                 # 使用当前用户的 shell",
            "sudo -l                 # 列出可执行的命令",
            "sudo -k                 # 清除缓存密码",
            "sudo -v                 # 验证密码（延长超时）",
            "sudo !!                 # 以 root 重复上一条命令"
        ],
        "options": [
            "-u, --user=USER   以指定用户执行",
            "-i, --login       登录 shell（加载环境）",
            "-s, --shell       使用当前 shell",
            "-l, --list        列出权限",
            "-v, --validate    验证/更新密码时间戳",
            "-k, --reset-timestamp  清除密码时间戳",
            "-b, --background  后台执行"
        ],
        "tips": [
            "sudo !! 可以快速以 root 重复上一条命令",
            "sudo -i 可以进入 root shell",
            "配置文件在 /etc/sudoers，用 visudo 编辑"
        ]
    },
    "systemctl": {
        "name": "systemctl",
        "description": "控制系统和服务管理器。用于管理 systemd 系统和服务。",
        "category": "系统管理",
        "examples": [
            "systemctl start service       # 启动服务",
            "systemctl stop service        # 停止服务",
            "systemctl restart service     # 重启服务",
            "systemctl status service      # 查看服务状态",
            "systemctl enable service      # 设置开机启动",
            "systemctl disable service     # 禁止开机启动",
            "systemctl list-units          # 列出所有单元",
            "systemctl list-units --type=service  # 列出所有服务",
            "systemctl daemon-reload       # 重新加载配置",
            "systemctl reboot              # 重启系统",
            "systemctl poweroff            # 关机",
            "systemctl suspend             # 挂起",
            "journalctl -u service         # 查看服务日志"
        ],
        "options": [
            "start       启动服务",
            "stop        停止服务",
            "restart     重启服务",
            "status      查看状态",
            "enable      设置开机启动",
            "disable     禁止开机启动",
            "is-active   检查是否运行中",
            "is-enabled  检查是否开机启动",
            "list-units  列出所有单元",
            "daemon-reload  重新加载配置文件"
        ],
        "tips": [
            "修改服务配置后要执行 daemon-reload",
            "systemctl status 查看服务是否正常运行",
            "用 enable/disable 控制开机启动"
        ]
    },
    "dnf": {
        "name": "dnf",
        "description": "Fedora/RHEL 的包管理器。用于安装、更新、删除软件包。",
        "category": "包管理",
        "examples": [
            "dnf update              # 更新所有包",
            "dnf upgrade             # 升级所有包",
            "dnf install package     # 安装软件包",
            "dnf remove package      # 删除软件包",
            "dnf search keyword      # 搜索软件包",
            "dnf info package        # 显示软件包信息",
            "dnf list installed      # 列出已安装的包",
            "dnf autoremove          # 删除不需要的依赖",
            "dnf clean all           # 清理缓存",
            "dnf history             # 查看操作历史",
            "dnf groupinstall 'Group Name'  # 安装软件组",
            "dnf provides /bin/ls    # 查找文件属于哪个包"
        ],
        "options": [
            "update/upgrade  更新包",
            "install         安装包",
            "remove          删除包",
            "search          搜索包",
            "info            显示包信息",
            "list            列出包",
            "autoremove      自动删除依赖",
            "clean           清理缓存",
            "provides        查找文件所属包",
            "-y              自动确认"
        ],
        "tips": [
            "dnf 是 yum 的升级版",
            "dnf update -y 可以一键更新系统",
            "dnf provides /usr/bin/cmd 可以找命令属于哪个包"
        ]
    },
    "git": {
        "name": "git",
        "description": "分布式版本控制系统。用于代码版本管理和协作开发。",
        "category": "版本控制",
        "examples": [
            "git init                    # 初始化仓库",
            "git clone url               # 克隆远程仓库",
            "git status                  # 查看状态",
            "git add .                   # 添加所有更改",
            "git add file.txt            # 添加指定文件",
            "git commit -m 'message'     # 提交更改",
            "git push origin main        # 推送到远程",
            "git pull origin main        # 拉取远程更新",
            "git branch feature          # 创建分支",
            "git checkout feature        # 切换分支",
            "git checkout -b feature     # 创建并切换分支",
            "git merge feature           # 合并分支",
            "git log --oneline           # 简洁日志",
            "git diff                    # 查看差异",
            "git stash                   # 暂存更改",
            "git stash pop               # 恢复暂存"
        ],
        "options": [
            "init        初始化仓库",
            "clone       克隆仓库",
            "status      查看状态",
            "add         添加到暂存区",
            "commit      提交更改",
            "push        推送到远程",
            "pull        拉取更新",
            "branch      分支管理",
            "checkout    切换分支",
            "merge       合并分支",
            "log         查看日志",
            "diff        查看差异",
            "stash       暂存更改"
        ],
        "tips": [
            "git status 经常用，随时查看状态",
            "git add . + git commit -m 'msg' 常用组合",
            "git log --oneline --graph 更直观的日志"
        ]
    },
    "ssh": {
        "name": "ssh",
        "description": "安全远程连接。通过加密通道连接远程服务器。",
        "category": "网络工具",
        "examples": [
            "ssh user@host               # 连接远程主机",
            "ssh -p 2222 user@host       # 指定端口连接",
            "ssh -i key.pem user@host    # 使用密钥连接",
            "ssh -L 8080:localhost:80 user@host  # 本地端口转发",
            "ssh -R 8080:localhost:80 user@host  # 远程端口转发",
            "ssh -D 1080 user@host       # SOCKS 代理",
            "ssh-copy-id user@host       # 复制公钥到服务器",
            "ssh-keygen                  # 生成密钥对",
            "ssh -J jump_host dest_host  # 跳板机连接"
        ],
        "options": [
            "-p PORT         指定端口",
            "-i IDENTITY     指定密钥文件",
            "-L [bind:]port:host:hostport  本地转发",
            "-R [bind:]port:host:hostport  远程转发",
            "-D [bind:]port  动态转发（SOCKS代理）",
            "-J JUMP_HOST    跳板机",
            "-v              详细输出（调试）",
            "-N              不执行远程命令",
            "-f              后台运行"
        ],
        "tips": [
            "ssh-keygen 生成密钥，ssh-copy-id 复制到服务器",
            "~/.ssh/config 可以配置主机别名",
            "ssh -v 可以调试连接问题"
        ]
    },
    "curl": {
        "name": "curl",
        "description": "命令行网络工具。用于传输数据，支持多种协议。",
        "category": "网络工具",
        "examples": [
            "curl https://example.com         # 获取网页",
            "curl -O https://example.com/file # 下载文件",
            "curl -o file.txt URL             # 保存为指定文件名",
            "curl -I https://example.com      # 只获取响应头",
            "curl -X POST -d 'data' URL       # POST 请求",
            "curl -H 'Content-Type: json' URL # 添加请求头",
            "curl -u user:pass URL            # 基本认证",
            "curl -L URL                      # 跟随重定向",
            "curl -x proxy:port URL           # 使用代理",
            "curl -F 'file=@local.txt' URL    # 上传文件",
            "curl --cookie 'key=value' URL    # 发送 cookie",
            "curl -s URL                      # 静默模式",
            "curl -w '%{http_code}' URL       # 显示 HTTP 状态码"
        ],
        "options": [
            "-O              使用远程文件名保存",
            "-o FILE         保存为指定文件名",
            "-I, --head      只获取响应头",
            "-X METHOD       指定请求方法",
            "-d DATA         发送数据",
            "-H HEADER       添加请求头",
            "-u USER:PASS    基本认证",
            "-L, --location  跟随重定向",
            "-x PROXY        使用代理",
            "-s, --silent    静默模式",
            "-v, --verbose   详细输出"
        ],
        "tips": [
            "curl -I 快速检查网站状态",
            "curl -L 跟随重定向",
            "curl -s 静默模式不显示进度"
        ]
    },
    "python3": {
        "name": "python3",
        "description": "Python 编程语言解释器。用于运行 Python 程序。",
        "category": "编程开发",
        "examples": [
            "python3 script.py           # 运行 Python 脚本",
            "python3 -m module           # 运行模块",
            "python3 -c 'print(1+1)'     # 执行单行代码",
            "python3 -i script.py        # 运行后进入交互模式",
            "python3 -m venv myenv       # 创建虚拟环境",
            "python3 -m pip install pkg  # 安装包",
            "python3 --version           # 查看版本",
            "python3 -m http.server 8000 # 启动 HTTP 服务器"
        ],
        "options": [
            "-c CMD         执行单行代码",
            "-m MODULE      运行模块",
            "-i             运行后进入交互模式",
            "-V, --version  显示版本",
            "-h, --help     显示帮助",
            "-u             无缓冲输出",
            "-O             优化（移除 assert）",
            "-OO            进一步优化"
        ],
        "tips": [
            "python3 -m http.server 可以快速启动 HTTP 服务器",
            "python3 -m venv 创建虚拟环境",
            "python3 -c 'code' 快速执行一行代码"
        ]
    },
    "pip": {
        "name": "pip",
        "description": "Python 包管理器。用于安装和管理 Python 包。",
        "category": "编程开发",
        "examples": [
            "pip install package          # 安装包",
            "pip install package==1.0.0   # 安装指定版本",
            "pip install -r requirements.txt  # 从文件安装",
            "pip uninstall package        # 卸载包",
            "pip list                     # 列出已安装的包",
            "pip show package             # 显示包信息",
            "pip search keyword           # 搜索包",
            "pip freeze > requirements.txt # 导出依赖",
            "pip install --upgrade package # 升级包",
            "pip install -e .             # 开发模式安装",
            "pip config set global.index-url URL  # 设置镜像源"
        ],
        "options": [
            "install        安装包",
            "uninstall      卸载包",
            "list           列出已安装",
            "show           显示包信息",
            "freeze         导出依赖",
            "search         搜索包",
            "config         配置",
            "-r FILE        从文件安装",
            "--upgrade/-U   升级",
            "--user         安装到用户目录",
            "-i URL         使用镜像源"
        ],
        "tips": [
            "pip install -r requirements.txt 批量安装依赖",
            "pip freeze > requirements.txt 导出依赖",
            "使用国内镜像加速：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple"
        ]
    },
    "vim": {
        "name": "vim",
        "description": "强大的文本编辑器。支持多种模式的编辑器，是 Linux 系统必备工具。",
        "category": "文本编辑",
        "examples": [
            "vim file.txt          # 打开/创建文件",
            "vim +10 file.txt      # 打开并跳到第10行",
            "vim +/pattern file.txt # 打开并跳到匹配处",
            "vim -R file.txt       # 只读模式",
            "vimdiff file1 file2   # 比较两个文件",
            "vim -b file           # 二进制模式"
        ],
        "hotkeys": [
            "i              进入插入模式",
            "Esc            返回普通模式",
            ":w             保存",
            ":q             退出",
            ":wq            保存并退出",
            ":q!            强制退出不保存",
            "dd             删除一行",
            "yy             复制一行",
            "p              粘贴",
            "u              撤销",
            "Ctrl+r         重做",
            "/pattern       向下搜索",
            "?pattern       向上搜索",
            "n              下一个匹配",
            "N              上一个匹配",
            ":s/old/new/g   当前行替换",
            ":%s/old/new/g  全局替换",
            ":set number    显示行号",
            "G              跳到文件末尾",
            "gg             跳到文件开头",
            ":10            跳到第10行"
        ],
        "tips": [
            "按 i 进入插入模式，Esc 返回普通模式",
            "输入 :wq 保存退出，:q! 不保存强制退出",
            "vimtutor 命令可以学习 vim 教程"
        ]
    },
    "nano": {
        "name": "nano",
        "description": "简单易用的文本编辑器。适合初学者，操作简单直观。",
        "category": "文本编辑",
        "examples": [
            "nano file.txt         # 打开/创建文件",
            "nano -l file.txt      # 显示行号",
            "nano -m file.txt      # 启用鼠标",
            "nano -B file.txt      # 备份原文件",
            "nano +10 file.txt     # 打开并跳到第10行",
            "nano -w file.txt      # 不自动换行"
        ],
        "hotkeys": [
            "Ctrl+O         保存",
            "Ctrl+X         退出",
            "Ctrl+K         剪切",
            "Ctrl+U         粘贴",
            "Ctrl+W         搜索",
            "Ctrl+\        替换",
            "Ctrl+C         显示光标位置",
            "Ctrl+_         跳到指定行",
            "Alt+/          跳到文件末尾",
            "Ctrl+G         显示帮助"
        ],
        "tips": [
            "底部显示快捷键，^ 表示 Ctrl，M- 表示 Alt",
            "Ctrl+O 保存，Ctrl+X 退出",
            "比 vim 简单，适合快速编辑"
        ]
    },
    "man": {
        "name": "man",
        "description": "查看命令手册。显示命令的详细帮助文档。",
        "category": "帮助工具",
        "examples": [
            "man ls               # 查看 ls 命令手册",
            "man 5 passwd         # 查看指定章节",
            "man -k keyword       # 搜索手册页",
            "man -f command       # 显示命令简介",
            "man -a command       # 显示所有匹配的手册",
            "man -w command       # 显示手册文件位置"
        ],
        "options": [
            "-k KEYWORD     搜索手册（apropos）",
            "-f COMMAND     显示简介（whatis）",
            "-a             显示所有匹配",
            "-w             显示文件位置",
            "章节号：",
            "1              用户命令",
            "2              系统调用",
            "3              库函数",
            "4              特殊文件",
            "5              文件格式",
            "6              游戏",
            "7              杂项",
            "8              系统管理命令"
        ],
        "tips": [
            "man 是最权威的命令文档",
            "按 / 可以搜索，q 退出",
            "man -k keyword 可以搜索不知道名字的命令"
        ]
    },
    "history": {
        "name": "history",
        "description": "显示命令历史。查看和管理之前执行过的命令。",
        "category": "Shell工具",
        "examples": [
            "history              # 显示所有历史",
            "history 20           # 显示最近20条",
            "!100                 # 执行第100条命令",
            "!!                   # 执行上一条命令",
            "!ls                  # 执行最近的 ls 命令",
            "!$                   # 使用上一条命令的最后一个参数",
            "history -c           # 清空历史",
            "history -d 10        # 删除第10条历史",
            "Ctrl+R               # 反向搜索历史"
        ],
        "options": [
            "-c             清空历史",
            "-d OFFSET      删除指定条目",
            "-a             追加到历史文件",
            "-r             读取历史文件",
            "-w             写入历史文件",
            "!N             执行第N条命令",
            "!!             执行上一条",
            "!string        执行最近匹配的命令"
        ],
        "tips": [
            "Ctrl+R 可以搜索历史命令",
            "!! 重复上一条命令",
            "!$ 使用上一条命令的最后一个参数"
        ]
    },
    "alias": {
        "name": "alias",
        "description": "设置命令别名。为常用命令创建简短的别名。",
        "category": "Shell工具",
        "examples": [
            "alias                     # 显示所有别名",
            "alias ll='ls -la'         # 设置别名",
            "alias la='ls -A'          # 设置别名",
            "alias ..='cd ..'          # 设置别名",
            "alias cls='clear'         # 设置别名",
            "alias grep='grep --color=auto'  # 带颜色的 grep",
            "unalias ll                # 删除别名",
            "alias ll                  # 查看特定别名"
        ],
        "options": [
            "alias NAME='COMMAND'    设置别名",
            "alias                   显示所有别名",
            "alias NAME              显示特定别名",
            "unalias NAME            删除别名"
        ],
        "tips": [
            "别名定义放在 ~/.bashrc 中永久生效",
            "alias ll='ls -la' 是最常见的别名",
            "用单引号避免特殊字符问题"
        ]
    },
    "echo": {
        "name": "echo",
        "description": "输出文本。在终端显示文本或变量值。",
        "category": "Shell工具",
        "examples": [
            "echo 'Hello World'        # 输出文本",
            "echo $HOME                # 输出变量",
            "echo -n 'No newline'      # 不换行",
            "echo -e 'Line1\\nLine2'   # 解析转义字符",
            "echo *                    # 输出当前目录文件",
            "echo {1..10}              # 输出序列",
            "echo 'text' > file.txt    # 输出重定向到文件",
            "echo 'text' >> file.txt   # 追加到文件"
        ],
        "options": [
            "-n             不输出末尾换行",
            "-e             启用转义字符解析",
            "-E             禁用转义字符（默认）",
            "转义字符：",
            "\\n            换行",
            "\\t            制表符",
            "\\\\            反斜杠",
            "\\r            回车"
        ],
        "tips": [
            "echo -e 支持转义字符",
            "echo $VAR 输出变量值",
            "配合 > 和 >> 进行输出重定向"
        ]
    },
    "export": {
        "name": "export",
        "description": "设置环境变量。将变量导出为环境变量，使其对子进程可见。",
        "category": "Shell工具",
        "examples": [
            "export VAR=value         # 设置环境变量",
            "export PATH=$PATH:/new/path  # 添加到 PATH",
            "export -n VAR            # 取消导出",
            "export -p                # 显示所有导出变量",
            "export JAVA_HOME=/usr/java  # 设置 JAVA_HOME",
            "export LANG=en_US.UTF-8  # 设置语言"
        ],
        "options": [
            "-n             取消导出",
            "-p             显示所有导出变量",
            "-f             导出函数"
        ],
        "tips": [
            "环境变量放在 ~/.bashrc 或 ~/.profile 中永久生效",
            "export PATH=$PATH:/new/path 是常用操作",
            "env 命令可以查看所有环境变量"
        ]
    },
    "source": {
        "name": "source",
        "description": "在当前 shell 执行脚本。使脚本中的变量和函数在当前 shell 生效。",
        "category": "Shell工具",
        "examples": [
            "source script.sh         # 执行脚本",
            ". script.sh              # 同上（简写）",
            "source ~/.bashrc         # 重新加载配置",
            "source venv/bin/activate # 激活虚拟环境"
        ],
        "tips": [
            ". 是 source 的简写",
            "修改 ~/.bashrc 后用 source 重新加载",
            "与直接运行脚本不同，source 在当前 shell 执行"
        ]
    },
    "htop": {
        "name": "htop",
        "description": "交互式进程查看器。top 的增强版，更直观易用。",
        "category": "系统监控",
        "examples": [
            "htop              # 启动 htop",
            "htop -u username  # 只显示指定用户",
            "htop -p PID       # 只显示指定进程",
            "htop -t           # 树状显示",
            "htop -C           # 无彩色模式"
        ],
        "hotkeys": [
            "F1              帮助",
            "F2              设置",
            "F3              搜索",
            "F4              过滤",
            "F5              树状视图",
            "F6              排序方式",
            "F7              降低优先级",
            "F8              提高优先级",
            "F9              终止进程",
            "F10             退出",
            "u              过滤用户",
            "P              按 CPU 排序",
            "M              按内存排序",
            "T              按时间排序"
        ],
        "tips": [
            "比 top 更直观易用",
            "支持鼠标操作",
            "按 F6 可以改变排序列"
        ]
    }
}

# CSS 样式
CSS = """
@define-color bg_color #1a1a2e;
@define-color card_color #16213e;
@define-color text_color #e8e8e8;
@define-color accent_color #e94560;
@define-color secondary_color #4fc3f7;
@define-color success_color #81c784;
@define-color warning_color #ffb74d;
@define-color muted_color #6b6b8b;

window {
    background-color: @bg_color;
}

.title_label {
    font-size: 24px;
    font-weight: bold;
    color: @accent_color;
}

.subtitle_label {
    font-size: 12px;
    color: @muted_color;
}

.search_entry {
    background-color: @card_color;
    color: @text_color;
    border: none;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 14px;
    min-height: 20px;
}

.search_entry:focus {
    border: 2px solid @accent_color;
}

.list_frame {
    background-color: @card_color;
    border-radius: 12px;
    padding: 8px;
}

.command_row {
    background-color: transparent;
    padding: 8px 12px;
    border-radius: 6px;
    margin: 2px 0;
}

.command_row:hover {
    background-color: alpha(@accent_color, 0.1);
}

.command_row:selected {
    background-color: @accent_color;
    color: white;
}

.command_name {
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 13px;
    color: @text_color;
}

.command_row:selected .command_name {
    color: white;
}

.detail_frame {
    background-color: @card_color;
    border-radius: 12px;
    padding: 16px;
}

.detail_title {
    font-size: 18px;
    font-weight: bold;
    color: @accent_color;
    margin-bottom: 8px;
}

.detail_subtitle {
    font-size: 13px;
    font-weight: bold;
    color: @secondary_color;
    margin-top: 16px;
    margin-bottom: 8px;
}

.detail_text {
    font-size: 12px;
    color: @text_color;
}

.example_text {
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 11px;
    color: @success_color;
    background-color: alpha(@success_color, 0.1);
    padding: 8px 12px;
    border-radius: 6px;
    margin: 4px 0;
}

.tip_text {
    font-size: 11px;
    color: @warning_color;
    padding: 4px 0;
}

.stats_label {
    font-size: 10px;
    color: @muted_color;
}

.status_label {
    font-size: 10px;
    color: @muted_color;
}

.scrolled_window {
    background-color: transparent;
}

.listbox {
    background-color: transparent;
}

.section_header {
    font-size: 12px;
    font-weight: bold;
    color: @accent_color;
    padding: 8px;
}
"""


class LinuxCommandHelper(Gtk.Window):
    def __init__(self):
        super().__init__(title="Linux 命令查询助手")
        
        # 设置窗口属性
        self.set_default_size(950, 700)
        self.set_border_width(20)
        
        # 设置窗口位置居中
        self.set_position(Gtk.WindowPosition.CENTER)
        
        # 存储命令数据
        self.commands = {}
        self.all_command_names = []
        self.filtered_commands = []
        
        # 加载CSS样式
        self.load_css()
        
        # 创建界面
        self.create_ui()
        
        # 解析手册
        self.parse_manual()
        
        # 显示窗口
        self.show_all()
        
    def load_css(self):
        """加载CSS样式"""
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(CSS.encode())
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        self.get_style_context().add_class("window")

    def create_ui(self):
        """创建用户界面"""
        # 主容器
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(main_box)
        
        # === 标题区域 ===
        title_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        
        title_label = Gtk.Label()
        title_label.set_markup('<span font_desc="Microsoft YaHei UI 24 bold" foreground="#e94560">🔍 Linux 命令查询助手</span>')
        title_label.set_halign(Gtk.Align.START)
        title_box.pack_start(title_label, False, False, 0)
        
        # 副标题
        subtitle_label = Gtk.Label()
        subtitle_label.set_markup('<span font_desc="Microsoft YaHei UI 11" foreground="#6b6b8b">输入命令名，快速查找详细说明</span>')
        subtitle_label.set_halign(Gtk.Align.START)
        subtitle_label.set_margin_top(8)
        title_box.pack_start(subtitle_label, False, False, 0)
        
        # 统计标签
        self.stats_label = Gtk.Label()
        self.stats_label.set_markup('<span font_desc="Microsoft YaHei UI 10" foreground="#6b6b8b">已加载 0 条命令</span>')
        self.stats_label.set_halign(Gtk.Align.END)
        title_box.pack_end(self.stats_label, False, False, 0)
        
        main_box.pack_start(title_box, False, False, 0)
        
        # === 搜索区域 ===
        search_frame = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        search_frame.set_margin_bottom(5)
        
        # 搜索图标
        search_icon = Gtk.Label()
        search_icon.set_markup('<span font_desc="Segoe UI Emoji 16" foreground="#e94560">🔍</span>')
        search_icon.set_margin_end(10)
        search_frame.pack_start(search_icon, False, False, 0)
        
        # 搜索输入框
        self.search_entry = Gtk.Entry()
        self.search_entry.set_placeholder_text("输入命令名搜索（例如：ls, cd, grep...）")
        self.search_entry.get_style_context().add_class("search_entry")
        self.search_entry.set_hexpand(True)
        self.search_entry.connect("changed", self.on_search_changed)
        self.search_entry.connect("key-press-event", self.on_key_press)
        search_frame.pack_start(self.search_entry, True, True, 0)
        
        # 清除按钮
        clear_btn = Gtk.Button()
        clear_btn.set_label("✕")
        clear_btn.set_relief(Gtk.ReliefStyle.NONE)
        clear_btn.connect("clicked", lambda w: self.search_entry.set_text(""))
        clear_btn.set_margin_start(10)
        search_frame.pack_start(clear_btn, False, False, 0)
        
        main_box.pack_start(search_frame, False, False, 0)
        
        # === 内容区域 ===
        content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        content_box.set_hexpand(True)
        content_box.set_vexpand(True)
        
        # 左侧：命令列表
        left_frame = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        left_frame.set_size_request(280, -1)
        left_frame.get_style_context().add_class("list_frame")
        
        # 列表标题
        list_title = Gtk.Label()
        list_title.set_markup('<span font_desc="Microsoft YaHei UI 11 bold" foreground="#e94560">📋 候选命令</span>')
        list_title.set_halign(Gtk.Align.START)
        list_title.set_margin_bottom(8)
        left_frame.pack_start(list_title, False, False, 0)
        
        # 滚动窗口
        list_scroll = Gtk.ScrolledWindow()
        list_scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        list_scroll.set_vexpand(True)
        list_scroll.set_shadow_type(Gtk.ShadowType.NONE)
        
        # 列表框
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.listbox.connect("row-selected", self.on_row_selected)
        self.listbox.connect("row-activated", self.on_row_activated)
        list_scroll.add(self.listbox)
        
        left_frame.pack_start(list_scroll, True, True, 0)
        content_box.pack_start(left_frame, False, False, 0)
        
        # 右侧：详情区域
        right_frame = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        right_frame.get_style_context().add_class("detail_frame")
        right_frame.set_hexpand(True)
        
        # 详情标题
        detail_title = Gtk.Label()
        detail_title.set_markup('<span font_desc="Microsoft YaHei UI 11 bold" foreground="#e94560">📖 命令详情</span>')
        detail_title.set_halign(Gtk.Align.START)
        detail_title.set_margin_bottom(8)
        right_frame.pack_start(detail_title, False, False, 0)
        
        # 详情滚动窗口
        detail_scroll = Gtk.ScrolledWindow()
        detail_scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        detail_scroll.set_vexpand(True)
        detail_scroll.set_shadow_type(Gtk.ShadowType.NONE)
        
        # 详情内容框
        self.detail_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.detail_box.set_margin_top(8)
        self.detail_box.set_margin_bottom(8)
        self.detail_box.set_margin_start(8)
        self.detail_box.set_margin_end(8)
        
        detail_scroll.add(self.detail_box)
        right_frame.pack_start(detail_scroll, True, True, 0)
        
        content_box.pack_start(right_frame, True, True, 0)
        main_box.pack_start(content_box, True, True, 0)
        
        # === 状态栏 ===
        status_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        self.status_label = Gtk.Label()
        self.status_label.set_markup('<span font_desc="Microsoft YaHei UI 9" foreground="#6b6b8b">💡 输入命令名开始搜索 | 上下键选择 | Enter查看详情</span>')
        self.status_label.set_halign(Gtk.Align.START)
        status_box.pack_start(self.status_label, False, False, 0)
        
        version_label = Gtk.Label()
        version_label.set_markup('<span font_desc="Microsoft YaHei UI 9" foreground="#4a4a6a">v1.0 by 轩轩</span>')
        version_label.set_halign(Gtk.Align.END)
        status_box.pack_end(version_label, False, False, 0)
        
        main_box.pack_start(status_box, False, False, 0)
        
        # 默认显示提示
        self.show_welcome()

    def show_welcome(self):
        """显示欢迎信息"""
        # 清空详情区域
        for child in self.detail_box.get_children():
            self.detail_box.remove(child)
        
        # 欢迎标题
        welcome = Gtk.Label()
        welcome.set_markup('<span font_desc="Microsoft YaHei UI 16 bold" foreground="#e94560">欢迎使用 Linux 命令查询助手！</span>')
        welcome.set_halign(Gtk.Align.CENTER)
        welcome.set_margin_top(50)
        self.detail_box.pack_start(welcome, False, False, 0)
        
        # 使用说明
        tips = [
            "🔍 在上方搜索框输入命令名",
            "⌨️ 使用上下键选择候选项",
            "📋 按 Enter 或点击查看详情",
            "💡 支持模糊搜索和自动补全"
        ]
        
        for tip in tips:
            tip_label = Gtk.Label()
            tip_label.set_markup(f'<span font_desc="Microsoft YaHei UI 12" foreground="#8b8b8b">{tip}</span>')
            tip_label.set_halign(Gtk.Align.CENTER)
            tip_label.set_margin_top(15)
            self.detail_box.pack_start(tip_label, False, False, 0)
        
        self.detail_box.show_all()

    def parse_manual(self):
        """解析Linux命令手册"""
        try:
            with open(MANUAL_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            self.show_error("未找到命令手册文件！")
            return
        
        # 解析每个命令块
        pattern = r'─+\n【(\d+)】\s*(.+?)\n─+\n(.*?)(?=─+\n【|$)'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for match in matches:
            num = match[0]
            cmd_name = match[1].strip()
            cmd_content = match[2].strip()
            
            # 使用命令名的第一个单词作为主键
            main_cmd = cmd_name.split()[0] if cmd_name else cmd_name
            
            # 检查是否有预定义的详细说明
            if main_cmd in COMMAND_DETAILS:
                # 使用预定义的详细数据
                self.commands[main_cmd] = COMMAND_DETAILS[main_cmd].copy()
            else:
                # 从手册提取
                description = self.extract_description(cmd_content)
                examples = self.extract_examples(cmd_content)
                
                self.commands[main_cmd] = {
                    'name': cmd_name,
                    'description': description,
                    'content': cmd_content,
                    'examples': examples,
                    'number': num
                }
            
            if main_cmd not in self.all_command_names:
                self.all_command_names.append(main_cmd)
        
        # 排序命令列表
        self.all_command_names.sort()
        self.filtered_commands = self.all_command_names.copy()
        
        # 更新列表显示
        self.update_listbox()
        
        # 更新统计
        self.stats_label.set_markup(f'<span font_desc="Microsoft YaHei UI 10" foreground="#6b6b8b">已加载 {len(self.commands)} 条命令</span>')

    def extract_description(self, content):
        """提取命令描述"""
        lines = content.split('\n')
        desc_lines = []
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('─'):
                continue
            if len(desc_lines) < 5:
                desc_lines.append(line)
            else:
                break
        
        return '\n'.join(desc_lines)

    def extract_examples(self, content):
        """提取使用示例"""
        examples = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('$ ') or stripped.startswith('用法：') or stripped.startswith('示例'):
                if stripped and not stripped.startswith('────'):
                    examples.append(stripped)
        
        return examples[:6]

    def update_listbox(self):
        """更新命令列表"""
        # 清空列表
        for child in self.listbox.get_children():
            self.listbox.remove(child)
        
        # 添加命令项
        for cmd in self.filtered_commands[:100]:  # 限制显示100条
            row = Gtk.ListBoxRow()
            row.cmd_name = cmd
            
            label = Gtk.Label()
            label.set_markup(f'<span font_desc="Consolas 12" foreground="#e8e8e8">{html.escape(cmd)}</span>')
            label.set_halign(Gtk.Align.START)
            label.set_margin_start(8)
            label.set_margin_end(8)
            label.set_margin_top(6)
            label.set_margin_bottom(6)
            
            row.add(label)
            self.listbox.add(row)
        
        self.listbox.show_all()

    def on_search_changed(self, entry):
        """搜索内容变化"""
        query = entry.get_text().strip().lower()
        
        if not query:
            self.filtered_commands = self.all_command_names.copy()
            self.status_label.set_markup('<span font_desc="Microsoft YaHei UI 9" foreground="#6b6b8b">💡 共 ' + str(len(self.commands)) + ' 条命令</span>')
        else:
            # 过滤命令 - 优先匹配命令名开头
            exact_match = []
            starts_with = []
            word_boundary = []  # 单词边界匹配
            contains = []
            
            for cmd in self.all_command_names:
                cmd_lower = cmd.lower()
                if cmd_lower == query:
                    exact_match.append(cmd)
                elif cmd_lower.startswith(query):
                    starts_with.append(cmd)
                elif re.search(r'\b' + re.escape(query), cmd_lower):
                    word_boundary.append(cmd)
                elif query in cmd_lower:
                    contains.append(cmd)
            
            # 按优先级排序
            self.filtered_commands = exact_match + starts_with + word_boundary + contains
            self.status_label.set_markup(f'<span font_desc="Microsoft YaHei UI 9" foreground="#6b6b8b">🔍 找到 {len(self.filtered_commands)} 条匹配命令</span>')
        
        self.update_listbox()
        
        # 如果只有一个结果，自动选中并显示
        if len(self.filtered_commands) == 1:
            GLib.idle_add(self.select_first_row)

    def select_first_row(self):
        """选中第一行"""
        row = self.listbox.get_row_at_index(0)
        if row:
            self.listbox.select_row(row)
            self.show_command_detail(row.cmd_name)
        return False

    def on_key_press(self, widget, event):
        """键盘事件处理"""
        keyval = event.keyval
        
        if keyval == Gdk.KEY_Down:
            # 下箭头
            selected = self.listbox.get_selected_row()
            if selected:
                next_row = self.listbox.get_row_at_index(selected.get_index() + 1)
            else:
                next_row = self.listbox.get_row_at_index(0)
            
            if next_row:
                self.listbox.select_row(next_row)
                self.listbox.scroll_to(next_row)
            return True
            
        elif keyval == Gdk.KEY_Up:
            # 上箭头
            selected = self.listbox.get_selected_row()
            if selected and selected.get_index() > 0:
                prev_row = self.listbox.get_row_at_index(selected.get_index() - 1)
                if prev_row:
                    self.listbox.select_row(prev_row)
                    self.listbox.scroll_to(prev_row)
            return True
            
        elif keyval == Gdk.KEY_Escape:
            # Escape键清空搜索
            self.search_entry.set_text("")
            return True
            
        elif keyval == Gdk.KEY_Return or keyval == Gdk.KEY_KP_Enter:
            # 回车键选中第一个命令并显示详情
            row = self.listbox.get_row_at_index(0)
            if row and hasattr(row, 'cmd_name'):
                self.listbox.select_row(row)
                self.show_command_detail(row.cmd_name)
            return True
            
        return False

    def on_row_selected(self, listbox, row):
        """列表项选中"""
        if row and hasattr(row, 'cmd_name'):
            self.show_command_detail(row.cmd_name)

    def on_row_activated(self, listbox, row):
        """列表项激活（双击）"""
        if row and hasattr(row, 'cmd_name'):
            self.show_command_detail(row.cmd_name)

    def show_command_detail(self, cmd_name):
        """显示命令详情"""
        if cmd_name not in self.commands:
            return
        
        cmd_data = self.commands[cmd_name]
        
        # 清空详情区域
        for child in self.detail_box.get_children():
            self.detail_box.remove(child)
        
        # 命令名称
        title = Gtk.Label()
        display_name = cmd_data.get('name', cmd_name)
        title.set_markup(f'<span font_desc="Microsoft YaHei UI 18 bold" foreground="#e94560">📌 {html.escape(str(display_name))}</span>')
        title.set_halign(Gtk.Align.START)
        title.set_margin_bottom(10)
        self.detail_box.pack_start(title, False, False, 0)
        
        # 分类标签（如果有）
        if 'category' in cmd_data:
            category_label = Gtk.Label()
            category_label.set_markup(f'<span font_desc="Microsoft YaHei UI 10" foreground="#4a4a6a">📂 分类：{cmd_data["category"]}</span>')
            category_label.set_halign(Gtk.Align.START)
            category_label.set_margin_bottom(8)
            self.detail_box.pack_start(category_label, False, False, 0)
        
        # 分隔线
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        self.detail_box.pack_start(separator, False, False, 0)
        
        # 命令说明标题
        desc_title = Gtk.Label()
        desc_title.set_markup('<span font_desc="Microsoft YaHei UI 12 bold" foreground="#4fc3f7">📝 命令说明</span>')
        desc_title.set_halign(Gtk.Align.START)
        desc_title.set_margin_top(15)
        desc_title.set_margin_bottom(8)
        self.detail_box.pack_start(desc_title, False, False, 0)
        
        # 命令说明内容
        desc_label = Gtk.Label()
        desc_text = cmd_data.get('description', '')
        desc_label.set_markup(f'<span font_desc="Microsoft YaHei UI 11" foreground="#e8e8e8">{html.escape(str(desc_text))}</span>')
        desc_label.set_halign(Gtk.Align.START)
        desc_label.set_line_wrap(True)
        desc_label.set_xalign(0)
        self.detail_box.pack_start(desc_label, False, False, 0)
        
        # 使用示例
        examples = cmd_data.get('examples', [])
        if examples:
            example_title = Gtk.Label()
            example_title.set_markup('<span font_desc="Microsoft YaHei UI 12 bold" foreground="#4fc3f7">💡 使用示例</span>')
            example_title.set_halign(Gtk.Align.START)
            example_title.set_margin_top(15)
            example_title.set_margin_bottom(8)
            self.detail_box.pack_start(example_title, False, False, 0)
            
            for example in examples:
                if example:
                    example_label = Gtk.Label()
                    escaped_example = html.escape(str(example))
                    example_label.set_markup(f'<span font_desc="Consolas 11" foreground="#81c784">  {escaped_example}</span>')
                    example_label.set_halign(Gtk.Align.START)
                    example_label.set_line_wrap(True)
                    example_label.set_xalign(0)
                    self.detail_box.pack_start(example_label, False, False, 2)
        
        # 常用选项
        options = cmd_data.get('options', [])
        if options:
            option_title = Gtk.Label()
            option_title.set_markup('<span font_desc="Microsoft YaHei UI 12 bold" foreground="#4fc3f7">⚙️ 常用选项</span>')
            option_title.set_halign(Gtk.Align.START)
            option_title.set_margin_top(15)
            option_title.set_margin_bottom(8)
            self.detail_box.pack_start(option_title, False, False, 0)
            
            for option in options:
                if option:
                    option_label = Gtk.Label()
                    escaped_option = html.escape(str(option))
                    option_label.set_markup(f'<span font_desc="Consolas 10" foreground="#b8b8b8">  {escaped_option}</span>')
                    option_label.set_halign(Gtk.Align.START)
                    option_label.set_line_wrap(True)
                    option_label.set_xalign(0)
                    self.detail_box.pack_start(option_label, False, False, 1)
        
        # 快捷键
        hotkeys = cmd_data.get('hotkeys', [])
        if hotkeys:
            hotkey_title = Gtk.Label()
            hotkey_title.set_markup('<span font_desc="Microsoft YaHei UI 12 bold" foreground="#4fc3f7">⌨️ 快捷键</span>')
            hotkey_title.set_halign(Gtk.Align.START)
            hotkey_title.set_margin_top(15)
            hotkey_title.set_margin_bottom(8)
            self.detail_box.pack_start(hotkey_title, False, False, 0)
            
            for hotkey in hotkeys:
                if hotkey:
                    hotkey_label = Gtk.Label()
                    escaped_hotkey = html.escape(str(hotkey))
                    hotkey_label.set_markup(f'<span font_desc="Consolas 10" foreground="#ce93d8">  {escaped_hotkey}</span>')
                    hotkey_label.set_halign(Gtk.Align.START)
                    hotkey_label.set_line_wrap(True)
                    hotkey_label.set_xalign(0)
                    self.detail_box.pack_start(hotkey_label, False, False, 1)
        
        # 小贴士
        tips = cmd_data.get('tips', [])
        if tips:
            tip_title = Gtk.Label()
            tip_title.set_markup('<span font_desc="Microsoft YaHei UI 12 bold" foreground="#4fc3f7">📌 小贴士</span>')
            tip_title.set_halign(Gtk.Align.START)
            tip_title.set_margin_top(15)
            tip_title.set_margin_bottom(8)
            self.detail_box.pack_start(tip_title, False, False, 0)
            
            for tip in tips:
                if tip:
                    tip_label = Gtk.Label()
                    tip_label.set_markup(f'<span font_desc="Microsoft YaHei UI 10" foreground="#ffb74d">  {html.escape(str(tip))}</span>')
                    tip_label.set_halign(Gtk.Align.START)
                    tip_label.set_line_wrap(True)
                    tip_label.set_xalign(0)
                    self.detail_box.pack_start(tip_label, False, False, 2)
        else:
            # 默认小贴士
            tip_title = Gtk.Label()
            tip_title.set_markup('<span font_desc="Microsoft YaHei UI 12 bold" foreground="#4fc3f7">📌 小贴士</span>')
            tip_title.set_halign(Gtk.Align.START)
            tip_title.set_margin_top(15)
            tip_title.set_margin_bottom(8)
            self.detail_box.pack_start(tip_title, False, False, 0)
            
            default_tips = [
                f"• 在终端输入 man {cmd_name} 查看详细手册",
                f"• 在终端输入 {cmd_name} --help 查看简要帮助",
                "• 按 Tab 键可以自动补全命令"
            ]
            
            for tip in default_tips:
                tip_label = Gtk.Label()
                tip_label.set_markup(f'<span font_desc="Microsoft YaHei UI 10" foreground="#ffb74d">  {tip}</span>')
                tip_label.set_halign(Gtk.Align.START)
                self.detail_box.pack_start(tip_label, False, False, 2)
        
        self.detail_box.show_all()
        
        # 更新状态栏
        self.status_label.set_markup(f'<span font_desc="Microsoft YaHei UI 9" foreground="#6b6b8b">📖 正在查看: {cmd_name}</span>')

    def show_error(self, message):
        """显示错误信息"""
        for child in self.detail_box.get_children():
            self.detail_box.remove(child)
        
        error_label = Gtk.Label()
        error_label.set_markup(f'<span font_desc="Microsoft YaHei UI 14" foreground="#e94560">❌ {message}</span>')
        error_label.set_halign(Gtk.Align.CENTER)
        error_label.set_margin_top(100)
        self.detail_box.pack_start(error_label, False, False, 0)
        self.detail_box.show_all()


def main():
    win = LinuxCommandHelper()
    win.connect("destroy", Gtk.main_quit)
    
    # 聚焦到搜索框
    win.search_entry.grab_focus()
    
    Gtk.main()


if __name__ == "__main__":
    main()
