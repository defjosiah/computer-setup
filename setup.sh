# Set up new computer. Assume execution from home directory (/Users/$USER)
# and ability to use sudo
# Also assume installation of:
# 1. Dropbox (including signed in account)
# 2. Sublime Text 3
# 3. iterm2
# 4. Alfred (I might add a folder for alfred plugins here)
# 5. Spotify (no reason for this really)

# install xcode command line tools
xcode-select --install

echo "installing homebrew"
# install homebrew
which -s brew
if [[ $? != 0 ]] ; then
    # http://brew.sh
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
else
    brew update
fi

# install commonly used brew applications
# Install GNU core utilities (those that come with OS X are outdated)
brew install coreutils

# Install GNU `find`, `locate`, `updatedb`, and `xargs`, g-prefixed
brew install findutils

# Install Bash 4
brew install bash

# Install more recent versions of some OS X tools
brew tap homebrew/dupes
brew install homebrew/dupes/grep

$PATH=$(brew --prefix coreutils)/libexec/gnubin:$PATH

binaries=(
  ack
  git
  fpp
  httpie
  jq
  watchman
  wget
  tree
)

echo "installing homebrew applications..."
brew install ${binaries[@]}

# install oh-my-zsh
echo "installing oh-my-zsh..."
if [ ! -d "/Users/$USER/.oh-my-zsh" ]; then
	sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
fi

# setup computer to match dropbox configuration
echo "symlinking dropbox..."
python $(pwd)/setup-dropbox.py
