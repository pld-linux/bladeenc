Summary:	Blade's MP3 Encoder
Summary(pl):	Encoder MP3 Blade'a
Name:		bladeenc
Version:	082
Release:	2
Copyright:	LGPL
Vendor:		Tord Jansson <tord.jansson@swipnet.se>
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source:		http://hem.bredband.net/tord/source/%{name}-%{version}-src-stable-2.tar.gz
URL:		http://hem.bredband.net/tord/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	BladeEnc

%description
BladeEnc is a program to generate MP3 files from WAV or AIFF sound files.

%description -l pl
BladeEnc jest programem s³u¿±cym do generowania plików MP3 z plików
d¼wiêkowych w formacie WAV lub AIFF.

%prep
%setup -q -n %{name}-%{version}-src-stable-2

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s bladeenc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc bladeenc.html
%attr(755,root,root) %{_bindir}/*
