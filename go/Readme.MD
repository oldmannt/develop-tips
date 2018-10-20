#### env
   1. Install Homebrew
``` sh
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
   2. Install GO
``` sh
    brew update && brew upgrade
    brew install go
```

    3. .bash_profile
```
    export GOROOT="/usr/local/Cellar/go/1.11.1/libexec"
    export GOPATH="/Users/llin/go"
    export GOBIN=$GOROOT/bin
    export PATH=$PATH:$GOROOT/bin
```
    4. install vscode and go extension
    5. configue vs code
``` json
{
    "go.autocompleteUnimportedPackages": true,
    "go.gopath": "/Users/llin/go",
    "go.delveConfig": {
        "apiVersion": 2,
        "dlvLoadConfig": {
            "followPointers": true,
            "maxVariableRecurse": 1,
            "maxStringLen": 64,
            "maxArrayValues": 64,
            "maxStructFields": -1
        }
    }
}
```
    6. vscode debuger
    https://github.com/Microsoft/vscode-go/wiki/Debugging-Go-code-using-VS-Code
    https://github.com/derekparker/delve/blob/master/Documentation/installation/osx/install.md
    install delve
``` sh
    xcode-select --install
    go get -u github.com/derekparker/delve/cmd/dlv
    cd $GOPATH/src/github.com/derekparker/delve
    make install
    // if can't find  github.com/spf13/cobra/cobra
     go get -u github.com/spf13/cobra/cobra // then make install again
```
