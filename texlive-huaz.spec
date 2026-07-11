%global tl_name huaz
%global tl_revision 77576

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Automatic Hungarian definite articles and suffixes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/huaz
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/huaz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/huaz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In Hungarian there are two definite articles, "a" and "az", which are
determined by the pronunciation of the subsequent word. The definite
article is "az", if the first phoneme of the pronounced word is a vowel,
otherwise it is "a". The huaz package helps the user to insert
automatically the correct definite article for cross-references and
other commands containing text. Another service offered by the package
is the automatic suffixing of numbers and cross-references, also based
on their pronunciation.

