Summary:	Tool for generating API documentation for Python modules
Summary(pl.UTF-8):   Narzędzie do generowania dokumentacji API modułów Pythona
Name:		epydoc
Version:	2.1
Release:	4
License:	MIT
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/epydoc/%{name}-%{version}.tar.gz
# Source0-md5:	94c494426c47496ee4d1ed26b580a5a7
Patch0:		%{name}-failed_identifiers.patch
URL:		http://epydoc.sourceforge.net/
BuildRequires:	python-modules >= 2.2.1
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
epytext wywoływany przez prosty język znaczników może służyć do
formatowania wewnętrznych opisów oraz do dodawania informacji o
konkretnych polach, takich jak parametry i zmienne instancji. epydoc
rozumie również wewnętrzne opisy stworzone w ReStructuredText, Javadoc
i w postaci czystego tekstu.

%package gui
Summary:	GUI for epydoc
Summary(pl.UTF-8):   Interfejs graficzny dla epydoc
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-tkinter

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
epytext wywoływany przez prosty język znaczników może służyć do
formatowania wewnętrznych opisów oraz do dodawania informacji o
konkretnych polach, takich jak parametry i zmienne instancji. epydoc
rozumie również wewnętrzne opisy stworzone w ReStructuredText, Javadoc
i w postaci czystego tekstu.

Ten pakiet zawiera graficzny interfejs użytkownika (GUI) dla epydoc.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/epydoc

%dir %{py_sitescriptdir}/epydoc
%{py_sitescriptdir}/epydoc/*.py[co]
%dir %{py_sitescriptdir}/epydoc/test
%{py_sitescriptdir}/epydoc/test/*.py[co]
%exclude %{py_sitescriptdir}/epydoc/gui.py[co]

%dir %{py_sitescriptdir}/epydoc/markup
%{py_sitescriptdir}/epydoc/markup/*.py[co]

%{_mandir}/man1/epydoc.*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epydocgui
%{py_sitescriptdir}/epydoc/gui.py[co]
%{_mandir}/man1/epydocgui.*
