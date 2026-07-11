%global tl_name annee-scolaire
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Automatically typeset the academic year (French way)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/annee-scolaire
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/annee-scolaire.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/annee-scolaire.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/annee-scolaire.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a macro \anneescolaire to automatically write the
academic year in the French way, according to the date of compilation,
two other macros to obtain the first and the second calendar year of the
academic year, a macro to be redefined to change the presentation of the
years.

