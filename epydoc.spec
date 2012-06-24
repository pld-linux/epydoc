Summary:	Tool for generating API documentation for Python modules
Summary(pl):	Narz�dzie do generowania dokumentacji API modu��w Pythona
Name:		epydoc
Version:	2.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	fbb0bd482a872795c59f897b699f9549
URL:		http://epydoc.sourceforge.net/
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
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

%description -l pl
epydoc jest narz�dziem do generowania dokumentacji API modu��w Pythona
w oparciu o ich wewn�trzne opisy (docstrings). Jako przyk�ad wyniku
jego dzia�ania mo�na obejrze� jego w�asn� dokumentacj� (html, pdf).
epytext wywo�ywany przez prosty j�zyk znacznik�w mo�e s�u�y� do
formatowania wewn�trznyvh opis�w oraz do dodawania informacji o
konkretnych polach, takich jak parametry i zmienne instancji. epydoc
rozumie r�wnie� wewn�trzne opisy stworzone w ReStructuredText, Javadoc
i w postaci czystego tekstu.

%package gui
Summary:	GUI for epydoc
Summary(pl):	Interfejs graficzny dla epydoc
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
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

%description gui -l pl
epydoc jest narz�dziem do generowania dokumentacji API modu��w Pythona
w oparciu o ich wewn�trzne opisy (docstrings). Jako przyk�ad wyniku
jego dzia�ania mo�na obejrze� jego w�asn� dokumentacj� (html, pdf).
epytext wywo�ywany przez prosty j�zyk znacznik�w mo�e s�u�y� do
formatowania wewn�trznyvh opis�w oraz do dodawania informacji o
konkretnych polach, takich jak parametry i zmienne instancji. epydoc
rozumie r�wnie� wewn�trzne opisy stworzone w ReStructuredText, Javadoc
i w postaci czystego tekstu.

Ten pakiet zawiera graficzny interfejs u�ytkownika (GUI) dla epydoc.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/epydoc

%dir %{py_sitedir}/epydoc
%{py_sitedir}/epydoc/*.py[co]
%exclude %{py_sitedir}/epydoc/gui.py[co]

%dir %{py_sitedir}/epydoc/markup
%{py_sitedir}/epydoc/markup/*.py[co]

%{_mandir}/man1/epydoc.*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/epydocgui
%{py_sitedir}/epydoc/gui.py[co]

%{_mandir}/man1/epydocgui.*
