Name:		texlive-annee-scolaire
Version:	55988
Release:	1
Summary:	Automatically typeset the academic year (French way)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/annee-scolaire
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/annee-scolaire.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/annee-scolaire.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/annee-scolaire.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a macro \anneescolaire to automatically
write the academic year in the French way, according to the
date of compilation, two other macros to obtain the first and
the second calendar year of the academic year, a macro to be
redefined to change the presentation of the years.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/annee-scolaire
%{_texmfdistdir}/tex/latex/annee-scolaire
%doc %{_texmfdistdir}/doc/latex/annee-scolaire

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
