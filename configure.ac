# -*- Autoconf -*-
dnl Process this file with autoreconf -i to produce a configure script.

AC_PREREQ([2.68])

dnl Name your plug-in here
m4_define([plugin_name], [gimp-plugin-astronomy])

dnl These two define the plug-in version number
m4_define([plugin_major_version], [0])
m4_define([plugin_minor_version], [10])

m4_define([plugin_version], [plugin_major_version.plugin_minor_version])
m4_define([plugin_package_name], [gimp-plugin-astronomy])

AC_INIT([plugin_name],[plugin_version],
   [[https://github.com/gimp-plugins-justice/gimp-plugin-astronomy/issues/]],[plugin_package_name],
   [http://www.hennigbuam.de/georg/gimp.html])

AC_CONFIG_SRCDIR([src/alignment.c])
AC_CONFIG_MACRO_DIR([m4])
AC_CANONICAL_TARGET
AC_CANONICAL_HOST
AC_CANONICAL_BUILD
AC_USE_SYSTEM_EXTENSIONS
AM_INIT_AUTOMAKE([foreign -Wall])
AM_MAINTAINER_MODE([enable])
AM_GNU_GETTEXT_VERSION(0.21)

m4_ifdef([AM_PROG_AR], [AM_PROG_AR])

AC_PROG_CC
AC_PROG_SED
AC_PROG_LN_S
AC_PROG_MKDIR_P
AC_PATH_PROG([STRIP],[strip],[:])
AC_PATH_PROG([GIMPTOOL],[gimptool-2.0],[:])
AC_PATH_PROG([MSGFMT],[msgfmt],[msgfmt])
AC_PATH_PROG([XGETTEXT],[xgettext],[:])
AC_CONFIG_HEADERS([src/config.h],[:])
AC_PROG_INSTALL
AC_PROG_MAKE_SET

msos=
case "$host" in
 *cygwin* | *mingw*)
   msos=yes
esac

# Check for math.h include and math library (some OSes have -lm built-in).
have_libm=maybe
AC_CHECK_HEADER([math.h],
    AC_SEARCH_LIBS([cos],[m],[have_libm=yes]))
if test x"${have_libm}" != xyes; then
    AC_MSG_FAILURE([ERROR: Please install the Math library and math.h],[1])
fi

# Check for package gsl, else gsl_version.h include file and gsl library. GPL
GSL_LIBS=
have_libgsl=maybe
PKG_CHECK_MODULES([GSL],[gsl],[have_libgsl=yes],[have_libgsl=no])
if test x"${have_libgsl}" != xyes; then
  AC_CHECK_HEADER([gsl/gsl_version.h],
     AC_SEARCH_LIBS([gsl_version],[gsl],
        AC_SEARCH_LIBS([cblas_sdsdot],[gslcblas],[have_libgsl=yes])))
fi
if test x"${have_libgsl}" != xyes; then
   AC_MSG_FAILURE([ERROR: Please install the developer version of gsl library.],[1])
fi
AC_SUBST(GSL_LIBS)

# Check for package fftw, else fftw3.h include file and fftw3 library. GPL
FFTW_LIBS=
have_libfftw=maybe
PKG_CHECK_MODULES([FFTW],[fftw3 >= 3.0],[have_libfftw=yes])
if test x"${have_libfftw}" != xyes; then
   AC_CHECK_HEADER([fftw3.h],
      AC_SEARCH_LIBS([fftw_plan_dft_r2c_2d],[fftw3],[have_libfftw=yes]))
fi
if test x"${have_libfftw}" != xyes; then
   AC_MSG_FAILURE([ERROR: Please install the developer version of fftw3 library.],[1])
fi
AC_SUBST(FFTW_LIBS)

# Check for libgimp/gimp.h include file and libgimp library. LGPL
GIMP_CFLAGS=
GIMP_LIBS=
have_libgimp=no
PKG_CHECK_MODULES([GIMP],[gimp-2.0 >= 2.4.0 gimpui-2.0 >= 2.4.0],[have_libgimp=yes])
if test x"${have_libgimp}" != xyes; then
    AC_MSG_FAILURE([ERROR: Please install the developer version of libgimp.],[1])
fi
AC_SUBST(GIMP_CFLAGS)
AC_SUBST(GIMP_LIBS)
GIMP_LIBDIR=`${PKG_CONFIG} --variable=gimplibdir gimp-2.0`
AC_SUBST(GIMP_LIBDIR)
GIMP_DATADIR=`${PKG_CONFIG} --variable=gimpdatadir gimp-2.0`
AC_SUBST(GIMP_DATADIR)

AC_CHECK_FUNCS(bind_textdomain_codeset)

LOCALEDIR='${datadir}/locale'
DATADIR='${datadir}/${plugin_name}'
AC_SUBST(LOCALEDIR)
AC_SUBST(DATADIR)

ACLOCAL="$ACLOCAL $ACLOCAL_FLAGS"
AC_SUBST([ACLOCAL],["${ACLOCAL}"])

AM_CONDITIONAL([HAVEGIMPTOOL],[test "${GIMPTOOL}"x != x])
AM_CONDITIONAL([HAVEMSOS],[test x"${msos}" == xyes])

CPPFLAGS="${CPPFLAGS} AS_ESCAPE([-I${top_builddir}]) AS_ESCAPE([-I${top_srcdir}])"
AC_SUBST([CPPFLAGS],["${CPPFLAGS}"])

AC_DEFINE(PLUGIN_NAME, ["plugin_package_name"], [Plug-In package name])
AC_DEFINE(PLUGIN_VERSION, ["plugin_version"], [Plug-In version])

AC_DEFINE(PLUGIN_MAJOR_VERSION, ["plugin_major_version"], [Plug-In major version])
AC_DEFINE(PLUGIN_MINOR_VERSION, ["plugin_minor_version"], [Plug-In minor version])

GETTEXT_PACKAGE=gimp-plugin-astronomy
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [The gettext translation domain.])
AM_GNU_GETTEXT([external])

AC_SUBST([PLUGIN_NAME],[plugin_name])
AC_SUBST([PLUGIN_PACKAGE_NAME],[plugin_package_name])
AC_SUBST([PLUGIN_VERSION],[plugin_version])

AC_CONFIG_FILES([
Makefile
doc/Makefile
scripts/Makefile
src/Makefile
po/Makefile.in
rpm/gimp-plugin-astronomy.spec
])

AC_OUTPUT

AC_MSG_NOTICE([

Configuration:

  Source code location	${srcdir}
  Build code location	${builddir}
  bindir		${bindir}
  Compiler		${CC}
  CPPFLAGS		${CPPFLAGS}
  GSL_LIBS		${GSL_LIBS}
  FFTW_LIBS		${FFTW_LIBS}
  GIMP_CFLAGS		${GIMP_CFLAGS}
  GIMP_LIBS		${GIMP_LIBS}
  CFLAGS		${CFLAGS}
  LIBS			${LIBS}
])
