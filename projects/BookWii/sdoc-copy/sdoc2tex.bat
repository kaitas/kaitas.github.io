rem sdoc -verbose -toc -index -format:html3,html4,latex2e -packager:dir test.sdoc
rem sdoc -verbose -toc -index -format:latex2e -packager:file LearnMathPhysicsWithWiiRemote.sdoc.xml
rem sdoc -verbose -toc -index -format:latex2e -packager:file all.xml -latex2e.dvips.package:graphicx -latex2e.dvips.options:dvipdfm
sdoc -verbose -toc -index -format:latex2e -packager:file all.xml

sdoc -format:html4 -html4.css.include:link -split:chapter all.xml

rem del LearnMathPhysicsWithWiiRemote.sdoc.dvi
rem del LearnMathPhysicsWithWiiRemote.sdoc.aux
rem del LearnMathPhysicsWithWiiRemote.sdoc.idx

