# Photoshop Script Chain

Photoshop scripting tool to chain transformations together. The tool is under development, so it works with a selected set of tranformations, e.g. _crop, rotation, flip, scale, copy paste from same image, blur, motion blur, unsharp_.

### Requisites:
* Python 2 or 3
* Photoshop (tested with Photoshop CC Release 2017 1.1)
* Adobe Extendscript Toolkit CC (tested with ExtendScript 4.5.5)

### Usage:
We refer to the root directory of the repository as `$ROOT`. Folder 'test' contains some test files you can use for check the tool out. 
In particular:
- _$ROOT/test/journal_from_JT.json_ journal file generated with MediFor journaling tool
- _$ROOT/test/img_src/*_ test images to process

Intended use case is the following:
##### 1. Journal translation

```
cd $ROOT
python jt_parser.py test/journal_from_JT.json test/parsed_journal_for_PS.json
```
input: json journal from MediFor journaling tool
output: json with ordered operations chain

##### 2. Image transformation
**2.1** Open _photoshop_chain.jsx_ with Adobe Extendscript Toolkit and set `rootDir` to `$ROOT`
**2.2** Execute _photoshop_chain.jsx_ (Photoshop should open up automatically)
Output images are saved in `$ROOT`/test/img_dst

## Disclaimer notice 
Users agree to the following restrictions on the utilization of this code:

- Redistribution: This code, in whole or in part, will not be further distributed, published, copied, or disseminated in any way or form whatsoever, whether for profit or not.
- Modification and Commercial Use: This code, in whole or in part, may not be modified or used for commercial purposes, without a formal agreement with the authors of the considered code.
- Citation: All documents and papers that report on activities that exploit this code must acknowledge its use by including an appropriate citation to the related publications.
- Indemnification: The authors are not responsible for any and all losses, expenses, damages, resulting from the use of this code.
