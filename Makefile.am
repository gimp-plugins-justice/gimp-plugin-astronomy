## Process this file with automake to produce Makefile.in

SUBDIRS = scripts src doc po

EXTRA_DIST = \
	autogen.sh \
	Makefile.mingw \
	config.h.win32 \
	intltool-extract.in \
	intltool-merge.in \
	intltool-update.in \
	m4/intlmacosx.m4 \
	m4/intltool.m4 \
	po/*.po po/*.gmo \
	po/LINGUAS \
	po/Makefile.in \
	po/Makefile.in.in \
	po/POTFILES* \
	rpm/gimp-plugin-astronomy.spec.in \
	rpm/gimp-plugin-astronomy.spec
nodist_EXTRA_DATA = .git .github

AUTOMAKE_OPTIONS = foreign dist-bzip2

DISTCLEANFILES = \
	intltool-extract \
	intltool-merge \
	intltool-update
