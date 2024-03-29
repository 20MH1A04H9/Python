
# Windows 11/10 Delete the recovery Partition

Deleting recovery partitions could potentially lead to problems if you ever need to use system recovery options. If you have Windows Recovery Environment (WinRE) disabled and you delete the recovery partitions, it will not reactivate WinRE because the system can’t find the recovery environment


## Below are the steps for deleting a recovery partition

1.Open the Disk Management tool.

2.In Disk Management Utility, locate the recovery partition you want to delete.

3.open CMD.exe and Type:


```bash
  diskpart
```
Type select disk 0 and hit Enter
```bash
  select disk 0
```
Type select partition 4 and hit Enter
```bash
  select partition 5
```
Type delete partition override and hit Enter
```bash
  delete partition override
```

    
