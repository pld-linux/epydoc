Summary:	Tool for generating API documentation for Python modules
Summary(pl.UTF-8):	Narzędzie do generowania dokumentacji API modułów Pythona
Name:		epydoc
Version:	3.0.1
Release:	6
License:	MIT
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/epydoc/%{name}-%{version}.zip
# Source0-md5:	43223b2139c59ec60f064564bea82bf4
Patch0:		%{name}-rst.patch
Patch1:		%{name}-__package__.patch
Patch2:		%{name}-cons_fields_stripping.patch
URL:		http://epydoc.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
epydoc is a tool for generating API documentation for Python modules,
based on their docstrings. For an example of epydoc's output, see the
API documentation for epydoc itself (html, pdf). A lightweight markup
language called epytext can be used to format docstrings and to add
information about specific fields, such as parameters and instance
variables. epydoc also understands docstrings written in
ReStructuredText, Javadoc and plaintext.

%description -l pl.UTF-8
epydoc jest narzędziem do generowania dokumentacji API modułów Pythona
w oparciu o ich wewnętrzne opisy (docstrings). Jako przykład wyniku
jego działania można obejrzeć jego własną dokumentację (html, pdf).
Dostępny jest prosty język znaczników o nazwie epytext, który można
wykorzystać do formatowania wewnętrznych opisów oraz do dodawania
informacji o konkretnych polach, takich jak parametry i zmienne
instancji. epydoc rozumie również wewnętrzne opisy stworzone w
formatach ReStructuredText i Javadoc oraz w postaci czystego tekstu.

%package gui
Summary:	GUI for epydoc
Summary(pl.UTF-8):	Interfejs graficzny dla epydoc
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-tkinter >= 2.2.1

%description gui
epydoc is a tool for generating API documentation for Python modules,
based on their docstrings. For an example of epydoc's output, see the
API documentation for epydoc itself (html, pdf). A lightweight markup
language called epytext can be used to format docstrings and to add
information about specific fields, such as parameters and instance
variables. epydoc also understands docstrings written in
ReStructuredText, Javadoc and plaintext.

This package contains GUI program for epydoc.

%description gui -l pl.UTF-8
epydoc jest narzędziem do generowania dokumentacji API modułów Pythona
w oparciu o ich wewnętrzne opisy (docstrings). Jako przykład wyniku
jego działania można obejrzeć jego własną dokumentację (html, pdf).
Dostępny jest prosty język znaczników o nazwie epytext, który można
wykorzystać do formatowania wewnętrznych opisów oraz do dodawania
informacji o konkretnych polach, takich jak parametry i zmienne
instancji. epydoc rozumie również wewnętrzne opisy stworzone w
formatach ReStructuredText i Javadoc oraz w postaci czystego tekstu.

Ten pakiet zawiera graficzny interfejs użytkownika (GUI) dla epydoc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%py_install

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/apirst2html.py
%attr(755,root,root) %{_bindir}/epydoc
%{_mandir}/man1/epydoc.1*
%{py_sitescriptdir}/epydoc
%exclude %{py_sitescriptdir}/epydoc/gui.py[co]
%{py_sitescriptdir}/epydoc-%{version}-py*.egg-info

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epydocgui
%{py_sitescriptdir}/epydoc/gui.py[co]
%{_mandir}/man1/epydocgui.1*
