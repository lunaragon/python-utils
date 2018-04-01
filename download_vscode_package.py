"""
https://
${publisher}.
gallery.vsassets.io
/_apis/public/gallery
/publisher/${publisher}
/extension/${extension name}
/${version}/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage

From url above, we need provide three information:
    publisher, extension name, and version
```bash
# example
python download_vscode_package.py publisher extension_name version
```
"""
import sys

   
def main():
    publisher = sys.argv[1]
    extension_name = sys.argv[2]
    version = sys.argv[3]

    print(
        ('https://{0}.gallery.vsassets.io/_apis/public/gallery/publisher/'
         '{0}/extension/{1}/{2}/assetbyname/'
         'Microsoft.VisualStudio.Services.VSIXPackage').format(
            publisher, extension_name, version)
        )


if __name__ == '__main__':
    sys.exit(main())
