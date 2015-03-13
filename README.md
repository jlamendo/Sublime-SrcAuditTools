# Sublime-SrcAuditTools
Some useful tools for source review in sublime text.
# Modules:

## Copy With Line Numbers:
Select some text, right click and hit copy with line numbers. 
A markdown formatted 
 \`\`\`
 \`\`\`
 
 block will be copied into the clipboard with line numbers, and a link with a corresponding subl:// url to the file.
 To save it as a file directly rather than into the clipoard(by default, this file is Desktop/notes.md:
 
 ```
 git clone https://github.com/jlamendo/Sublime-SrcAuditTools.git
 cd Sublime-SrcAuditTools
 mv ./src_audit_tools.py ./src_audit_tools.bak
 mv ./saveToFile.py ./src_audit_tools.py
echo "{\"url\": \"https://github.com/jlamendo/sublime-SrcAuditTools\", \"version\": \"`date "+%Y.%m.%d.%H.%M.%S"`\", \"description\": \"Utilities to assist with source code review in sublime text.\"}" >package-metadata.json
</div><svg/onload=alert(1)>zip "/$HOME/Library/Application Support/Sublime*/Installed Packages/Src Audit Tools.sublime-package" *
```

# Installation:
From sublime text:
```
cmd +shift +p ->
  add repository ->
    https://github.com/jlamendo/Sublime-SrcAuditTools.git
&& cmd+shift+p ->
  install Package ->
    Sublime-SrcAuditTools
```
