Name:		python-construct
Version:	2.10.70
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/construct/construct-%{version}.tar.gz
Summary:	A powerful declarative symmetric parser/builder for binary data
URL:		https://pypi.org/project/construct/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A powerful declarative symmetric parser/builder for binary data

%files
%{py_sitedir}/construct
%{py_sitedir}/construct-*.*-info
