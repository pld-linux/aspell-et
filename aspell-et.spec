Summary:	Estonian dictionary for aspell
Summary(pl):	S³ownik estoñski dla aspella
Name:		aspell-et
Version:	0.1.21
%define	subv	1
Release:	1
License:	Custom
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/et/aspell6-et-%{version}-%{subv}.tar.bz2
# Source0-md5:	82929f49ddc1149b6ef2bde4c3c12bcd
URL:		http://wordlist.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Estonian dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik estoñski (tzn. lista s³ów) dla aspella.

%prep
%setup -q -n aspell6-et-%{version}-%{subv}

%build
# Note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright
%{_libdir}/aspell/*
%{_datadir}/aspell/*
