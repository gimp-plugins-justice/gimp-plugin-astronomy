## Process this file with automake to produce Makefile.in


if HAVEMSOS
astrodir=${GIMP_DATADIR}/doc
else
astrodir=${docdir}
endif
documentationdocsdir=${astrodir}
documentationdocs_DATA = \
	documentation.tex \
	documentation.pdf

documentation.pdf: documentation.tex
	pdflatex documentation.tex

EXTRA_DIST = \
	align.jpg \
	artificial_galaxy.jpg \
	artificial_stars.jpg \
	background_gradient.jpg \
	border_information.jpg \
	documentation.pdf \
	documentation.tex \
	merge.jpg \
	star_rounding_drawing.png \
	star_rounding.jpg \
	star_rounding_long.png \
	star_rounding_rounded.png
