# Minify-JSON-Action
GitHub Action to minify JSON files for upload.

## General
This action takes a JSON input file and removes any whitespace and line breaks. By default file paths are relative to your current working directory.

## Parameters
| Parameter | Status | Description
| --- | --- | ---
| input_file | required | The JSON input file to load and minify.
| output_file | optional | The file to write the minified JSON to. If omitted overwrites the input file.

## Example Usage
```YAML
on:
  push:
    branches: [main]
  workflow_dispatch:
name: Deploy
jobs:
  web-deploy:
    name: Deploy
    runs-on: ubuntu-latest
    steps:
    - name: [Checkout your files or create a new one]
    
    - name: Minify JSON
      uses: StefanEnsmann/Minify-JSON-Action@1.1.0
      with:
        input_file: input.json
        output_file: output.json
    
    - name: [Do what you want with the minified file]
```
