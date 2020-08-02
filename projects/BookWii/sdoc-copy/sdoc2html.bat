@echo on
del /Q xml.bak
echo --copy start---
rem LFNFOR OFF
mkdir xml.bak
FOR %%A IN (*.xml) DO copy %%A xml.bak
echo ----- xml.bakフォルダにコピー終了 -----

FOR %%A IN (*.xml) DO sdoc -format:html4 -html4.css.include:link %%A
rem sdoc -format:html4 -html4.css.include:link all.xml
rem java -Xmx128M -jar C:\cygwin\usr\local\lib\sdoc\SmartDoc.jar %1 %2 %3 %4 %5 %6 %7 %8 %9
