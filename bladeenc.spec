Summary:	Blade's MP3 Encoder
Summary(pl):	Encoder MP3 Blade'a
Name:		bladeenc
Version:	0.92.0
Release:	2
Epoch:		1
License:	GPL
Vendor:		Tord Jansson <tord.jansson@swipnet.se>
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://bladeenc.mp3.no/source/%{name}-%{version}-src-stable.tar.gz
URL:		http://bladeenc.mp3.no/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	BladeEnc

%description
BladeEnc is a program to generate MP3 files from WAV or AIFF sound
files.

%description -l pl
BladeEnc jest programem s³u¿±cym do generowania plików MP3 z plików
d¼wiêkowych w formacie WAV lub AIFF.

%prep
%setup -q

%build
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,ChangeLog,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/*
