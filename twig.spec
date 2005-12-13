Summary:	TWIG - webmail and PIM package
Summary(pl):	TWIG - pakiet do poczty WWW i zarz±dzania informacjami osobistymi
Name:		twig
Version:	2.7.7
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://twig.screwdriver.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	03bbdd4d6180789451a2bb20c06f790f
Patch0:		%{name}-php4.patch
URL:		http://twig.screwdriver.net/
Requires:	php
Requires:	php-gettext
Requires:	php-imap
Requires:	php-pcre
Requires:	webserver
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_twigdir	/home/services/httpd/html/twig

%description
This package contains TWIG, a webmail and PIM system which allows you
check mail by any cookie-aware WWW browser.

%description
Ten pakiet zawiera system poczty WWW i zarz±dzania informacjami
osobistymi TWIG, umo¿liwiaj±cy sprawdzanie poczty za pomoc± dowolnej
wspieraj±cej ciasteczka (cookies) przegl±darki WWW.

%prep
%setup -q
%patch0 -p1

%build
for I in `find . -name '*.php3'`; do
	mv "$I" "`echo $I | sed -e 's/php3/php/g'`"
done

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_twigdir}

./twig-install $RPM_BUILD_ROOT%{_twigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS FAQ README TODO UPGRADE docs/*
%dir %{_twigdir}
%dir %{_twigdir}/config
%config(noreplace) %verify(not md5 mtime size) %{_twigdir}/config/*
%{_twigdir}/features
%{_twigdir}/goto.php
%{_twigdir}/images
%{_twigdir}/index.php
%{_twigdir}/lib
%{_twigdir}/test.php
