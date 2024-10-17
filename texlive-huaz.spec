Name:		texlive-huaz
Version:	71180
Release:	1
Summary:	Automatic Hungarian definite articles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/huaz
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/huaz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/huaz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In Hungarian there are two definite articles, "a" and "az",
which are determined by the pronunciation of the subsequent
word. The definite article is "az", if the first phoneme of the
pronounced word is a vowel, otherwise it is "a". The huaz
package helps the user to insert automatically the correct
definite article for cross-references and other commands
containing text.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/huaz
%doc %{_texmfdistdir}/doc/latex/huaz

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
