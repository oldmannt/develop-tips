
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

## typescript

### declare keywords
Declare vs. var  
var creates a new variable. declare is used to tell TypeScript that the variable has been created elsewhere. If you use declare, nothing is added to the JavaScript that is generated - it is simply a hint to the compiler.  

For example, if you use an external script that defines var externalModule, you would use declare var externalModule to hint to the TypeScript compiler that externalModule has already been set up  

### this
Any access to this keyword within a function is actually controlled by how the function is actually called. It is commonly referred to as the “calling context.”  
``` typescript
function foo() {
  console.log(this);
}

foo(); // logs out the global e.g. `window` in browsers
let bar = {
  foo
}
bar.foo(); // Logs out `bar` as `foo` was called on `bar`
```

### import {}
An import declaration of the form
```sh
import d from "mod";
```
is exactly equivalent to the import declaration
```sh
import { default as d } from "mod";
```
we would omit the braces only when you are importing something that was exported as the `default` entity of the module (with an `export default` declaration, of which there can only be one per module). The name you provide in the `import` declaration becomes an alias for that imported entity.  
When importing anything else, even if it's just one entity, you need to provide the braces.

