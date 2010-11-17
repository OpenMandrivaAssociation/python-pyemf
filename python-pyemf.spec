%define module	pyemf
%define name	python-%{module}
%define version 2.0.0
%define release %mkrel 1

Summary:	Pure Python Enhanced Metafile Library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	LGPLv2.1
Group:		Development/Python
Url:		http://pyemf.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

%description
pyemf is a pure python module that provides bindings for an ECMA-234
compliant vector graphics library. ECMA-234 is the published interface
for the Windows GDI used in the Microsoft windows environment and,
more importantly, natively supported by the OpenOffice suite of tools.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README examples/
%py_puresitedir/*
