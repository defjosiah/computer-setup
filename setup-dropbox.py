import os

#The sync directory (~/Dropbox) and the symlink directory "~" just happen
#to be based off of the home environmental variable
sync_directory = os.path.join(os.environ["HOME"], "Dropbox")
symlink_directory = os.path.join(os.environ["HOME"], "Documents")
media_directory = os.path.join(sync_directory, "media")

mirror_top_directories = ["dev", "personal"]
mirror_media_directories = ["Pictures"]

def is_clean_symlink(test_file):
    print test_file
    return (not os.path.isdir(os.path.join(symlink_directory, test_file)) and
            os.path.isdir(os.path.join(sync_directory, test_file)))

def link_dropbox():
    symlink_with_filter(sync_directory, symlink_directory, mirror_top_directories)

def link_media():
    symlink_with_filter(media_directory, os.environ["HOME"], mirror_media_directories)

def symlink_with_filter(base_directory, sym_directory, file_list):
    map(lambda x: os.symlink(os.path.join(base_directory, x), os.path.join(sym_directory, x)),
        filter(is_clean_symlink, file_list))

if __name__ == '__main__':
    link_dropbox()
    link_media()