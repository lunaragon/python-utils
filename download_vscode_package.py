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
import fire


def get_download_url(publisher, ext_name, version):
    """
        get visual studio code extension off-line download url
    """
    return ('https://{0}.gallery.vsassets.io/_apis/public/gallery/publisher/'
         '{0}/extension/{1}/{2}/assetbyname/'
         'Microsoft.VisualStudio.Services.VSIXPackage').format(
            publisher, ext_name, version)


def main():
    fire.Fire(get_download_url)


if __name__ == '__main__':
    sys.exit(main())
