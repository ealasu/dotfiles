#!/bin/bash
set -e

src_dev=/dev/mmcblk1p1

confirm () {
    # call with a prompt string or use a default
    read -r -p "${1:-Are you sure? [y/N]} " response
    case $response in
        [yY][eE][sS]|[yY]) 
            true
            ;;
        *)
            false
            ;;
    esac
}

sudo umount /mnt/sd || true
sudo umount /mnt/hdd || true

sudo mount $src_dev /mnt/sd
sudo mount /dev/sda1 /mnt/hdd

name=$1
if [ -z $name ]; then
  echo 'must specify a name for the destination folder'
  exit 1
fi
echo $name

src=/mnt/sd/DCIM
dest="/mnt/hdd/data/Pictures/CanonEOS60D/$name"

if [ -d $dest ]; then
  echo "dest already exists, make sure you're not overwriting stuff"
  exit 1
fi

mkdir $dest

rsync -av --progress $src $dest

confirm 'delete photos from SD card?' && sudo rm -rf $src

sudo umount /mnt/sd
