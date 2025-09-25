---
title: Guide to LVM on Ubuntu
pubDatetime: 2025-09-23
featured: false
tags:
  - Hands On Lab
  - Linux
  - LVM
description: A Beginner's Guide to LVM on Ubuntu
---



## A Beginner's Guide to LVM on Ubuntu

LVM, or **Logical Volume Management**, is a powerful tool that provides a more flexible way to manage storage than traditional partitioning. It allows you to resize, move, and create file systems without worrying about the physical layout of the hard drive. Here's a step-by-step guide for a beginner to practice LVM on an Ubuntu system, using a virtual machine is highly recommended for this practice.

-----

### Install LVM2

First, you need to ensure the LVM2 package is installed on your Ubuntu system. Open a terminal and run the following command:

```bash
sudo apt update && sudo apt install lvm2 -y
```

  * **sudo**: This command is used to execute a command with superuser privileges, which are required to install software and manage system configurations.
  * **apt update**: This command updates the list of available packages and their versions from the repositories.
  * **apt install lvm2**: This command installs the LVM2 package.
  * **-y**: This flag automatically answers "yes" to any prompts, making the installation non-interactive.

-----

### Create a Physical Volume (PV)

A **physical volume (PV)** is a physical disk or partition that is designated for use by LVM. It's the building block of an LVM setup. For this guide, we'll assume you have a spare disk named `/dev/sdc`. If you don't have a spare disk, you can create a partition on an existing disk and use that. Use the following command to create a PV:

![output](@/assets/images/Screenshot_20250924_045117.png)

```bash
sudo pvcreate /dev/xvdc
```

  * **pvcreate**: This command initializes a physical volume for use by LVM.
  * **/dev/sdb**: This is the name of the disk you are using. **Important**: Make sure to replace this with the correct device name on your system. You can use `lsblk` to list your disks.

To check the status of your newly created physical volume, use the `pvdisplay` command:

```bash
sudo pvdisplay
# or 
sudo pvs
```
  * **pvdisplay**: This command displays the attributes of physical volumes, showing information like the PV name, size, and whether it's part of a volume group.

  * **pvs**: This commands displays the short summary of physical volumes.

-----

### Create a Volume Group (VG)

A **volume group (VG)** pools one or more physical volumes into a single logical entity. It's the central storage space from which you'll create logical volumes. Create a VG named `janak-vg` using your new physical volume:

![output](@/assets/images/Screenshot_20250924_045742.png)


```bash
sudo vgcreate janak-vg /dev/xvdb
```

  * **vgcreate**: This command creates a new volume group.
  * **janak-vg**: This is the name you are giving to your new volume group. You can name it anything you like.
  * **/dev/sdb**: This is the PV you are adding to the VG.

To verify the creation of the volume group, you can use the `vgdisplay` command:

```bash
sudo vgdisplay
# or
sudo vgs
```

  * **vgdisplay**: This command displays the attributes of volume groups, including the VG name, size, and the number of physical volumes it contains.

---

### Extend the Volume Group. 

* Use the **`vgextend`** command to add the newly created PV to your existing volume group.

![output](@/assets/images/Screenshot_20250924_050244.png)

    ```bash
    sudo vgextend janak-vg /dev/xbdc
    ```

    (Replace `janak-vg` with the name of your volume group, e.g., `janak-vg`.)

---

### Create a Logical Volume (LV)

A **logical volume (LV)** is the equivalent of a partition in a traditional setup. It's a "virtual" partition created from the free space in a volume group. This is the volume that you will format and mount. Create a 5GB logical volume named `janak-data-lv` within `janak-vg`:

![output](@/assets/images/Screenshot_20250924_052950.png)

```bash
sudo lvcreate -L 550G -n janak-data-lv janak-vg
```

  * **lvcreate**: This command creates a new logical volume.
  * **-L 5G**: This flag specifies the size of the logical volume. `5G` means 5 gigabytes.
  * **-n janak-data-lv**: This flag specifies the name of the new logical volume.
  * **janak-vg**: This is the name of the volume group from which the LV will be created.

To see your new logical volume, use the `lvdisplay` command:

```bash
sudo lvdisplay
# or
sudo lvs
```

  * **lvdisplay**: This command displays the attributes of logical volumes, including the LV path, size, and the volume group it belongs to.

-----

### Format and Mount the Logical Volume

![output](@/assets/images/Screenshot_20250924_053608.png)

The logical volume is now a raw block device and needs to be formatted with a file system before it can be used. We'll use the `ext4` file system. The path to your new LV will be `/dev/janak-vg/janak-data-lv`.

```bash
sudo mkfs.ext4 /dev/janak-vg/janak-data-lv
```

  * **mkfs.ext4**: This command creates an ext4 file system on the specified device. `mkfs` stands for "make file system."
  * **/dev/janak-vg/janak-data-lv**: This is the full path to your new logical volume. LVM creates a symbolic link to the device file in the `/dev` directory.

Now that the LV is formatted, you can mount it to make it accessible to your system. First, create a mount point, which is a directory where the LV will be attached.

```bash
sudo mkdir -p /mnt/data
```

  * **mkdir**: This command creates a new directory.
  * **-p** → the `-p` flag means **"parents"**.
    * It creates **all necessary parent directories** if they don’t exist (e.g., `/mnt` and then `/mnt/data`).
    * If the directory already exists, it **does not throw an error** — it just silently succeeds.

  * **/mnt/data**: This is the name of the directory where you will mount the LV. You can choose any name and location.

Next, mount the logical volume to the new directory:

```bash
sudo mount /dev/janak-vg/janak-data-lv /mnt/data
```

  * **mount**: This command attaches the file system from a device to a directory.
  * **/dev/janak-vg/janak-data-lv**: The source device to be mounted.
  * **/mnt/data**: The destination mount point.

To verify that the volume is mounted, you can use the `df -h` command:

```bash
df -h
```

  * **df**: This command reports file system disk space usage.
  * **-h**: This flag displays the output in a human-readable format (e.g., using M for megabytes, G for gigabytes).

You have now successfully created, formatted, and mounted a logical volume using LVM\!

-----

###  Resize a Logical Volume (LV)

One of the main benefits of LVM is the ability to **easily resize logical volumes**. Let's extend our LV to 555GB.

![output](@/assets/images/Screenshot_20250924_055649.png)

First, you need to extend the logical volume itself:

```bash
sudo lvextend -L +5G /dev/janak-vg/janak-data-lv
```

  * **lvextend**: This command extends the size of a logical volume.
  * **-L +2G**: This flag specifies that you want to **add** 2 gigabytes to the existing size. You can also specify the final size directly (e.g., `-L 7G`).

Next, you must **resize the file system** on the logical volume to recognize the new space. For `ext4`, use `resize2fs`:

```bash
sudo resize2fs /dev/janak-vg/janak-data-lv
```

  * **resize2fs**: This command resizes ext2, ext3, or ext4 file systems. It will automatically detect the new size of the underlying logical volume.

Use `df -h` again to confirm the new size. The logical volume should now show as 7GB.

### Remove the Logical Volume: 


To remove a logical volume (LV), you must first unmount it if it's currently in use. After unmounting, you can use the `lvremove` command to delete it.


#### Unmount the Logical Volume 

First, determine if the logical volume is mounted. You can use the `df -h` command to see a list of mounted filesystems. Look for the logical volume you want to remove, which will likely be listed as  `/dev/VG_name/LV_name`.

Once you've identified its mount point, use the `umount` command to unmount it.

```bash
sudo umount /mnt/data
```


####  Remove the Logical Volume

After confirming the logical volume is unmounted, you can safely remove it using `lvremove`. **This action is permanent and will delete all data on the volume.**

```bash
sudo lvremove /dev/janak-vg/janak-data-lv
```

---

### Remove the volume group:

To remove a volume group (VG), you must first remove all the logical volumes (LVs) residing within it. This is a critical safety measure to prevent data loss. Once the logical volumes are gone, you can remove the volume group itself.

![output](@/assets/images/Screenshot_20250924_060847.png)

```bash
sudo vgremove janak-vg
```


---


### Remove the Physical Volume from the Volume Group 

You'll use the **`vgreduce`** command to remove `/dev/xvdc` from the `janak-vg` volume group. Since there are no logical volumes (LVs) or data on this physical volume, this command will execute without any issues.

![output](@/assets/images/Screenshot_20250924_050719.png)

```bash
sudo vgreduce janak-vg /dev/xvdc
```

---

## Remove the physical volume:

![output](@/assets/images/Screenshot_20250924_061127.png)


```bash
sudo pvremove /dev/xvdb
```

Your `/dev/xvdb` disk is now back to its initial state.
