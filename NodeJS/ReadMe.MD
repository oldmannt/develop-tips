
### new node typescript project
https://code.visualstudio.com/docs/languages/typescript  
setting "typescript.referencesCodeLens.enabled": true  
setting "typescript.implementationsCodeLens.enabled": true  

code navigation  
https://code.visualstudio.com/docs/editor/editingevolved  

debugging  
https://code.visualstudio.com/docs/editor/debugging  

node debugging  
https://code.visualstudio.com/docs/nodejs/nodejs-debugging  

``` shell
npm init -y // setup package.json
npm install -D typescript
npm install -D @type/node
tsc --init // generate tsconfig.json
```
tsconfig.json
``` json
{
    "compilerOptions": {
        "module": "commonjs",
        "esModuleInterop": true,
        "target": "es6",
        "noImplicitAny": true,
        "moduleResolution": "node",
        "sourceMap": true,
        "outDir": "dist",
        "baseUrl": ".",
        "paths": {
            "*": [
                "node_modules/*",
                "src/types/*"
            ]
        }
    },
    "include": [
        "src/**/*"
    ]
}
```
tslint.json
get latest from https://github.com/Microsoft/TypeScript-Node-Starter/blob/master/tslint.json

.vscode/launch.json
``` json
{
    "version": "0.2.0",
    "configurations": [        
        {
            "type": "node",
            "request": "launch",
            "name": "Launch Program",
            "program": "${workspaceFolder}/dist/server.js"
        }
    ]
}
```
Add scripts to package.json
get latest from https://github.com/Microsoft/TypeScript-Node-Starter/blob/master/package.json

### migrate to typescript
``` shell
$npm install -g typescript  // install tsc
$npm install -g ts-node
$npm install -g tslint 
$tsc --init // generate tsconfig.json
$npm install -D @types/express
```
