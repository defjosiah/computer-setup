import os

#The sync directory (~/Dropbox) and the symlink directory "~" just happen
#to be based off of the home environmental variable
sync_directory = os.path.join(os.environ["HOME"], "Dropbox")
symlink_directory = os.environ["HOME"]
mirror_top_directories = ["dev", "personal"]

def is_clean_symlink(test_file):
    return (not os.path.isdir(os.path.join(symlink_directory, test_file)) and
            os.path.isdir(os.path.join(sync_directory, test_file)))

def link_dropbox():
    map(lambda x: os.symlink(os.path.join(sync_directory, x), os.path.join(symlink_directory, x)),
        filter(lambda x: is_clean_symlink(x), mirror_top_directories))

if __name__ == '__main__':
    link_dropbox()