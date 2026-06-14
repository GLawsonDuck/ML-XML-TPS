# ML-XML-TPS

A Python utility to convert XML landmark files output by 
[ML-Morph](https://github.com/agporto/ml-morph) into TPS format 
compatible with TPSDig from [SBMorphometrics](https://www.sbmorphometrics.org/soft-dataacq.html).

## Background

ML-Morph is a machine learning tool for automated morphometric 
landmark detection in images. TPSDig is widely used in geometric 
morphometrics research. These tools use incompatible file formats — 
this script bridges the gap.

## Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## Usage

```bash
python XML_to_TPS_converter.py --input yourfile.xml --output results.tps --height 2848
```

Arguments:
- `--input` : path to the ML-Morph XML output file
- `--output` : desired path for the TPS output file  
- `--height` : image height in pixels (default: 2848)


## Background

Written to support fish morphometrics research at the University 
of Glasgow. Tested on XML output from ML-Morph v[1.0.0].
