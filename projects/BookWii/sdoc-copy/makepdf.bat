rem http://www.alles.or.jp/~torutk/oojava/maneuver/2000/9-1.html
rem http://www.klavis.info/pdfmake.html


rem platex LearnMathPhysicsWithWiiRemote.sdoc.tex
rem C:\tex\bin\dvipdfm.exe LearnMathPhysicsWithWiiRemote.sdoc.dvi

platex all.tex
jbibtex all
platex all
platex all
out2uni all
platex all
dvipdfm.exe all.dvi
"C:\Program Files\Adobe\Reader 8.0\Reader\AcroRd32.exe" all.pdf

