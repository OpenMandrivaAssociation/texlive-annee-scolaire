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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a macro \anneescolaire to automatically write the
academic year in the French way, according to the date of compilation,
two other macros to obtain the first and the second calendar year of the
academic year, a macro to be redefined to change the presentation of the
years.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/annee-scolaire
%dir %{_datadir}/texmf-dist/source/latex/annee-scolaire
%dir %{_datadir}/texmf-dist/tex/latex/annee-scolaire
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/LISEZMOI.md
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/MANIFEST.md
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/README.md
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/annee-scolaire-eng.pdf
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/annee-scolaire-eng.tex
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/annee-scolaire-fra.pdf
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/annee-scolaire-fra.tex
%doc %{_datadir}/texmf-dist/doc/latex/annee-scolaire/annee-scolaire.pdf
%doc %{_datadir}/texmf-dist/source/latex/annee-scolaire/annee-scolaire.dtx
%doc %{_datadir}/texmf-dist/source/latex/annee-scolaire/annee-scolaire.ins
%{_datadir}/texmf-dist/tex/latex/annee-scolaire/annee-scolaire.sty
