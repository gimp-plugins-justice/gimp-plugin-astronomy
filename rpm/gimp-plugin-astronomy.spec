%define         moname        %{name}
%define         plugindir     %{_libdir}/gimp/2.0/plug-ins
%define         scriptdir     %{_datadir}/gimp/2.0/scripts

Name:           gimp-plugin-astronomy
Version:        0.10
Release:        0
Summary:        Astronomy plugins for the GIMP graphic editor
License:        GPLv2+
Group:          Graphics/Editors and Converters

URL:            http://hennigbuam.de/georg/gimp.html
Source0:        http://www.hennigbuam.de/georg/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:  intltool
BuildRequires:  gtk+2-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gimp-2.0)
Requires:       gimp >= 2.6.0
Requires:       libfftw3
#Requires:       libgsl25


%description
Gimp Astronomy is a set of plug-ins for the Gimp graphic editor
intended for astronomical image processing. They support various basic
and more advanced tasks such as aligning and stacking images with
arithmetic, geometric, median, or sigma mean, removing dark frames and
dividing by a flat field. Some plug-gins are designed for creating
synthetic stars distribution or synthetic galaxy images.


%prep
%setup -q

%build
autoreconf -ivs
automake
%configure
%make_build


%install
%make_install
%find_lang %{moname}


# Upstream provides no tests.


%files -f %{moname}.lang
%doc README AUTHORS COPYING
%doc documentation.pdf documentation.tex
%{scriptdir}/background_gradient_batch.scm
%{scriptdir}/border_information.scm
%{scriptdir}/brightness_contrast_batch.scm
%{scriptdir}/dark_subtraction.scm
%{scriptdir}/flat_division.scm
%{scriptdir}/mode_batch.scm
%{scriptdir}/normalize_batch.scm
%{plugindir}/astronomy-alignment
%{plugindir}/astronomy-artificial-galaxy
%{plugindir}/astronomy-artificial-stars
%{plugindir}/astronomy-background-gradient
%{plugindir}/astronomy-merge
%{plugindir}/astronomy-star-rounding


%changelog
