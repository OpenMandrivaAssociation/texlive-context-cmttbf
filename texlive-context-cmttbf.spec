Name:		texlive-context-cmttbf
Version:	47085
Release:	1
Summary:	Use Computer Modern Typewriter bold font in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/context-cmttbf
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cmttbf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cmttbf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The module makes provision for bold typewriter CM fonts, in
ConTeXt. Such a font may be found in the Computer Modern 'extra
bold' font set.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/context/third/cmttbf
%doc %{_texmfdistdir}/doc/context/third/cmttbf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
