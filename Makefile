define renderLatex
    cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

reports/tarea_02.pfd: reports/tarea_02.tex
	$(renderLatex)


clean:
	rm --force --recursive reports/pythontex*
	rm --force reports/*.aux
	rm --force reports/*.log
	rm --force reports/*.pdf
	rm --force reports/*.pytxcode
