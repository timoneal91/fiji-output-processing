This is a simple application that processes FIJI output

Simply run:

- `$ python3 main.py "<absolute_path_to_root>"`

Your output will then be in the supplied root.

To get the path you should use, use a Terminal to `cd` into it, then use `pwd`:

```
Joshs-rMBP:~ josh$ cd Desktop/Self-admin\ data/dMSN-hM4Di/
Joshs-rMBP:dMSN-hM4Di josh$ pwd
/Users/josh/Desktop/Self-admin data/dMSN-hM4Di
```

Here we would then use:

- `$ python3 main.py "/Users/josh/Desktop/Self-admin data/dMSN-hM4Di"`

To setup Python 3 on a fresh Mac OS:

- `$ cd ~/Desktop`
- `$ git clone https://github.com/timoneal91/msn-dreadd.git`
- `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
- `$ echo 'export PATH="$PATH:/usr/local/bin"' >> ~/.bash_profile`
- `$ brew install python3`
- `$ brew postinstall python3`