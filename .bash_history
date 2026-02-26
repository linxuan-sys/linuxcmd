:
[[ "$VAR" =~ regex ]]
[[ "$VAR" != "value" ]]
[[ "$VAR" == "value" ]]
# 标签页1: Python 开发
# 标签页2: C++ 开发  
# 标签页3: 其他工作
~/下载
alias
alias apt-install='sudo apt install'
alias apt-update='sudo apt update'
alias apt-upgrade='sudo apt upgrade -y'
alias bashrc='nano ~/.bashrc'
alias ....='cd ../../..'
alias ...='cd ../..'
alias ..='cd ..'
alias ~='cd ~'
alias cls='clear'
alias cpuinfo='lscpu'
alias df='df -h'
alias diskinfo='df -h'
alias dnf-install='sudo dnf install'
alias dnf-update='sudo dnf update'
alias dnf-upgrade='sudo dnf upgrade -y'
alias docker-exec='docker exec -it'
alias docker-img='docker images'
alias docker-log='docker logs'
alias docker-psa='docker ps -a'
alias docker-ps='docker ps'
alias docker-rm='docker rm'
alias docker-rmi='docker rmi'
alias du='du -h'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias free='free -h'
alias git-br='git branch'
alias git-ci='git commit'
alias git-co='git checkout'
alias git-lg='git log --oneline --graph'
alias git-pl='git pull'
alias git-ps='git push'
alias git-st='git status'
alias grep='grep --color=auto'
alias h='history'
alias install='sudo dnf install'
alias j='jobs'
alias j='jobs -l'
alias la='ls -A'
alias listen='netstat -tln'
alias ll='ls -la'
alias l='ls'
alias l='ls -CF'
alias meminfo='free -h'
alias mkdir='mkdir -pv'
alias myip='curl ifconfig.me'
alias myip='curl -s ifconfig.me'
alias nowdate='date +"%Y-%m-%d"'
alias now='date +"%T"'
alias npm-install='npm install'
alias npm-run='npm run'
alias npm-update='npm update'
alias ping='ping -c 5'
alias pip-install='pip3 install'
alias pip-list='pip3 list'
alias pip-update='pip3 install --upgrade'
alias ports='netstat -tulanp'
alias pscpu='ps auxf | sort -nr -k 3 | head -10'
alias psmem='ps auxf | sort -nr -k 4 | head -10'
alias reload='source ~/.bashrc'
alias remove='sudo dnf remove'
alias search='sudo dnf search'
alias update='sudo dnf update'
alias vimrc='nano ~/.vimrc'
alias wget='wget -c'
alias yarn-add='yarn add'
alias yarn-install='yarn install'
anacron
ansible
ansible all -a "uptime"
ansible all -m ping
ansible-galaxy
ansible-galaxy install role
ansible-playbook
ansible-playbook playbook.yml
ansible-vault
ansible-vault decrypt file
ansible-vault encrypt file
ant
apache2ctl configtest
apache2ctl graceful
apt
apt autoremove
apt-cache
apt clean
apt edit-sources
apt-get
apt install package
apt list --installed
apt list --upgradable
apt remove package
apt search keyword
apt show package
apt update
apt upgrade
arch
args
ascii
at 10:00
at now + 1 hour
atq
atrm 1
audacity
automake
autopep8 --in-place script.py
autopoint
autoreconf
autoreconf -i
autoscan
autoupdate
awk
awk 'BEGIN{print 1+1}'
aws
aws cloudformation deploy --template-file file.yaml --stack-name name
aws cloudformation list-stacks
aws ec2
aws ec2 describe-instances
aws ec2 run-instances --image-id ami --instance-type t2.micro
aws ec2 start-instances --instance-ids id
aws ec2 stop-instances --instance-ids id
aws ec2 terminate-instances --instance-ids id
aws ecr get-login-password | docker login --username AWS --password-stdin account.dkr.ecr.region.amazonaws.com
aws eks update-kubeconfig --name cluster_name
aws lambda
aws lambda invoke --function-name name output.json
aws lambda list-functions
aws rds describe-db-instances
aws s3
aws s3 cp file s3://bucket/
aws s3 ls
aws s3 rm s3://bucket/file
aws s3 sync local s3://bucket/
aws sns list-topics
aws sqs list-queues
az acr list
az storage account list
az vm list
az vm start --name name --resource-group rg
az vm stop --name name --resource-group rg
babel script.js -o output.js
badblocks
base32
base64
base64-decode
base64 -d file
base64-encode
base64 file
basename
bash
bashbug
bash script.sh
bash-static
batch
bazel build //target
bazel run //target
bazel test //target
bc
bcrypt
bg
bind
/bin/python /home/ice/桌面/python/python2.py
biosdecode
black .
black script.py
bleachbit
blender
bootctl
bower install
brew
bridge
btrfs
btrfs-convert
btrfs-find-root
btrfs-image
btrfs-map-logical
btrfs-select-super
btrfstune
btrfs-zero-log
builtin
bun
bun add
bun install
bun run
busctl
bzcat
bzcmp
bzdiff
bzegrep
bzfgrep
bzgrep
bzip2
bzip2recover
bzless
bzmore
cabal build
cal
cal 12 2024
cal 2024
calibre
callgrind_annotate callgrind.out
cargo
cargo-add
cargo-binstall
cargo build
cargo build --release
cargo check
cargo-clean
cargo clippy
cargo doc
cargo-doc
cargo-init
cargo-install
cargo install crate
cargo-locate-project
cargo-login
cargo-logout
cargo-metadata
cargo-new
cargo new project
cargo-outdated
cargo-owner
cargo-package
cargo-pkgid
cargo publish
cargo-report
cargo-rm
cargo run
cargo-run
cargo-search
cargo test
cargo-tree
cargo-uninstall
cargo update
cargo-upgrade
cargo-vendor
cargo-verify-project
cargo-version
cargo-yank
cat
cat /etc/group
cat /etc/gshadow
cat /etc/passwd
cat /etc/shadow
cat /etc/sudoers
catman
cat /proc/sys/kernel/random/uuid
cc
c++-config
cd
cd ~
cd ~/桌面/python 
celery -A tasks beat
celery -A tasks flower
celery -A tasks worker --loglevel=info
certbot certificates
certbot certonly --nginx
certbot renew
cfdisk
chage
chage -E 2024-12-31 username
chage -I 7 username
chage -l username
chage -M 90 username
chage -W 7 username
chattr
chcon
chcpu
checkinstall
checkpolicy
chfn
chgrp
chkconfig
chmem
chmod
chmod +x script.sh
choom
chown
chronyc
chroot
chroot /path /bin/bash
chrt
chsh
chvt
ckbcomp
cksum
clang-format -i file.cpp
clang -o output source.c
clang++ -o output source.cpp
clang-tidy file.cpp
clash-verge
clear
clear_console
clock
clockdiff
cmake
cmake .
cmake -B build
cmake --build .
cmake --build build
cmake --install .
cmp
code
code .
code-oss
col
colcrt
colrm
column
column -s: -t /etc/passwd
column -t file
comm
command | tee output.log
command | tee >(process1) >(process2)
commitlint --edit
composer
composer dump-autoload
composer install
composer require
composer require package
composer update
conda update --all
./configure
conmon
consolehelper
consul kv get key
consul kv put key value
consul members
control-center
convert input.png -blur 0x4 output.png
convert input.png -crop 100x100+10+10 output.png
convert input.png -quality 90 output.jpg
convert input.png -resize 50% output.png
convert input.png -rotate 90 output.png
convert -size 100x100 xc:red output.png
coredumpctl
coverage report
coverage run -m pytest
cp
cpio
cpp
cppcheck file.cpp
cpupower
cpupower-frequency-info
cpupower-frequency-set
cpupower-idle-info
cpupower-idle-set
cpupower-info
cpupower-set
crda
createrepo
crontab
crontab -e
crontab -l
crontab -r
crontab -u user -e
csplit
ctrlaltdel
curl
curl-config
cut
cvs
daemonize
darktable
dash
date
date -d "2024-01-01"
date -d "+7 days"
date -d "-7 days"
date -d "next monday"
date +%H:%M:%S
date +%s
date -u
date +%Y-%m-%d
date +%Y-%m-%d\ %H:%M:%S
db_checkpoint
db_deadlock
db_dump
db_load
db_printlog
db_recover
db_stat
db_upgrade
dbus-binding-tool
dbus-cleanup-sockets
dbus-daemon
dbus-launch
dbus-monitor
dbus-run-session
dbus-send
dbus-test-tool
dbus-update-activation-environment
dbus-uuidgen
dconf
dconf dump
dconf load
dconf reset
dconf write
[ -d dir ]
[[ -d dir ]]
debugfs
declare
declare -a ARRAY
declare -A MAP
declare -i VAR
declare -r VAR
delpart
delta
deno
depmod
devlink
df
dfutool
dhclient
dhclient-script
dhcpd
dhcrelay
diff
diff3
diffstat
dig
dir
dircolors
dirmngr
dirmngr-client
dirname
dirs
discord
disown
django-admin startapp app
django-admin startproject project
djpeg
dmesg
dmidecode
dmsetup
dmstats
dnf
dnf-automatic
dnf autoremove
dnf check-update
dnf clean all
dnf clean cache
dnf clean dbcache
dnf clean metadata
dnf-config-manager
dnf config-manager --add-repo url
dnf config-manager --disable repo
dnf config-manager --enable repo
dnf-copr
dnf-debug
dnf downgrade package
dnf-download
dnf erase package
dnf-generate_completion_cache
dnf group info "group name"
dnf group install "group name"
dnf group list
dnf group remove "group name"
dnf-groups-manager
dnf history
dnf-history
dnf history list
dnf history redo transaction_id
dnf history undo transaction_id
dnf info package
dnf install
dnf install package
dnf-leaves
dnf list
dnf list available
dnf list installed
dnf list updates
dnf-local
dnf makecache
dnf-makecache
dnf-mark
dnf-module
dnf module enable module:stream
dnf module install module:stream/profile
dnf module list
dnf-offline
dnf-offline-upgrade
dnf provides /usr/bin/command
dnf-reinstall
dnf reinstall package
dnf remove
dnf-remove
dnf remove package
dnf-repo
dnf-repograph
dnf repolist
dnf-repolist
dnf repolist disabled
dnf repolist enabled
dnf-repoquery
dnf-reposync
dnf-search
dnf search keyword
dnf-shell
dnf-swap
dnf update
dnf-updateinfo
dnf upgrade
dnf-upgrade
dnf upgrade --refresh
dnf whatprovides /usr/bin/command
dnsdomainname
docker
docker build
docker-compose
docker exec
docker logs
docker rm
docker rmi
docker run
docker stop
doctl compute droplet list
doctl kubernetes cluster list
domainname
dos2unix
dos2unix file
dpkg
dpkg-deb
dpkg -i package.deb
dpkg -l
dpkg -L package
dpkg-query
dpkg -r package
dpkg -S /path/to/file
dpkg-statoverride
dpkg-trigger
dracut
drawterm
du
dump
dump-acct
dumpe2fs
dumpkeys
dump-utmp
dvd+rw-booktype
dvd+rw-format
dvd+rw-mediainfo
dvipdf
dwarf2json
e2freefrag
e2fsck
e2image
e2label
e2mmpstatus
e2scrub
e2scrub_all
e2undo
e4crypt
e4defrag
easyeffects
easy_install
ebtables
echo
echo "* * * * * command" | crontab -
echo -e "line1\nline2"
echo "hello"
echo "ibase=2; 1010" | bc
echo -n "no newline"
echo "obase=2; 10" | bc
echo "scale=2; 10/3" | bc
ed
edit
editorconfig-checker
edquota
efibootmgr
efivar
egrep
eject
element
elfedit
elinks
elinks-keys
emacs
enable
env
envsubst
eps2eps
epsffit
eqn
eslint --fix .
eslint script.js
etags
etcdctl del key
etcdctl get key
etcdctl get "" --prefix
etcdctl put key value
ethtool
evince
ex
exec
exiftool -all= image.jpg
exiftool -Artist="Name" image.jpg
exiftool image.jpg
exit
expand
expand file > newfile
expect
expiry
export
export DISPLAY=:0
export EDITOR=vim
export GOPATH=$HOME/go
export JAVA_HOME=/usr/lib/jvm/java
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LESS="-R"
export NODE_PATH=/usr/lib/node_modules
export -n VAR
export PAGER=less
export PATH=$PATH:/new/path
export TERM=xterm-256color
export TZ=Asia/Shanghai
export VISUAL=vim
expr
expr 1 + 1
expr 2 \* 3
expr length "string"
expr substr "string" 1 3
facter
faillock
faillog
false
fastapi dev main.py
fbgs
fbset
fc
fc-cache
fc-cat
fc-conflist
fcitx5
fcitx5-configtool
fcitx5-remote
fc-list
fc-match
fc-pattern
fc-query
fc-scan
fc-validate
fd
fdformat
fdisk
[ -f file ]
[[ -f file ]]
ffmpeg
ffmpeg -f concat -i list.txt -c copy output.mp4
ffmpeg -i
ffmpeg -i input.mp4 -an -vcodec copy output.mp4
ffmpeg -i input.mp4 -b:v 1M -b:a 128k output.mp4
ffmpeg -i input.mp4 -c:v libx264 -crf 23 output.mp4
ffmpeg -i input.mp4 -filter:v "fps=fps=15" output.gif
ffmpeg -i input.mp4 output.mp3
ffmpeg -i input.mp4 -s 1280x720 output.mp4
ffmpeg -i input.mp4 -ss 00:01:00 -t 10 output.mp4
ffmpeg -i input.mp4 -vf "fade=t=in:st=0:d=5" output.mp4
ffmpeg -i input.mp4 -vf "scale=640:-1" output.mp4
ffmpeg -i input.mp4 -vn -acodec copy output.aac
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4
ffmpeg -loop 1 -i image.png -c:v libx264 -t 10 output.mp4
ffprobe input.mp4
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.mp4
fg
fgconsole
figma-linux
file
file -b filename
file binary
file filename
filefrag
file -i filename
file --mime-type filename
find
findfs
findmnt
finger
finger username
firefox
firefox-esr
flake8 script.py
flask db init
flask db migrate -m "message"
flask db upgrade
flask run
flask shell
flatpak
flatpak info app
flatpak install
flatpak install flathub app
flatpak list
flatpak remote-add --if-not-exists flathub url
flatpak remote-delete remote
flatpak remote-list
flatpak run app
flatpak search keyword
flatpak uninstall
flatpak uninstall app
flatpak update
flatpak update --appstream
flatseal
flock
flock -x /tmp/lock -c "command"
fly apps list
fly deploy
fly logs
fly ssh console
fmt
fmt file
fmt -w 80 file
fold
fold -w 80 file
fontconfig
fonttosfnt
free
fsck
fsck.cramfs
fsck.ext2
fsck.ext3
fsck.ext4
fsck.minix
fsck.xfs
fsfreeze
fstrim
fuser
fuser 80/tcp
fuser -k 80/tcp
fusermount
fusermount3
g++
gapplication
gawk
gcc
gcc-config
gcc -g -o output source.c
gcc -o output source.c
gcc -shared -fPIC -o lib.so source.c
gcc -Wall -o output source.c
gcloud compute instances list
gcloud compute ssh instance_name
gcloud container clusters list
gcloud storage ls
gcore
gdb
gdb --args command arg1 arg2
gdb binary
gdb -p pid
gdbserver
gdbus
gdbus-codegen
gdiffmk
gdisk
gdk-pixbuf-csource
gdk-pixbuf-pixdata
gdk-pixbuf-query-loaders
gdm
gdmdynamic
gdmflexiserver
gdm-safe-restart
gdm-signal
gedit
gem
gem environment
gem install package
gem list
gem uninstall package
gem update
gencat
genisoimage
getcap
getconf
getenforce
getent
getfacl
getfattr
getopt
getpcaps
getsebool
gettext
ghostscript
gif2rgb
gifbuild
gifclrmp
gifcolor
gifcomb
gifict
gifinto
gifovly
gifpos
gifrotat
gifrsize
giftext
gifwedge
gimp
gimp-2.10
gio
gio-querymodules
git
git add
git archive --format=zip HEAD > archive.zip
git branch
git bundle create file.bundle main
git bundle unbundle file.bundle
git checkout
git-clang-format
git clone
git commit
git config --list --global
git config --list --local
git config --list --system
git count-objects -v
git count-objects -vH
git-credential-cache
git-credential-cache--daemon
git-credential-libsecret
git-credential-store
git diff
git-filter-repo
git for-each-ref --sort=-committerdate
git-lfs
git lfs install
git lfs lsfiles
git lfs push --all origin
git lfs track "*.psd"
git log
git ls-files
git ls-remote origin
git ls-tree HEAD
git merge
git pull
git push
git rebase
git remote
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
git rev-parse --short HEAD
git-shell
git shortlog -sn
git shortlog -sne
git show-ref
git sparse-checkout init
git sparse-checkout set dir1 dir2
git stash
git status
git submodule add url path
git submodule foreach git pull
git submodule init
git submodule update
git submodule update --init --recursive
git symbolic-ref HEAD
git verify-pack -v .git/objects/pack/*.idx
git worktree add ../path branch
git worktree list
git worktree remove ../path
glib-compile-resources
glib-compile-schemas
glib-genmarshal
glib-gettextize
glib-mkenums
glob
gnome-calculator
gnome-calculator-search-provider
gnome-control-center
gnome-desktop-item-edit
gnome-disks
gnome-disk-utility
gnome-extra-settings
gnome-font-viewer
gnome-help
gnome-keyring
gnome-keyring-3
gnome-keyring-daemon
gnome-logs
gnome-power-manager
gnome-screenshot
gnome-session
gnome-session-inhibit
gnome-session-quit
gnome-settings-daemon
gnome-shell
gnome-shell-extension-prefs
gnome-shell-perf-tool
gnome-software
gnome-system-monitor
gnome-terminal
gnome-terminal.real
gnome-text-editor
gnome-thumbnail-font
gnome-tweaks
gnome-weather
go
gobject-query
go build
go build -o output main.go
go fmt
gofmt -w .
go get
go get package
goimports -w .
golint ./...
go mod
go mod init
go mod tidy
google-chrome
google-chrome-stable
g++ -o output source.cpp
go run
go run main.go
go test
go test ./...
go vet ./...
gpasswd
gpg
gpg2
gpg-agent
gpgconf
gpg-connect-agent
gpg --decrypt file.gpg
gpg --encrypt file
gpg --export -a "name" > public.key
gpg --gen-key
gpg --import public.key
gpg --list-keys
gpgparsemail
gpg --sign file
gpgsm
gpgsplit
gpgtar
gpgv
gpg --verify file.sig
gpg-wks-server
gpg-zip
gpic
gprof
gptx
gradle
gradle build
gradle dependencies
gradle run
gradle test
grep
groupadd groupname
groupdel groupname
groupmod -n newname oldname
groups
groups username
grpck
grpconv
grpunconv
grub2-editenv
grub2-file
grub2-glue-efi
grub2-install
grub2-kbdcomp
grub2-macbless
grub2-menulst2cfg
grub2-mkconfig
grub2-mkfont
grub2-mkimage
grub2-mklayout
grub2-mknetdir
grub2-mkpasswd-pbkdf2
grub2-mkrelpath
grub2-mkrescue
grub2-mkstandalone
grub2-ofpathname
grub2-probe
grub2-reboot
grub2-render-label
grub2-script-check
grub2-set-default
grub2-set-password
grub2-sparc64-setup
grub2-syslinux2cfg
grub-file
grub-fstest
grub-glue-efi
grub-kbdcomp
grub-menulst2cfg
grub-mkfont
grub-mkimage
grub-mklayout
grub-mknetdir
grub-mkpasswd-pbkdf2
grub-mkrelpath
grub-mkrescue
grub-mkstandalone
grub-ofpathname
grub-probe
grub-reboot
grub-render-label
grub-script-check
grub-syslinux2cfg
gs
gsbj
gsdj
gsdj500
gsettings
gsettings-data-convert
gslj
gslp
gsnd
gsoelim
gs-office
gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -o output.pdf input.pdf
gss-proxy
gssproxy
g++ -std=c++17 -o output source.cpp
gtbl
gtf
gtk-builder-convert
gtk-encode-symbolic-svg
gtk-launch
gtk-query-immodules-3.0
gtk-update-icon-cache
gtroff
gunicorn app:app
gunicorn -w 4 -b 0.0.0.0:8000 app:app
gunzip
gvfs-afc-volume-monitor
gvfs-backend
gvfsd
gvfsd-admin
gvfsd-afc
gvfsd-afp
gvfsd-afp-browse
gvfsd-archive
gvfsd-cdda
gvfsd-computer
gvfsd-dav
gvfsd-dnssd
gvfsd-ftp
gvfsd-http
gvfsd-localtest
gvfsd-metadata
gvfsd-mtp
gvfsd-network
gvfsd-recent
gvfsd-sftp
gvfsd-smb
gvfsd-smb-browse
gvfsd-trash
gvfsd-webdav
gvfs-fuse-daemon
gvfs-goa-volume-monitor
gvfs-gphoto2-volume-monitor
gvfs-mtp-volume-monitor
gvfs-uae-volume-monitor
gvfs-udisks2-volume-monitor
gzexe
gzip
gzlog
halt
handbrake
hash
hd
hdparm
head
head -1 script.sh
helm
helm install release chart
helm list
helm repo add name url
helm repo update
helm rollback release
helm search repo keyword
helm show values chart
helm template release chart
helm uninstall release
helm upgrade release chart
help
heroku apps:list
heroku logs --tail
heroku ps:scale web=1
hexdump
hexdump -C binary
hexdump -C file
hinfo
history
host
hostid
hostname
hostnamectl
hostnamectl set-hostname newname
hostnamectl status
hostname -d
hostname -f
hostname -i
hostname -I
hpftodit
htdbm
htdigest
htop
htpasswd
husky install
hwclock
hwe-support-status
hwinfo
i2cdetect
i2cdump
i2cget
i2cset
iconv
iconvconfig
iconv -f UTF-8 -t GBK file
iconv -l
id
ident
identify
identify image.png
id -Gn username
id -G username
id username
id -u username
ifcfg
ifconfig
ifdown
ifenslave
iflow
ifquery
ifstat
iftop
ifup
imagemagick convert input.png output.jpg
import
indent
indxbib
info
infobrowser
infocmp
infokey
infotocap
init
initctl
inkscape
inotifywait
inotifywatch
insmod
install
install-info
installkernel
instmodsh
iostat
ip
ip6tables
ip6tables-restore
ip6tables-save
ip addr
ipcalc
ipcmk
ipcrm
ipcs
ip link
ip maddress
ipmievd
ipmilan
ipmish
ipmitool
ipmiui
ip monitor
ip mroute
ip mrule
ip neighbour
ip netns
ip ntable
ip route
ip rule
ip socket
iptables
iptables-apply
iptables-restore
iptables-save
ip tcpmetrics
ip token
iptraf
iptraf-ng
ip tunnel
iptunnel
ip xfrm
iscsiadm
iscsid
iscsi-iname
iscsistart
isort script.py
isosize
ispell
istioctl analyze
istioctl dashboard kiali
iw
iwconfig
iwevent
iwgetid
iwlist
iwpriv
iwspy
jar
jarsigner
java
javac
javac -cp . Main.java
javac Main.java
java -cp . Main
javadoc
javah
java Main
javap
jcmd
jconsole
jdb
jest
jest --coverage
jetbrains-toolbox
jhat
jinfo
jjs
jmap
jobs
joplin
journalctl
jps
jrunscript
jsadebugd
jspm install
jstack
jstat
jstatd
karma start
kbdinfo
kbd_mode
kcachegrind callgrind.out
kdenlive
keepassxc
kernel-install
kexec
keyctl
kill
killall
kitty @ dump-session > ~/桌面/my-session.conf
kitty @ ls
kitty --session ~/桌面/文本文档.txt
kitty --session ~/桌面/kitty-session.conf
kitty --session ~/桌面/my-session.conf
kmod
kubectl apply -f deployment.yaml
kubectl cluster-info
kubectl config get-contexts
kubectl config use-context context_name
kubectl cp file pod_name:/path/
kubectl create deployment name --image=image
kubectl delete -f deployment.yaml
kubectl describe pod pod_name
kubectl exec -it pod_name -- /bin/bash
kubectl expose deployment name --port=80 --type=LoadBalancer
kubectl get deployments
kubectl get nodes
kubectl get pods
kubectl get pods -A
kubectl get services
kubectl logs -f pod_name
kubectl logs pod_name
kubectl port-forward pod_name 8080:80
kubectl rollout history deployment/name
kubectl rollout status deployment/name
kubectl rollout undo deployment/name
kubectl scale deployment name --replicas=3
kubectl set image deployment/name container=image:tag
kubectl top nodes
kubectl top pods
last
lastb
lastlog
lastlog -u username
last -n 10
last reboot
last shutdown
last -x
launch /home/ice/桌面/C++
launch /home/ice/桌面/office
launch /home/ice/桌面/python
ld
ldattach
ldconfig
ldconfig -p
ldconfig.real
ldd
ldd /usr/bin/command
ld-linux
ld-linux.so
ld.so
lerna bootstrap
lerna run build
less
lessecho
lessfile
lesskey
lesspipe
lesspipe.sh
letsencrypt renew
let VAR++
let VAR--
let VAR=1+1
lex
lexgrog
lh_archive
lh_clean
lh_config
lh_source
libnetcfg
libreoffice
libreoffice-base
libreoffice-calc
libreoffice-draw
libreoffice-impress
libreoffice-writer
lightdm
link
lint-staged
linux32
linux64
linux-boot-prober
list_introspect
list_queue
list_user
ln
lnstat
loadkeys
locale
localectl
localedef
local var
locate
lockfile
logger
login
loginctl
logname
logout
logsave
look
lookbib
losetup
lp
lpadmin
lpc
lpinfo
lpmove
lpoptions
lppasswd
lpq
lpr
lprm
lpstat
ls
lsattr
lsblk
lscgroup
lscpu
lsinitrd
lsipc
ls -la
ls -la .git/
lslocks
lslogins
lsmem
lsns
lsof
lsof -i :80
lsof -p pid
lsof -u user
lspci
lspgpot
lsusb
lsusb.py
ltrace
ltrace command
luseradd
luserdel
lusermod
lutris
lwp-download
lwp-mirror
lwp-request
lwp-rget
lxc
lxc-attach
lxc-autostart
lxc-cgroup
lxc-checkconfig
lxc-checkpoint
lxc-config
lxc-console
lxc-copy
lxc-create
lxc-destroy
lxc-device
lxc-execute
lxc-freeze
lxc-info
lxc-ls
lxc-monitor
lxc-snapshot
lxc-start
lxc-stop
lxc-top
lxc-unfreeze
lxc-unshare
lxc-usernsexec
lxc-wait
lz
lz4
lz4c
lz4cat
lzcat
lzcmp
lzdiff
lzegrep
lzfgrep
lzgrep
lzless
lzma
lzmadec
lzmainfo
lzmash
lzmore
m4
mail
mailq
mailx
make
make clean
make install
make uninstall
make_win_binaries
man
manpath
man-recode
mapfile
mattermost
mcookie
md5sum
md5sum file
melm
melm-data
melm-lib.pl
mesg
meson compile -C build
meson setup build
mgetty
microcom
mii-diag
mii-tool
minfo
mkdic
mkdict
mkdir
mkdosfs
mke2fs
mkfifo
mkfs
mkfs.bfs
mkfs.cramfs
mkfs.ext2
mkfs.ext3
mkfs.ext4
mkfs.fat
mkfs.jfs
mkfs.minix
mkfs.msdos
mkfs.ntfs
mkfs.vfat
mkfs.xfs
mkhomedir
mkhomedir_helper
mkinitramfs
mkinitrd
mkisofs
mklost+found
mknod
mkpasswd
mkrescue
mkswap
mktemp
mktemp -d
mktemp -t prefix
mkvextract tracks input.mkv 1:video.mp4 2:audio.aac
mkvmerge -o output.mkv input1.mp4 input2.mp4
mlocate
mmcli
mocha
modinfo
modprobe
modules-config
mogrify
mogrify -resize 50% *.jpg
mongo
mongo database
mongodump --db database
mongo --eval "db.collection.find()"
mongorestore --db database dump/
montage
more
mosh
mosh-client
mosh-server
mount
mountpoint
mpstat
mpv
mpv file.mp4
mpv --loop file.mp4
mpv --mute=yes file.mp4
mpv --speed=1.5 file.mp4
msgattrib
msgcat
msgcmp
msgcomm
msgconv
msgen
msgexec
msgfilter
msgfmt
msggrep
msginit
msgmerge
msgunfmt
msguniq
msql2mysql
mtools
mtr
mtrace
mtr-packet
multipath
multipathd
mutt
mv
mvn
mvn clean install
mvn compile
mvn dependency:tree
mvn package
mvn test
myisamchk
myisam_ftdump
myisamlog
myisampack
my_print_defaults
mypy script.py
mysql
mysqlaccess
mysqlbinlog
mysqlbug
mysqlcheck
mysql_client_test
mysql_config
mysql_convert_table_format
mysqld_multi
mysqld_safe
mysqldump
mysqldumpslow
mysqldump -u user -p database > backup.sql
mysqldump -u user -p database table > table.sql
mysql_find_rows
mysql_fix_extensions
mysqlhotcopy
mysqlimport
mysql_install_db
mysql_plugin
mysql_secure_installation
mysql_setpermission
mysqlshow
mysqlslap
mysqltest
mysql_tzinfo_to_sql
mysql -u
mysql_upgrade
mysql -u user -p
mysql -u user -p database
mysql -u user -p database < backup.sql
mysql -u user -p -e "SHOW DATABASES;"
mysql -u user -p -e "USE db; SHOW TABLES;"
mysql_waitpid
mysql_zap
[ -n "$VAR" ]
namei
nano
nautilus
nawk
nc
ncat
ncurses5-config
ncurses6-config
ndg_httpsclient
ndiff
neqn
nest-simulator
netease-cloud-music
netlify deploy
netplan
netplan-apply
netplan-generate
netplan-try
netreport
netstat
networkctl
newaliases
newgrp
newgrp group
new_tab 工作
new_tab C++开发
new_tab Python开发
newusers
nfs4_editfacl
nfs4_getfacl
nfs4_setfacl
nfsiostat
nfsstat
nfswatch
ngettext
nginx
nginx-debug
nginx -s reload
nginx -s stop
nginx -t
nice
ninja -C build
nisdomainname
njconn
nl
nl -ba file
nl file
nm
nmap
nm-applet
nmap-update
nm binary
nm -C binary
nmcli
nm-connection-editor
nmtui
nmtui-connect
nmtui-edit
nmtui-hostname
node
node --check script.js
nohup
notify-send
npm
npm install
npm run
npm run format
npm run lint
npm run test
npm update
nproc
npx prettier --write .
nroff
nsenter
nslookup
nsupdate
ntpq
ntpstat
ntptime
ntptrace
ntp-wait
numactl
numademo
numastat
nvidia-bug-report.sh
nvidia-modprobe
nvidia-persistenced
nvidia-smi
nvidia-xconfig
nx build project
nx test project
objcopy
objdump
objdump -d binary
objdump -h binary
obs
obsidian
od
od -c file
od -x file
ogg123
oggdec
oggenc
ogginfo
oldfind
omshell
on_ac_power
onlyoffice
openrc
openrc-init
openrc-run
openrc-shutdown
openssl
openssl enc -aes-256-cbc -d -in file.enc -out file
openssl enc -aes-256-cbc -in file -out file.enc
openssl genrsa -out private.key 2048
openssl rand -base64 32
openssl rand -hex 32
openssl req -new -x509 -key private.key -out cert.pem -days 365
openssl rsa -in private.key -pubout -out public.key
openssl s_client -connect host:443
openssl x509 -in cert.pem -text -noout
os-prober
pacat
packer build template.json
pacman
pacmd
pactl
pactl info | grep Server Name
padsp
pandoc input.docx -o output.md
pandoc input.html -o output.pdf
pandoc input.md -o output.docx
pandoc input.md -o output.html
pandoc input.md -o output.pdf
pandoc input.md -s -o output.html
pandoc --pdf-engine=xelatex input.md -o output.pdf
pandoc --toc input.md -o output.pdf
paperconf
paperconfig
paplay
parcel build index.html
parcel index.html
parec
parecord
passwd
passwd -e username
passwd -l username
passwd -S username
passwd username
passwd -u username
paste
patch
pathchk
pax
pbmmake
pbmmask
pbmpage
pbmpscale
pbmreduce
pbmtext
pbmtextps
pbmto10x
pbmtoascii
pbmtoatk
pbmtobbnbg
pbmtocis
pbmtocmuwm
pbmtoepsi
pbmtoepson
pbmtog3
pbmtogem
pbmtogo
pbmtoicon
pbmtolj
pbmtomacp
pbmtomda
pbmtomgr
pbmtonokia
pbmtopgm
pbmtopi3
pbmtopk
pbmtoplot
pbmtoppa
pbmtowinicon
pbmtox10bm
pbmtoxbm
pbmtoybm
pcimodules
pcitweak
pcregrep
pdb
pdb3
pdb3.10
pdf2dsc
pdf2ps
pdf2ps input.pdf output.ps
pdfdetach
pdffonts
pdfimages
pdfinfo
pdfseparate
pdfseparate input.pdf output-%d.pdf
pdftk input.pdf cat 1-5 output output.pdf
pdftk input.pdf cat 1-endodd output odd.pdf
pdftocairo
pdftohtml
pdftoppm
pdftops
pdftotext
pdftotext input.pdf output.txt
pdfunite
pdfunite input1.pdf input2.pdf output.pdf
peekfd
perf
perf record -g command
perf report
perf stat command
perf top
perl
perl5.38.2
perlbug
perldoc
perlthanks
pfbtopfa
pftp
pgawk
pg_dumpall -U user > all_backup.sql
pg_dump -U user database > backup.sql
pgm
pgmkernel
pgrep
pg_restore -U user database < backup.sql
php
php artisan cache:clear
php artisan config:clear
php artisan db:seed
php artisan make:command Command
php artisan make:controller Controller
php artisan make:event Event
php artisan make:factory Factory
php artisan make:job Job
php artisan make:listener Listener
php artisan make:mail Mail
php artisan make:middleware Middleware
php artisan make:migration create_table
php artisan make:model Model
php artisan make:notification Notification
php artisan make:observer Observer
php artisan make:policy Policy
php artisan make:provider Provider
php artisan make:request Request
php artisan make:resource Resource
php artisan make:rule Rule
php artisan make:seeder Seeder
php artisan make:test Test
php artisan migrate
php artisan route:list
php artisan serve
php-config
phpize
pic
pic2graph
piconv
pidof
pidstat
pigz
pinentry
pinentry-curses
pinentry-gnome3
pinentry-gtk-2
pinentry-qt
pinentry-tty
ping
ping4
ping6
pinky
pinky username
pip
pip2
pip3
pip3.10
pip3 freeze > requirements.txt
pip3 install package
pip3 install -r requirements.txt
pip3 install --user package
pip3 list --outdated
pip3 uninstall package
pipenv
pipenv install
pipenv shell
pip freeze
pip install
pip list
pipx
pivot_root
pixieboot
pkaction
pkcheck
pkcon
pkexec
pkg-config
pkgdata
pkgdiff
pkgrm
pkgtool
pkill
pl2pm
pldd
plog
plymouth
plymouth-set-default-theme
pmap
png-fix-itxt
pngtopam
pnpm add package
pnpm install
pnpm update
podman
poetry install
poetry shell
poff
pon
port
post-grohtml
postman
poweroff
ppm3d
ppmbrighten
ppmchange
ppmcie
ppmcolormask
ppmcolors
ppmdim
ppmdist
ppmdither
ppmfade
ppmflash
ppmforge
ppmhist
ppmlabel
ppmmake
ppmmix
ppmnorm
ppmntsc
ppmpat
ppmquant
ppmquantall
ppmqvga
ppmrainbow
ppmrelief
ppmshadow
ppmshift
ppmspread
ppmtoacad
ppmtobmp
ppmtoeyuv
ppmtogif
ppmtoicr
ppmtoilbm
ppmtojpeg
ppmtoleaf
ppmtolj
ppmtomap
ppmtomitsu
ppmtompil
ppmtopcx
ppmtopgm
ppmtopi1
ppmtopict
ppmtopj
ppmtopjxl
ppmtoppm
ppmtopuzz
ppmtorgb3
ppmtosixel
ppmtotga
ppmtouil
ppmtowinicon
ppmtoxpm
ppmtoyuv
ppmtoyuvsplit
ppmtv
pre-commit install
pre-commit run --all-files
preconv
pre-grohtml
prename
prettier --check .
prettier --write script.js
pr file
print
printenv
printenv PATH
printf
printf "Name: %s\n" "value"
pr -l 60 file
prlimit
procps
profmark
prove
prune
ps
ps2ascii
ps2epsi
ps2pdf
ps2pdf12
ps2pdf13
ps2pdf14
ps2pdf input.ps output.pdf
ps2pdfwr
ps2ps
ps2ps2
ps2txt
ps aux
psed
psfaddtable
psfgettable
psfstriptable
psfxtable
psidtopgm
psiod
pslmake
pslog
pspp
psql -U user -d database
psql -U user -d database -c "SELECT * FROM table;"
pstree
ptar
ptardiff
ptargrep
ptx
pulumi config
pulumi destroy
pulumi stack ls
pulumi up
pv
pvchange
pvcreate
pvdisplay
pvmove
pvremove
pvresize
pvs
pvscan
pwck
pwconv
pwd
pwdx
pwhelp
pwunconv
pydoc
pydoc3
pydoc3.10
pyflakes
pygmentize
pylint
pylint script.py
pytest
pytest --cov=module
pytest -k test_name
pytest -v
python
python2
python2.7
python3
python3.10
python3.10-config
python3.10-gdb.py
python3-config
python3 -m py_compile script.py
python-config
python manage.py collectstatic
python manage.py createsuperuser
python manage.py dbshell
python manage.py dumpdata app.Model
python manage.py loaddata fixture
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py shell
python manage.py test
python py文档.py
python --v
pyvenv
qemu-img
qemu-nbd
qemu-system-x86_64
qmgr
qpdf --decrypt input.pdf output.pdf
qperf
quot
quotacheck
quotaoff
quotaon
quotastats
rabbitmqctl list_bindings
rabbitmqctl list_exchanges
rabbitmqctl list_queues
racerun
rake
rake-compiler
rake-compiler0.9.0
rancid-run
rancid-run.in
ranlib
rapache
rarp
ras2tiff
raw
raw2tiff
rawtherapee
rbash
rcp
rdesktop
rdist
rdoc
read
read -a ARRAY
read -d ':' VAR
readelf
readelf -d binary
readelf -h binary
readelf -S binary
readlink
read -n 1 VAR
readonly VAR
read -p "Enter: " VAR
readprofile
read -s -p "Password: " VAR
read -t 5 VAR
read VAR
realpath
reboot
recode-sr-latin
recode UTF-8..GBK file
red
redis-benchmark
redis-check-aof
redis-check-rdb
redis-cli
redis-cli DEL key
redis-cli FLUSHALL
redis-cli GET key
redis-cli -h host -p 6379 -a password
redis-cli INFO
redis-cli KEYS "*"
redis-cli MONITOR
redis-cli ping
redis-cli SET key value
redis-sentinel
redis-server
refile
reindexdb
reiserfsck
reiserfstune
remmina
remove-shell
render
renice
repomanage
repotrack
repquota
reset
resize2fs
resizecons
resizepart
resolvectl
rev
rfkill
rg
ri
rlogin
rm
rmdir
rmmod
rmt
rndc
rndc-confgen
rollup -c
routef
routel
rpcbind
rpcclient
rpcdebug
rpc.gssd
rpc.idmapd
rpcinfo
rpc.nfsd
rpc.sm-notify
rpc.statd
rpm
rpm2archive
rpm2cpio
rpm2cpio package.rpm | cpio -idmv
rpm --checksig package.rpm
rpmdb
rpm -e package
rpmgraph
rpm --import GPG-KEY
rpm -ivh package.rpm
rpmkeys
rpmlint
rpm -qa
rpm -qc package
rpm -qd package
rpm -qf /path/to/file
rpm -qi package
rpm -ql package
rpm -q package
rpm -qR package
rpmsign
rpmspec
rpm -Uvh package.rpm
rpm -Va
rsh
rsync
rsyslogd
rtacct
rtcwake
rtmon
rtpr
rtstat
ruby
runcon
runlevel
run-parts
runuser
rush build
rustc main.rs
rustfmt src/main.rs
rustup default stable
rustup update
rview
rvim
s2p
s3cmd
sa1
sa2
sadc
sadf
sam deploy --guided
sam local invoke Function
sar
sass
sass-convert
savelog
savetty
sbct
sbd
sbi
sbic
sbplot
sbrsh
sclient
scons
scp
screen
screenconfig
screenfetch
script
script -a output.log
script -c command output.log
scriptlive
script output.log
scriptreplay
scriptreplay timing.log output.log
. script.sh
./script.sh
script -t 2> timing.log -a output.log
sdiff
sdptool
sealert
secon
sed
sed -i 's/\r$//' file
seed
seinfo
selabel_digest
selabel_lookup
selabel_lookup_best_match
selabel_partial_match
select option in opt1 opt2 opt3; do echo $option; break; done
selinuxconlist
selinuxdefcon
selinuxenabled
selinuxexeccon
semanage
semantic-release
semodule
semodule_package
semodule_unpackage
sepermit.conf
seq 10
seq 1 0.5 5
seq 1 2 10
seq -s, 1 10
seq -w 1 100
serverless deploy
serverless logs -f function
service
sestatus
set
setarch
setcap
setcifsacl
setenforce
setfacl
setfattr
setfont
setkey
setkeycodes
setleds
setlogcons
setmetamode
setpci
setpriv
setsid
setterm
setup
setupcon
setup-nsssysinit.sh
setvtrgb
sfdisk
sftp
sg
sg group -c "command"
sginfo
sh
sha1sum
sha1sum file
sha224sum
sha256sum
sha256sum file
sha384sum
sha512sum
sha512sum file
shar
showconsolefont
showkey
shred
sh script.sh
shuf
shuf -e a b c d
shuf file
shuf -i 1-100 -n 10
shuf -n 10 file
shutdown
sigdist
simpleburn
size binary
skill
slabtop
slack
sleep 1h
sleep 1m
sleep 5
slim
sln
slogin
sls deploy function -f function_name
smartctl
smartd
smbcquotas
smbget
smbpasswd
smbspool
smbstatus
smbtar
smbtree
smime
snap
snapctl
snapd
snap disable package
snap enable package
snapfuse
snap info package
snap install
snap install package
snap list
snap logs package
snap refresh
snap remove package
snap revert package
snap services
snice
snmpbulkget
snmpbulkwalk
snmpconf
snmpdelta
snmpdf
snmpget
snmpgetnext
snmpinform
snmpnetstat
snmpset
snmpstatus
snmptable
snmptest
snmptranslate
snmptrap
snmpusm
snmpvacm
snmpwalk
sntp
snxc
soelim
sort
source
source script.sh
sox input.wav output.wav
sox input.wav output.wav reverse
sox input.wav output.wav speed 1.5
sox -n output.wav synth 5 sine 440
spax
speech-dispatcher
speedtest-cli
spell
spf
spice-client
spice-gtk
splain
split
splitfont
spotify
sprof
sqlite3
sqlite3 database.db
sqlite3 database.db < commands.sql
sqlite3 database.db ".dump"
sqlite3 database.db ".restore backup.sql"
sqlite3 database.db ".schema"
sqlite3 database.db "SELECT * FROM table;"
sqlite3 database.db ".tables"
squid
squidclient
ss
ssh
ssh-add
ssh-agent
ssh-argv0
ssh-copy-id
sshd
sshfs
ssh-keygen
ssh-keygen -t ed25519 -f key
ssh-keygen -t rsa -b 4096 -f key
ssh-keyscan
ssh-pkcs11-helper
ssl
sslscan
sssd
stack build
standard-version
stap
stap-prep
stap-report
start-stop-daemon
stat
staticcheck ./...
stdbuf
steam
steam-native
strace
strace command
strace -f command
strace -p pid
stream
streamlink URL 720p
streamlink URL best
strings
strings -a file
strings binary
strings file
strings -n 10 file
strip
strip binary
stty
stylelint "*.css"
su
su -c "command" username
sudo
sudo command
sudo dnf install easyeffects
sudo -i
sudo -k
sudo -l
sudoreplay
sudo -s
sudo -u user command
sudo -v
sulogin
sum
supervisorctl restart all
supervisorctl start all
supervisorctl status
supervisorctl stop all
supervisord
su-to-root
su - username
svc
svg2pdf
svg2png
svgconvert
svn
svnadmin
svnauthz
svnauthz-validate
svndumpfilter
svnfsfs
svnlook
svnmucc
svn-populate-node-origins-index
svnrdump
svnserve
svnsync
svnversion
swaplabel
swapoff
swapon
swig
symfony console cache:clear
symfony console doctrine:migrations:migrate
symfony console make:controller
symfony console make:entity
symfony new project
symfony server:start
sync
synclient
syndaemon
sysctl
sysdig
systemctl
systemctl disable
systemctl enable
systemctl reload apache2
systemctl reload nginx
systemctl start
systemctl status
systemctl status cron
systemctl status crond
systemctl stop
systemd
systemd-analyze
systemd-ask-password
systemd-cat
systemd-cgls
systemd-cgtop
systemd-delta
systemd-detect-virt
systemd-escape
systemd-id128
systemd-inhibit
systemd-machine-id-setup
systemd-mount
systemd-notify
systemd-nspawn
systemd-path
systemd-resolve
systemd-run
systemd-socket-activate
systemd-stdio-bridge
systemd-sysusers
systemd-tmpfiles
systemd-tty-ask-password-agent
systemd-umount
systool
tabs
tac
tail
tailf
tail -f /var/log/apache2/access.log
tail -f /var/log/apache2/error.log
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
talk
tar
tar -czvf
tar -xzvf
taskset
tbl
tcpdump
tcpflow
tcpslice
tcptraceroute
tcsh
tee
tee -a file
tee file
telegram-desktop
telinit
telnet
terraform
terraform apply
terraform destroy
terraform fmt
terraform init
terraform output
terraform plan
terraform show
terraform state list
terraform validate
terraform workspace list
terraform workspace new name
test
test "$VAR" -eq 1
test "$VAR" -ge 1
test "$VAR" -gt 1
test "$VAR" -le 1
test "$VAR" -lt 1
test "$VAR" -ne 1
test "$VAR" != "value"
test "$VAR" = "value"
test -d dir
test -f file
test -n "$VAR"
testparm
test -r file
test -s file
test -w file
test -x file
test -z "$VAR"
texconfig
texconfig-dialog
texconfig-sys
texhash
texlinks
texlua
texluac
tfmtodit
tftopl
tgkill
thinkjettopbm
thunderbird
tic
tiff2bw
tiff2pdf
tiff2ps
tiff2rgba
tiffcmp
tiffcp
tiffcrop
tiffdither
tiffdump
tiffgt
tiffinfo
tiffmedian
tiffset
tiffsplit
time
time command
timedatectl
timeout
timeout 10 command
timeout -s KILL 10 command
times
tload
tmux
tn5250
toe
top
touch
tput
tr
tracepath
tracepath6
traceroute
traceroute6
transmission-gtk
traptoemail
tr -d '\r' < file > newfile
tree
troff
true
truncate
tsc
tsc --noEmit
tsc --watch
tset
tsort
tty
tunctl
tune2fs
tunefs.ocfs2
tunelp
turbo run build
twopi
txt2man
txt2man.sh
typeset
typora
tzconfig
tzselect
ua
ubuntu-advantage
ubuntu-bug
ubuntu-core-launcher
ubuntu-distro-info
ubuntu-report
ubuntu-security-status
ubuntu-support-status
ucf
ucfq
ucfr
udevadm
udisksctl
ufw
ul
ulockmgr_server
umask
umount
unalias
unalias alias_name
uname
uname -a
uname -m
uname -n
uname -o
uname -r
uname -s
uname -v
uncompress
unexpand
unexpand -a file > newfile
unicode_start
unicode_stop
uniq
unix2dos file
unix_chkpwd
unix_update
unlink
unlz4
unlzma
unpack200
unpigz
unset VAR
unshare
unxz
unzip
unzipsfx
update-alternatives
update-ca-certificates
update-cracklib
updatedb
update-desktop-database
update-gdk-pixbuf-loaders
update-gtk-immodules
update-icon-caches
update-inetd
update-initramfs
update-locale
update-mime
update-pciids
update-perl-sax-parsers
update-python-modules
update-rc.d
update-usbids
update-xmlcatalog
upower
uptime
uptime -p
uptime -s
urlgrabber
usb-devices
usbhid-dump
useradd
useradd -G group1,group2 username
useradd -m -s /bin/bash username
useradd -m username
useradd username
userdel
userdel -r username
userdel username
usermod
usermod -aG group username
usermod -d /new/home -m username
usermod -l newname oldname
usermod -L username
usermod -s /bin/zsh username
usermod -U username
users
usleep
/usr/bin/time -v command
utmpdump
uuidd
uuidgen
uuidparse
uvicorn main:app --host 0.0.0.0 --port 8000
uvicorn main:app --reload
uz
vagrant box add box_name
vagrant box list
vagrant destroy
vagrant halt
vagrant ssh
vagrant status
vagrant up
valgrind --leak-check=full ./program
valgrind --tool=cachegrind ./program
valgrind --tool=callgrind ./program
valgrind --tool=memcheck ./program
(( VAR++ ))
(( VAR-- ))
(( VAR > 1 ))
(( VAR+=1 ))
vault kv get secret/key
vault kv put secret/key value=vault
vault secrets enable kv
vault status
vdir
vercel deploy
vercel logs
vi
view
vim
vim.basic
vimdiff
vim.tiny
vimtutor
vipw
virtualenv
visual-studio-code
visudo
vite build
vite dev
vlc
vlc file.mp4
vmstat
volname
w
waf configure build
wait
wait $!
wall
watch
watchgnupg
wc
wdctl
webpack-dev-server
webpack --mode production
wechat
wget
whatis
whereis
which
whiptail
who
whoami
windmc
windres
wine
wine64
wine64-preloader
wineboot
winebuild
winecfg
wineconsole
winedbg
winedump
winefile
winegcc
winemaker
winemine
winepath
wine-preloader
wineserver
wipefs
wish
wish8.6
wn
wnbrowse
wnctrl
word-list-compress
wpa_cli
wpa_passphrase
wpa_supplicant
write
wsdl2h
wtf
www-browser
X
x11perf
x11perfcomp
x3270
x3270if
x86_64
x86_64-linux-gnu-addr2line
x86_64-linux-gnu-ar
x86_64-linux-gnu-as
x86_64-linux-gnu-c++filt
x86_64-linux-gnu-dwp
x86_64-linux-gnu-elfedit
x86_64-linux-gnu-g++
x86_64-linux-gnu-gcc
x86_64-linux-gnu-gcc-ar
x86_64-linux-gnu-gcc-nm
x86_64-linux-gnu-gcc-ranlib
x86_64-linux-gnu-gcov
x86_64-linux-gnu-gcov-dump
x86_64-linux-gnu-gcov-tool
x86_64-linux-gnu-gold
x86_64-linux-gnu-gprof
x86_64-linux-gnu-ld
x86_64-linux-gnu-ld.bfd
x86_64-linux-gnu-ld.gold
x86_64-linux-gnu-nm
x86_64-linux-gnu-objcopy
x86_64-linux-gnu-objdump
x86_64-linux-gnu-ranlib
x86_64-linux-gnu-readelf
x86_64-linux-gnu-size
x86_64-linux-gnu-strings
x86_64-linux-gnu-strip
x86_64-redhat-linux-ar
x86_64-redhat-linux-as
x86_64-redhat-linux-c++filt
x86_64-redhat-linux-elfedit
x86_64-redhat-linux-g++
x86_64-redhat-linux-gcc
x86_64-redhat-linux-gcc-ar
x86_64-redhat-linux-gcc-nm
x86_64-redhat-linux-gcc-ranlib
x86_64-redhat-linux-gcov
x86_64-redhat-linux-gcov-dump
x86_64-redhat-linux-gcov-tool
x86_64-redhat-linux-gold
x86_64-redhat-linux-gprof
x86_64-redhat-linux-ld
x86_64-redhat-linux-ld.bfd
x86_64-redhat-linux-ld.gold
x86_64-redhat-linux-nm
x86_64-redhat-linux-objcopy
x86_64-redhat-linux-objdump
x86_64-redhat-linux-ranlib
x86_64-redhat-linux-readelf
x86_64-redhat-linux-size
x86_64-redhat-linux-strings
x86_64-redhat-linux-strip
xargs
xauth
xbacklight
xbiff
xcalc
xclipboard
xclock
xcmsdb
xconsole
xcutsel
xdg-desktop-icon
xdg-desktop-menu
xdg-email
xdg-icon-resource
xdg-mime
xdg-open
xdg-screensaver
xdg-settings
xdg-user-dir
xdg-user-dirs-update
xditview
xdpyinfo
xdriinfo
xedit
xev
xeyes
xfd
xfisheye
xfontsel
xfs_admin
xfs_bmap
xfs_copy
xfs_db
xfsdump
xfs_estimate
xfs_freeze
xfs_fsr
xfs_growfs
xfs_info
xfsinvutil
xfs_io
xfs_logprint
xfs_mdrestore
xfs_metadump
xfs_mkfile
xfs_ncheck
xfs_quota
xfs_repair
xfsrestore
xfs_rtcp
xfs_scrub
xfs_scrub_all
xfs_spaceman
xgamma
xgc
xhost
xinit
xinput
xkbbell
xkbcomp
xkbevd
xkbprint
xkbvleds
xkbwatch
xkill
xload
xlogo
xlsatoms
xlsclients
xlsfonts
xmag
xman
xmessage
xmodmap
xmore
xmsg
xprop
xrandr
xrdb
xrefresh
xscope
xscreensaver
xscreensaver-command
xsd
xset
xsetbg
xsetmode
xsetpointer
xsetroot
xsm
xstdcmap
xsubpp
xterm
xvinfo
xwd
xwininfo
xwud
xxd
xxd binary
xxd file
xxd -r file
xz
xzcat
xzcmp
xzdec
xzdiff
xzegrep
xzfgrep
xzgrep
xzless
xzmore
yacc
yapf --in-place script.py
yarn add package
yarn audit
yarn install
yarn outdated
yarn remove package
yarn upgrade
yelp
yelp-build
yelp-check
yelp-new
yes
yes | rm -r dir
yes "string"
youtube-dl URL
ypbind
ypdomainname
ypmatch
yppasswd
yppoll
yppush
ypserv
ypset
yptest
ypwhich
ypxfr
yt-dlp
yt-dlp --embed-subs URL
yt-dlp -f best URL
yt-dlp URL
yt-dlp --write-sub URL
yt-dlp -x --audio-format mp3 URL
yum
yum-builddep
yum clean all
yum-complete-transaction
yum-config-manager
yum-debug-dump
yum-debug-restore
yumdownloader
yum-groups-manager
yum history
yum info package
yum install
yum install package
yum list
yum list installed
yum makecache
yum provides command
yum remove package
yum search keyword
yum update
[ -z "$VAR" ]
zcat
zcmp
zdiff
zegrep
zfgrep
zforce
zgrep
zip
zipcloak
zipdetails
zipgrep
zipinfo
zipnote
zipsplit
zless
zmore
znew
zoom
zsh
zsoelim
/bin/python /home/ice/桌面/python/python2.py
iflow
spf
sudo -v
spf
/bin/python /home/ice/桌面/命令查询工具.py
/bin/python /home/ice/桌面/命令查询工具.py
