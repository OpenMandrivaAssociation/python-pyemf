%define module	pyemf

Summary:	Pure Python Enhanced Metafile Library
Name:		python-%{module}
Version:	2.0.0
Release:	12
License:	LGPLv2.1
Group:		Development/Python
Url:		https://pyemf.sourceforge.net/
Source0:	%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python2)

%description
pyemf is a pure python module that provides bindings for an ECMA-234
compliant vector graphics library. ECMA-234 is the published interface
for the Windows GDI used in the Microsoft windows environment and,
more importantly, natively supported by the OpenOffice suite of tools.

%prep
%setup -qn %{module}-%{version}

%install
%{__python2} setup.py install --root=%{buildroot} --record=FILE_LIST

%files
%doc ChangeLog LICENSE README examples/
%{py2_puresitedir}/*

