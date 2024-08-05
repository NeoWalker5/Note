
# opt/homebrew/etc/rsyncd.conf
use chroot = no
max connections = 4
pid file = /var/run/rsyncd.pid
lock file = /var/run/rsync.lock
log file = /var/log/rsyncd.log

[merge_server_test]
path = /Users/neo/Documents/www
comment = My shared folder
uid = neo
gid = staff
read only = no
list = yes
auth users = neo
secrets file = /etc/rsyncd.secrets
fake super = yes


# test
rsync -avz --port 873 /Users/neo/Documents/rstest/ neo@localhost::merge_server_test
sudo nano /etc/rsyncd.secrets
sudo nano /opt/homebrew/etc/rsyncd.conf

sudo pkill rsync
sudo rsync --daemon

chmod -R 755 /Users/neo/Documents/www

