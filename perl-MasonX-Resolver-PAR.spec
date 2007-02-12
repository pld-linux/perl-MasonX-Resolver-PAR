#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MasonX
%define		pnam	Resolver-PAR
Summary:	MasonX::Resolver::PAR - get Mason components from a PAR file
Summary(pl.UTF-8):   MasonX::Resolver::PAR - pobieranie komponentów Masona z pliku PAR
Name:		perl-MasonX-Resolver-PAR
Version:	0.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	85b7ea68b962f9e19002e9239ed222e5
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	apache1-mod_perl
BuildRequires:	perl-HTML-Mason >= 1.1
BuildRequires:	perl-PAR >= 0.62
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a custom Mason Resolver which loads it's content from a PAR
archive. This is meant to be used in conjunction with Apache::PAR.

%description -l pl.UTF-8
To jest własny obiekt Mason Resolver ładujący swoją zawartość z
archiwum PAR. Jest przeznaczony do używania w połączeniu z
Apache::PAR.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a sample $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
