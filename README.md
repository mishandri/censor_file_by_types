# Censor files by types
Program removes all new files that do not match the extensions

# Requirements
WatchDog library is required
```python
    pip install watchdog
```
# Describe
source_path.txt (in the same folder with "censor_file_type.py")

    List of directories. Don't intersect directories

file_types.txt (in the same folder with "censor_file_type.py")
    
    List of filetypes, that don't remove
    
# Attention
Program don't remove files, that already exist, be carefully
